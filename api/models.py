from django.db import models

# Create your models here.


class MyPacket(models.Model):
    packet_type = models.CharField(max_length=5)
    src_port = models.CharField(max_length=7)
    dest_port = models.CharField(max_length=7)
    src_IP = models.CharField(max_length=20)
    dest_IP = models.CharField(max_length=20)
    data = models.CharField(max_length=100)
