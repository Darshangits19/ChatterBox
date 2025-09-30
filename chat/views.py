# chat/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Friendship, PrivateChatMessage
from django.db.models import Q

@login_required
def home_view(request):
    pending_requests = Friendship.objects.filter(friend=request.user, status='pending')
    accepted_friendships = Friendship.objects.filter(
        Q(creator=request.user) | Q(friend=request.user),
        status='accepted'
    )
    friends = []
    for friendship in accepted_friendships:
        if friendship.creator == request.user:
            friends.append(friendship.friend)
        else:
            friends.append(friendship.creator)

    friends_ids = [friend.id for friend in friends]
    pending_requests_sent_ids = Friendship.objects.filter(creator=request.user).values_list('friend_id', flat=True)
    pending_requests_received_ids = pending_requests.values_list('creator_id', flat=True)
    
    related_user_ids = set(friends_ids) | set(pending_requests_sent_ids) | set(pending_requests_received_ids)
    related_user_ids.add(request.user.id)

    other_users = User.objects.exclude(id__in=related_user_ids)

    context = {
        'friends': friends,
        'pending_requests': pending_requests,
        'other_users': other_users,
    }
    return render(request, 'chat/home.html', context)

@login_required
def send_friend_request(request, user_id):
    receiver = get_object_or_404(User, id=user_id)
    if receiver != request.user:
        Friendship.objects.get_or_create(creator=request.user, friend=receiver)
    return redirect('chat:home')

@login_required
def manage_friend_request(request, friendship_id, action):
    friendship = get_object_or_404(Friendship, id=friendship_id, friend=request.user)
    if action == 'accept':
        friendship.status = 'accepted'
        friendship.save()
    elif action == 'decline':
        friendship.delete()
    return redirect('chat:home')

@login_required
def private_chat_view(request, username):
    friend = get_object_or_404(User, username=username)
    
    friendship = Friendship.objects.filter(
        (Q(creator=request.user, friend=friend) | Q(creator=friend, friend=request.user)),
        status='accepted'
    ).first()
    
    if not friendship:
        return redirect('chat:home')

    past_messages = PrivateChatMessage.objects.filter(
        (Q(sender=request.user, receiver=friend) | 
         Q(sender=friend, receiver=request.user))
    ).order_by('timestamp')

    context = {
        'friend': friend,
        'past_messages': past_messages,
    }
    return render(request, 'chat/private_chat.html', context)