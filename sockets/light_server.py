import argparse, sys, os
sys.path.append(os.path.abspath(os.path.pardir))

from socket_base import SocketBase
from domotic.simulators.light import Light

# Starting the sockets for device

light = Light()
light_sock = SocketBase()
light_sock.create_socket('127.0.0.3', 65433)
light_sock.start(light)