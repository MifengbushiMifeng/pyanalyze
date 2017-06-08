import socket

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8003))
    sock.listen(5)
    while True:
        con, addr = sock.accept()
        try:
            con.settimeout(5)
            buffer = con.recv(1024)
            if buffer.decode('utf8') == '1':
                con.send(b'socket connected!')
            else:
                con.send(b'socket refused!')
        except socket.timeout:
            print('socket time out.')
        finally:
            con.close()
        con.close()
