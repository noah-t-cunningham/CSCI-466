import socket
import sys
import os
import packet
import pickle
import csv
import random
from _thread import *

print("Server starting...")

# inputs
port = int(sys.argv[1])
MSS = int(sys.argv[2])
PCP = float(sys.argv[3])

host = socket.gethostname()

_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    _socket.bind((host, port))
except socket.error as e:
    print(str(e))

_socket.listen()
print("Server is ready for connections")
connection, addr1 = _socket.accept()

incoming_pack_list = []

while True:

    # recieves packets
    data = connection.recv(1024)
    pack = pickle.loads(data)
    # checks if corrupted and send ack_nak packet
    if(pack.get_corruption() == 0):
        ack_nak = packet.Packet(-1,-1,0,-1,'',-1)
        ack_nak_data = pickle.dumps(ack_nak)
        connection.send(ack_nak_data)
        incoming_pack_list.append(pack)
    elif (pack.get_corruption() == 1):
        ack_nak = packet.Packet(-1, -1, 1, -1, '', -1)
        ack_nak_data = pickle.dumps(ack_nak)
        connection.send(ack_nak_data)

    #print("Message: " + pack.get_message())
    # exit loop
    if pack.get_last_packet() == 1:
        break

full_message = ""
for i in incoming_pack_list:
    if i.get_last_packet() == 0:
        full_message = full_message + i.get_message()

print("Recieved Message: ", full_message)
split_message = full_message.split()
#print("split_message: ", split_message)
# translate message
with open('pirate.csv', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', skipinitialspace=True)
    line_count = 0
    for i in range(len(split_message)):
        for row in csv_reader:
            if row[0] == split_message[i]:
                split_message[i] = row[1]
                line_count += 1
        csv_file.seek(0)

translated_message = " ".join(split_message)
print("Translated Message to Send: ", translated_message)

# segment sentence
segmented_sentence = [translated_message[i:i+MSS] for i in range(0, len(translated_message), MSS)]

#create packets
outgoing_packet_list = []
for i in range(len(segmented_sentence)):
    outgoing_packet_list.append(packet.Packet(i + 1, 0, 2, len(segmented_sentence[i]), segmented_sentence[i], 0))

# final packet thats sent with special values
last_pack = packet.Packet(-1,-1,-1,-1,'', 1)
outgoing_packet_list.append(last_pack)

i = 0
while(i < len(outgoing_packet_list)):
    outgoing_packet_list[i].set_corruption(0)
    if random.random() < PCP:
        #print("setting coruption")
        outgoing_packet_list[i].set_corruption(1)
    data = pickle.dumps(outgoing_packet_list[i])
    connection.send(data)
    print("Sending Packet" + str(outgoing_packet_list[i].get_sequence()) + " " + outgoing_packet_list[i].get_message())
    ack_nak_data = connection.recv(1024)
    ack_nak = pickle.loads(ack_nak_data)
    if ack_nak.get_ack_nak() == 0:
        print("Recieved Ack")
        i = i + 1
    else:
        print("Recieved Nak")

print("Server Done")

