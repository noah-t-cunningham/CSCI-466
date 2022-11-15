import socket
import random
import sys
import pa3_packet
import pickle
import csv

class Router:
    def __init__(self, name: str, connections: list, list_of_ip_addresses: list, rules: dict):
        self.name = name
        self.list_of_ip_addresses = list_of_ip_addresses
        self.connections = connections
        self.rules = rules

def which_router(val, router_list):
    for obj in router_list:
        if obj.name == val:
            return obj

def forward(packet, parsed_value, router_list):
    #forward to parsed_value[1]
    router = which_router(parsed_value[1], router_list)
    print("Forwarding packet to router ", router.name)
    arrival(packet, router_list, router)
def drop():
    print("Packet is Being Dropped")
    print("Moving on to next packet")
    return

def modify(packet, parsed_value, router_list, router):
    print("Modifying packet: ", parsed_value[1], '=', parsed_value[2])
    if parsed_value[1] == 'dst_ip_address':
        packet.set_dst_ip_address(parsed_value[2])
    elif parsed_value[1] == 'src_ip_address':
        packet.set_src_ip_address(parsed_value[2])
    elif parsed_value[1] == 'src_tl_port':
        packet.set_src_tl_port(parsed_value[2])
    elif parsed_value[1] == 'dst_tl_port':
        packet.set_dst_tl_port(parsed_value[2])
    elif parsed_value[1] == 'protocol':
        packet.set_protocol(parsed_value[2])
    arrival(packet, router_list, router)

#fucntion to make sure i dont have to rewrite a bunch of code
def execute(parsed_key, packet, router_list, router, key):
    print("Rule found: ", key)
    value = router.rules[key]
    if '=' in value:
        parsed_value = value.split('=')
    else:
        parsed_value = [value]

    if parsed_value[0] == 'Forward':
        forward(packet, parsed_value, router_list)
    if parsed_value[0] == 'Drop':
        drop()
        return
    if parsed_value[0] == 'Modify':
        modify(packet, parsed_value, router_list, router)

def arrival(packet, router_list, router):
    print("Packet arrives at router ", router.name)

    # check if ip in subnet
    if packet.dst_ip_address in router.list_of_ip_addresses:
        print("IP found in subnet!")
        print("Delivering packet...")
        print("Moving on to next packet")
        return
    else:
        print("No matching ip addresses in subnet...")

    # check rules
    print("Checking rules for router ", router.name)
    iter = 0
    for key in router.rules:
        parsed_key = key.split("=")
        if parsed_key[0] == 'dst_ip_address':
            if parsed_key[1] == packet.get_dst_ip_address():
                execute(parsed_key, packet, router_list, router, key)
                return
        elif parsed_key[0] == 'src_ip_address':
            if parsed_key[1] == packet.get_src_ip_address():
                execute(parsed_key, packet, router_list, router, key)
                return
        elif parsed_key[0] == 'src_tl_port':
            if int(parsed_key[1]) == int(packet.get_src_tl_port()):
                execute(parsed_key, packet, router_list, router, key)
                return
        elif parsed_key[0] == 'dst_tl_port':
            if int(parsed_key[1]) == int(packet.get_dst_tl_port()):
                execute(parsed_key, packet, router_list, router, key)
                return
        elif parsed_key[0] == 'protocol':
            if parsed_key[1] == packet.get_protocol():
                execute(parsed_key, packet, router_list, router, key)
                return
        iter = iter + 1
    if len(router.rules) == iter:
        print("No rules found... Packet is being dropped")
        print("Moving on to next packet")
        return

#read routers
routers_list = []
empty_dict = {}
with open('routers.csv', encoding='utf-8-sig') as router_csv:
    csv_reader = csv.reader(router_csv, delimiter=',', skipinitialspace=True)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            parsed_links = row[1].split(";")
            parsed_ips = row[2].split(";")
            routers_list.append(Router(row[0], parsed_links, parsed_ips, empty_dict))
            line_count += 1

#read rules
for obj in routers_list:
    line_count = 0
    with open('rules.csv', encoding='utf-8-sig') as rules_csv:
        csv_reader2 = csv.reader(rules_csv, delimiter=',', skipinitialspace=True)
        for row in csv_reader2:
            if line_count == 0:
                line_count += 1
            else:
                if row[0] == obj.name:
                    rules_dict = {}
                    rules_dict[row[2]] = row[1]
                    if len(obj.rules) == 0:
                        obj.rules = rules_dict
                    else:
                        dict1 = obj.rules
                        dict2 = rules_dict
                        dict3 = {**dict1, **dict2}
                        obj.rules = dict3
            line_count += 1

print("Network starting...")

# inputs
port = int(sys.argv[1])


host = socket.gethostname()

_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    _socket.bind((host, port))
except socket.error as e:
    print(str(e))

_socket.listen()
print("Network is ready for connections")
connection, addr1 = _socket.accept()

incoming_pack_list = []

while True:

    # recieves packets
    data = connection.recv(1024)
    pack = pickle.loads(data)
    if pack.get_protocol() == 'last':
        break
    incoming_pack_list.append(pack)

iter = 1
for i in incoming_pack_list:
    print("Packet ", iter)
    print("src_ip_address: ",i.get_src_ip_address())
    print("dst_ip_address: ",i.get_dst_ip_address())
    print("src_tl_port:", i.get_src_tl_port())
    print("dst_tl_port:",i.get_dst_tl_port())
    print("protocol:",i.get_protocol())

    arrival(i, routers_list, routers_list[0])
    iter = iter + 1

print("Server Done")




