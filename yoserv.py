import os
import socket
import sys


# host
HOST = ''

# address family
IPV4 = socket.AF_INET

# tcp
TCP = socket.SOCK_STREAM

# port
PORT = 5000

# create socket
s = socket.socket(IPV4, TCP)
print(s)

# bind socket
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
print(s)

# listen connect
s.listen(5)

# conn is child/client socket
def active_connection(conn):
    data = conn.recv(1024)
    if data == b'QUIT\r\n':
        conn.send(b'Bye!\r\n')
        return
    

def client_child(conn, addr):
    print(f'{addr} connected')
    active_connection(conn)
    conn.shutdown(socket.SHUT_RDWR)
    conn.close
    print(f'{addr} disconnected')


while True:
    conn, addr = s.accept()
    pid = os.fork()
    if pid == 0:
        client_child(conn, addr)
