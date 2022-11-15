import socket
import random
import sys
import pa3_packet
import pickle
import csv
import time

port = int(sys.argv[1])

host = socket.gethostname()
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientSocket.connect( (host,port))

#read pakcets, and create packets
packet_list = []
with open('packets.csv', encoding='utf-8-sig') as packets_csv:
    csv_reader = csv.reader(packets_csv, delimiter=',', skipinitialspace=True)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            packet_list.append(pa3_packet.Packet(row[0],row[1],int(row[2]),int(row[3]),row[4]))
            line_count += 1

# final packet thats sent with special values
last_pack = pa3_packet.Packet('na','na',-1,-1,'last')
packet_list.append(last_pack)

# send packets
i = 0
print(len(packet_list))
while(i < len(packet_list)):
    data = pickle.dumps(packet_list[i])
    clientSocket.send(data)
    print("Sending Packet:" + str(packet_list[i].get_src_ip_address()) + " " + packet_list[i].get_dst_ip_address())
    time.sleep(.25)
    i = i+1


