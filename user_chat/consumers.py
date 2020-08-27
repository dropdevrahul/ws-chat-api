import json
import collections
from rest_framework.authtoken.models import Token
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.scope['user'] = Token.objects.get(key=self.scope['subprotocols'][0]).user # fetch user from subprotocol header which is the inly way to send headr info in websockets
        self.room_name = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = 'chat_%s' % self.room_name
        async_to_sync(self.channel_layer.group_add)(
                self.room_group_name,
                self.channel_name
                )
        self.accept(self.scope["subprotocols"][0]) # its required to send the selected subprotocol otherwise an error will be generated

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
                self.room_group_name,
                self.channel_name
                )

    def receive(self, text_data):
        chat_message = json.loads(text_data)
        async_to_sync(self.channel_layer.group_send)(
                self.room_group_name, {
                        'type': 'chat_message',
                        'message': chat_message['message'],
                        'current_user_id': chat_message['current_user_id']
                    }
                )

    def chat_message(self, event):
        self.send(text_data=json.dumps(event))

