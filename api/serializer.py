from rest_framework import serializers
from .models import MyPacket


class PacketSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyPacket
        fields = '__all__'
