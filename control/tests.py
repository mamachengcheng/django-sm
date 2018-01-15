from django.test import TestCase
from threading import Thread
from .control import ListenTask
from socket import gethostname, gethostbyname
# Create your tests here.

host_name = gethostname()
host = gethostbyname(host_name)
port = 5050

ListenTask(address=host, port=port)
ListenTask.daemon = True
ListenTask.start()
ListenTask.join()

