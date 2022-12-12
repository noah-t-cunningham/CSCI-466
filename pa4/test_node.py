import sys
import random
import socket
import time

# inputs
send_port = int(sys.argv[1])
recv_port = int(sys.argv[2])
packets = int(sys.argv[3])
head = int(sys.argv[4])
node = int(sys.argv[5])
token = 'token'

host = socket.gethostname()
connection = (host,recv_port)

clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
clientSocket.bind( connection )

print("send port ", send_port)
print("recv port ", recv_port)

if head == 1:
    clientSocket.sendto(token.encode(), (host, send_port))

if head == 0:
    print('Waiting for Connection')
    data = clientSocket.recvfrom(1024)
    print('I have the ' + data[0].decode())

# if head == 1:
#     print("I am the head, so i have the token first")
#     print("Sending packet")
#     packets -= 1
#     clientSocket.sendto(str('token').encode(),(host,send_port))
#     time.sleep(3)
#
# else:
#     print('Waiting for Connection')
#     while True:
#         data = clientSocket.recvfrom(1024)
#         print('I have the ' + data[0].decode())
#
#         if packets == 0:
#             print("I have no packets to send")
#             clientSocket.sendto(str('token').encode(), (host, send_port))
#             time.sleep(3)
#             if random.random() < 0.25:
#                 packets += 1
#         else:
#             print("Sending packet")
#             packets -= 1
#             clientSocket.sendto(str('token').encode(), (host, send_port))
#             time.sleep(3)
#             if random.random() < 0.25:
#                 packets += 1







