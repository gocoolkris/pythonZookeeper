from kazoo.client import KazooClient
from kazoo.client import KazooState
import logging

class ZooConnector(object):

    def __init__(self, host, port):

        self.host = host
        self.port = port
        logging.basicConfig()
        self.client = KazooClient(host + ':' + port, read_only=True)
        self.client.start()

    def is_connected(self):
        return bool(self.client)


    def reconnect(self):
        self.client = KazooClient(self.host + ':' + self.port)

    def disconnect(self):
        self.client.stop()
