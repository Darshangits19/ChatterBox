# chat/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from asgiref.sync import sync_to_async
from .models import PrivateChatMessage

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        if not self.user.is_authenticated:
            await self.close()
            return

        self.other_username = self.scope['url_route']['kwargs']['username']
        self.other_user = await sync_to_async(User.objects.get)(username=self.other_username)

        usernames = sorted([self.user.username, self.other_username])
        self.room_group_name = f"chat_{usernames[0]}_{usernames[1]}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        if hasattr(self, 'room_group_name'):
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
        await self.save_message(message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender_username': self.user.username
            }
        )

    async def chat_message(self, event):
        message = event['message']
        sender_username = event['sender_username']

        await self.send(text_data=json.dumps({
            'message': message,
            'sender_username': sender_username
        }))

    @sync_to_async
    def save_message(self, message):
        PrivateChatMessage.objects.create(
            sender=self.user,
            receiver=self.other_user,
            message=message
        )