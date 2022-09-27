import socket
import random
import sys

port = int(sys.argv[1])
user = int(sys.argv[2])
choices = ["rock", "paper", "scissors"]
host = socket.gethostname()
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientSocket.connect( (host,port))

if user == 0:
    intro = clientSocket.recv(1024).decode()
    print(intro)
    valid = False
    sentence = input("rock, paper, scissors: ")
    sentence = sentence.lower()
    while sentence not in choices:
        print("404 Error")
        sentence = input("rock, paper, scissors: ")
        sentence = sentence.lower()
    print("200 Ok")
    print("You Selected " + sentence)


    clientSocket.send(sentence.encode())
    response = clientSocket.recv(1024).decode()
    print("Response from server: ",response)

elif user == 1:
    intro = clientSocket.recv(1024).decode()
    print(intro + " you are a CPU")
    cpu_choice = random.choice(choices)
    print("CPU picks " + cpu_choice)
    clientSocket.send(cpu_choice.encode())
    response = clientSocket.recv(1024).decode()
    print("Response from server: ", response)


