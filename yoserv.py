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

# socket timeout
SOCKET_TIMEOUT = 30

# create socket
s = socket.socket(IPV4, TCP)
print(s)

# bind socket
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
print(s)

# listen connect
s.listen(5)

#MEIS
def login(data):
    pass

# conn is child/client socket
def active_connection(conn):
    while True:
        try:
            data = conn.recv(1024)
        except socket.timeout:
            return
        if data == b'NOYO\r\n':    #QUIT
            conn.send(b'200 OK BYE\r\n')
            return
        elif data[:4] == b'MEIS':   #LOGIN USER ie 'MEIS name'
            user = data[5:-2]
            print(f'{user.decode()} logged in.')
            conn.send(b'200 USER OK\r\n')
        elif data == b'YOSR\r\n':      #LIST USERS
            pass
        elif data[:4] == b'YOYO':       #QUEUE YO for someone
            pass
        elif data == b'YOLO\r\n':       #collect YO for me
            pass
        else:
            conn.send(b'400 BAD COMMAND\r\n')

def client_child(conn, addr):
    print(f'{addr} connected')
    conn.settimeout(SOCKET_TIMEOUT)
    active_connection(conn)
    conn.shutdown(socket.SHUT_RDWR)
    conn.close
    print(f'{addr} disconnected')


while True:
    conn, addr = s.accept()
    pid = os.fork()
    if pid == 0:
        client_child(conn, addr)
