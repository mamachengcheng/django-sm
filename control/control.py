# **coding: utf-8**
import time
import string
from struct import pack, unpack
from string import ResolveData
from threading import Thread
from sm_socket.socket_client import SocketClient
from sm_socket.socket_server import SocketServer

from socket import gethostname, gethostbyname


class ControlTask(Thread):

    """
    控制stm32
    """
    def __init__(self, address, port):
        super().__init__()
        self.address = address
        self.port = port

    def run(self):
        with SocketClient(address=self.address, port=self.port) as control:
            connect, address = control.accept()
            connect.send('你好'.encode())


class ListenTask(Thread):

    """
    监听stm32
    """
    def __init__(self, address, port):
        super().__init__()
        self.address = address
        self.port = port

    def run(self):
        with SocketServer(address=self.address, port=self.port) as control:
            print("开始监听")
            while True:
                connect, address = control.accept()
                print('连接地址: {0}'.format(address))

                data = connect.recv(1024)
                print('接受数据: {0} 数据类型: {1}'.format(data, type(data)))
                data = unpack('l', data)
                msg = self.check(data[0])
                print("发送消息：{0}".format(msg))

                # connect.send(pack('l', msg))
                msg = ResolveData(data[0])
                state_code, state_semantic, state_msg = msg.get_state()
                step_code, step_semantic, step_msg = msg.get_step()
                active_code, active_semantic, active_msg = msg.get_active()

                print('状态码:{0} 原语:{1} 消息:{2}'.format(state_code, state_semantic, state_msg))
                print('状态码:{0} 原语:{1} 消息:{2}'.format(step_code, step_semantic, step_msg))
                print('状态码:{0} 原语:{1} 消息:{2}'.format(active_code, active_semantic, active_msg))

    @ staticmethod
    def check(msg):
        print(u"接受数据: {0}".format(bin(msg)))
        if string.RESET_FINISHED == msg:
            print(u"复位完成")
            return 0b0000
        elif string.MATERIAL_FINISHED == msg:
            print(u"取料完成")
            return 0b0001
        elif string.PRINTING_FINISHED == msg:
            print(u"打印完成")
            return 0b0010
        elif string.BALE_FINISHED == msg:
            print(u"打包完毕")
            return 0b0011
        else:
            print(u"继续工作")
            return 0b1111

if __name__ == '__main__':
    host_name = gethostname()
    host = gethostbyname(host_name)
    port = 5050
    listen_task = ListenTask(address=host, port=port)
    listen_task.start()
