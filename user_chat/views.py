import uuid
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from user_app.models import ApiUser
from .models import ChatRoom
from user_app.serializers import LoggedInUserSerializer

class ChatRoomView(APIView):

    def post(self, request):
        target_user = get_object_or_404(ApiUser, pk=request.data.get('target_user_id'))
        try:
            room = ChatRoom.objects.get(owner=request.user, target=target_user)
        except ChatRoom.DoesNotExist:
            room , _ = ChatRoom.objects.get_or_create(target=request.user, owner=target_user)

        return Response({
                'id': room.id,
                "target_username": target_user.username
            })

