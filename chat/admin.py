from django.contrib import admin
from .models import Friendship, PrivateChatMessage

# Register your new models here.
admin.site.register(Friendship)
admin.site.register(PrivateChatMessage)