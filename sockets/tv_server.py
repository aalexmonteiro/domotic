import argparse, sys, os
sys.path.append(os.path.abspath(os.path.pardir))

from socket_base import SocketBase
from domotic.simulators.tv import TV

# Starting the sockets for device

tv = TV()
tv_sock = SocketBase()
tv_sock.create_socket('127.0.0.4', 65434)
tv_sock.start(tv)