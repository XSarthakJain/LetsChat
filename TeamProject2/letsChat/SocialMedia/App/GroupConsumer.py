import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class GroupConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        # self.room_group_name = 'Shubham'
        # print(self.room_group_name)
        # print(self.room_name)

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        print(text_data)
        text_data_json = json.loads(text_data)
        uname = text_data_json['username']
        loggedUserFullName = text_data_json['loggedUserFullName']
        loggedUserPic = text_data_json['loggedUserPic']
        sender = text_data_json['sender']
        # receiver = text_data_json['receiver']
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'username':uname,
                'loggedUserFullName':loggedUserFullName,
                'loggedUserPic':loggedUserPic,
                'sender':sender,
                # 'receiver':receiver,
                'message': message,
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        username = event['username']
        loggedUserFullName = event['loggedUserFullName']
        loggedUserPic = event['loggedUserPic']
        sender = event['sender']
        # receiver = event['receiver']
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'username':username,
            'loggedUserFullName':loggedUserFullName,
            'sender':sender,
            # 'receiver':receiver,
            'loggedUserPic':loggedUserPic,
        }))