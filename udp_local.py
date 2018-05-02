
#UDP client and server on localhost

import argparse, socket
from datetime import datetime

MAX_BYTES = 65535

def server(ipadress, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ipadress, port))
    print('Listening at {}'.format(sock.getsockname()))
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode('ascii')
        print('The client at {} says {!r}'.format(address, text))
        text = 'Your data was {} bytes long'.format(len(data))
        data = text .encode('ascii')
        sock.sendto(data, address)
