import argparse, sys, os
sys.path.append(os.path.abspath(os.path.pardir))

from socket_base import SocketBase
from domotic.simulators.audio_system import AudioSystem

# Starting the sockets for device

audio = AudioSystem()
audio_sock = SocketBase()
audio_sock.create_socket('127.0.0.5', 65435)
audio_sock.start(audio)