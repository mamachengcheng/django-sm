# **coding: utf-8**
import time
from struct import pack, unpack
from socket import socket, AF_INET, SOCK_STREAM
from socket import gethostname, gethostbyname


class SocketClient:

    def __init__(self, address, port, family=AF_INET, type=SOCK_STREAM):
        self.address = (address, port)
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        self.sock = socket(family=self.family, type=self.type)
        self.sock.connect(self.address)
        self.sock.settimeout(4)
        return self.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()
        self.sock = None

if __name__ == '__main__':
    host_name = gethostname()
    host = gethostbyname(host_name)
    port = 5050

    msgs = [
        0b1000110000000000,          # 复位完成
        0b1001110000000000,          # 取料完成
        0b1010110000000000,          # 打印完成
        0b1011110000000000           # 包装完成
    ]

    for msg in msgs:
        with SocketClient(host, port) as send_service:
            data = pack('l', msg)
            send_service.send(data)
            # data = send_service.recv(1024)
            # data = unpack('l', data)
            # print(data)
            # print("数据发送完毕")


