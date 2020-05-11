from rest_framework import serializers

class MessageSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField(max_length=50)
    content = serializers.CharField(max_length=400)
    created = serializers.DateTimeField()