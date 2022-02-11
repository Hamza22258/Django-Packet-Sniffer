from rest_framework import generics
from .models import MyPacket
from api.serializer import PacketSerializer
from rest_framework.views import APIView
from scapy.all import *
from rest_framework.response import Response
# Create your views here.

# parsePacket()


def packet_callback_tcp(packet):
    type = "TCP"
    if packet[TCP].payload:
        src_ip = packet[IP].src
        dst_ip = packet[IP].src
        src_port = packet[IP].sport
        dst_port = packet[IP].dport
        data = ""
        # print("\n{}:{} ----TCP----> {}:{}".format(src_ip, src_port, dst_ip, dst_port))
        if packet[IP].dport == 80:
            data = str(bytes(packet[TCP].payload))
        datamodel = MyPacket(
            packet_type='TCP',
            src_port=src_port,
            dest_port=dst_port,
            src_IP=src_ip,
            dest_IP=dst_ip,
            data=data
        )
        datamodel.save()
        # print("\n{}", data)


def packet_callback_udp(packet):
    type = "UDP"
    if packet[UDP].payload:
        src_ip = packet[IP].src
        dst_ip = packet[IP].src
        src_port = packet[IP].sport
        dst_port = packet[IP].dport
        datamodel = MyPacket(
            packet_type='UDP',
            src_port=src_port,
            dest_port=dst_port,
            src_IP=src_ip,
            dest_IP=dst_ip,
        )
        datamodel.save()
        # print("\n{}:{} ----UDP----> {}:{}".format(src_ip, src_port, dst_ip, dst_port))


class PacketView(generics.ListAPIView):
    queryset = MyPacket.objects.all()
    serializer_class = PacketSerializer


class Main:
    def __init__(self):
        self.flag = 0

    class Start(APIView):
        """
        View to list all users in the system.

        * Requires token authentication.
        * Only admin users are able to access this view.
        """

        def post(self, request, format=None):
            self.flag = request.data["data1"]
            while self.flag == 0:
                sniff(filter='tcp', prn=packet_callback_tcp,
                      store=0, count=0, timeout=1)
                sniff(filter='udp', prn=packet_callback_udp,
                      store=0, count=0, timeout=1)
            return Response("success")


class Stop(APIView):
    """
    View to list all users in the system.

    * Requires token authentication
    * Only admin users are able to access this view.
    """

    def post(self, request, format=None):
        flag = True
        return Response()


class Delete(APIView):
    """
    View to list all users in the system/

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    def post(self, request, format=None):
        MyPacket.objects.all().delete()
        return Response()
