import argparse, sys, os
sys.path.append(os.path.abspath(os.path.pardir))

from socket_base import SocketBase
from domotic.simulators.air_conditioner import AirConditioner

# Starting the sockets for device
air = AirConditioner()
air_sock = SocketBase()
air_sock.create_socket('127.0.0.2', 65432)
air_sock.start(air)