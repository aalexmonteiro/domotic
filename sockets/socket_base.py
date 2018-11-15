import socket
import threading

class SocketBase(object):

    def __init__(self):
        self.s = None

    def create_socket(self, host, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((host, port))
        self.s.listen()

    def start(self, device):
        while True:
            sock, addr = self.s.accept()
            t = threading.Thread(target=self.__handle_tcp, args=(sock, addr, device))
            t.start()
    
    def __handle_tcp(self, sock, addr, device):
        print("new connection from %s:%s" % addr)

        while True:
            received_value = sock.recv(1024)
            value = received_value.decode('utf-8')
            current = device.get()
            if current:
                current = current.decode('utf-8')
            if value == '':
                break
            if current != value:
                device.save(value)
        sock.close()
