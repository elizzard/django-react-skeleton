from rest_framework import viewsets, permissions
from .serializers import MessageSerializer
from rest_framework.response import Response


class MessageViewSet(viewsets.ViewSet):
    permission_classes = [ permissions.AllowAny ]
    serializer_class = MessageSerializer

    def list(self, request):
        # serializer = MessageSerializer(message)
        message = {
            'email': 'qwerty@gmail.com',
            'name' : 'Peek-a-boo',
            'content': 'Okie Dokie',
            'created': '2020-01-27T15:17:10.375877',
        }
        return Response(message)