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


host = socket.gethostname()
connection = (host,recv_port)

clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
clientSocket.bind( connection )


if head == 1:
    print("Node ", node, " is the head, so i have the token first")
    print("Node ", node, " has a current queue size of ", packets)
    print("Node ", node, " Sending packet")
    packets -= 1
    clientSocket.sendto(str('token').encode(),(host,send_port))
    time.sleep(3)
    # go into while loop
    print("Node ", node, "Waiting for Connection")
    while True:
        print()
        data = clientSocket.recvfrom(1024)
        print("Node ", node, " has the " + data[0].decode())
        print("Node ", node, " has a current queue size of ", packets)

        if packets == 0:
            print("Node ", node, " has no packets to send")
            clientSocket.sendto(str('token').encode(), (host, send_port))
            time.sleep(3)
            if random.random() < 0.25:
                print("Node ", node, " added a packet")
                packets += 1
        else:
            print("Node ", node, " Sending packet")
            packets -= 1
            clientSocket.sendto(str('token').encode(), (host, send_port))
            time.sleep(3)
            if random.random() < 0.25:
                print("Node ", node, " added a packet")
                packets += 1

else:
    print("Node ", node, " Waiting for Connection")
    while True:
        print()
        data = clientSocket.recvfrom(1024)
        #print("Node ", node, " received packet")
        print("Node ", node, " has the " + data[0].decode())
        print("Node ", node, " has a current queue size of ", packets)
        time.sleep(3)

        if packets == 0:
            print("Node ", node, " has no packets to send")
            clientSocket.sendto(str('token').encode(), (host, send_port))
            time.sleep(3)
            if random.random() < 0.25:
                print("Node ", node, " added a packet")
                packets += 1
        else:
            print("Node ", node, "Sending packet")
            packets -= 1
            clientSocket.sendto(str('token').encode(), (host, send_port))
            time.sleep(3)
            if random.random() < 0.25:
                print("Node ", node, " added a packet")
                packets += 1







