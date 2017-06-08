from contextlib import contextmanager
import os
if __name__ == '__main__':
    import socket
    import time

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 8003))
    time.sleep(2)
    sock.send(b'2')
    print(sock.recv(1024))
    sock.close()

@contextmanager
def ignored(*exception):
    try:
        yield
    except exception:
        pass

with ignored(OSError):
    os.remove('somefile.tmp')