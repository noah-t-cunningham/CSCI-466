import socket
import random
import sys
import packet
import pickle

# inputs port number, Message Segment Length, Chance to Corrupt(whole number)
port = int(sys.argv[1])
MSS = int(sys.argv[2])
PCP = float(sys.argv[3])


host = socket.gethostname()
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientSocket.connect( (host,port))

# where client takes in input
sentence = input("Enter Message:")
sentence = sentence.lower()
print("Message to Send: ", sentence )

# segment sentence
segmented_sentence = [sentence[i:i+MSS] for i in range(0, len(sentence), MSS)]

#create packets
outgoing_packet_list = []
for i in range(len(segmented_sentence)):
    outgoing_packet_list.append(packet.Packet(i + 1, 0, 2, len(segmented_sentence[i]), segmented_sentence[i], 0))

# final packet thats sent with special values
last_pack = packet.Packet(-1,-1,-1,-1,'', 1)
outgoing_packet_list.append(last_pack)

# send packets

# for i in packet_list:
#     data = pickle.dumps(i)
#     clientSocket.send(data)
#     print("Sending Packet" + str(i.get_sequence()) + " " + i.get_message())
#     ack_nak_data = clientSocket.recv(1024)
#     ack_nak = pickle.loads(ack_nak_data)

i = 0
while(i < len(outgoing_packet_list)):
    outgoing_packet_list[i].set_corruption(0)
    if random.random() < PCP:
        #print("setting coruption")
        outgoing_packet_list[i].set_corruption(1)
    data = pickle.dumps(outgoing_packet_list[i])
    clientSocket.send(data)
    print("Sending Packet" + str(outgoing_packet_list[i].get_sequence()) + " " + outgoing_packet_list[i].get_message())
    ack_nak_data = clientSocket.recv(1024)
    ack_nak = pickle.loads(ack_nak_data)
    if ack_nak.get_ack_nak() == 0:
        print("Recieved Ack")
        i = i + 1
    else:
        print("Recieved Nak")

incoming_pack_list = []

while True:

    # recieves packets
    data = clientSocket.recv(1024)
    pack = pickle.loads(data)
    # checks if corrupted and send ack_nak packet
    if(pack.get_corruption() == 0):
        ack_nak = packet.Packet(-1,-1,0,-1,'',-1)
        ack_nak_data = pickle.dumps(ack_nak)
        clientSocket.send(ack_nak_data)
        incoming_pack_list.append(pack)
    elif (pack.get_corruption() == 1):
        ack_nak = packet.Packet(-1, -1, 1, -1, '', -1)
        ack_nak_data = pickle.dumps(ack_nak)
        clientSocket.send(ack_nak_data)

    #print("Message: " + pack.get_message())
    # exit loop
    if pack.get_last_packet() == 1:
        break

full_message = ""
for i in incoming_pack_list:
    if i.get_last_packet() == 0:
        full_message = full_message + i.get_message()

print("Translated Message: ", full_message)
print("")
print("client done")


# send segemnted message, and the length of it
# i = 0
# for segment in segmented_sentence:
#     i = i+1
#
# clientSocket.send(str(i).encode())
#
# for segment in segmented_sentence:
#     clientSocket.send(segment.encode())
#
# recieved_input = clientSocket.recv(1024).decode()
# print(recieved_input)

# while sentence not in choices:
#     print("404 Error")
#     sentence = input("rock, paper, scissors: ")
#     sentence = sentence.lower()
# print("200 Ok")
# print(sentence)
# clientSocket.send(sentence.encode())
# response = clientSocket.recv(1024).decode()
# print("Response from server: ",response)

