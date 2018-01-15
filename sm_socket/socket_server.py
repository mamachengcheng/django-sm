# **coding: utf-8**
from socket import socket, gethostname, AF_INET, SOCK_STREAM


class SocketServer:

    def __init__(self, address, port, family=AF_INET, type=SOCK_STREAM):
        self.address = (address, port)
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        # if socket is not None:
        #     raise RuntimeError('Already bind')
        self.sock = socket(family=self.family, type=self.type)
        self.sock.bind(self.address)
        self.sock.listen(5)
        return self.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()
        self.sock = None

