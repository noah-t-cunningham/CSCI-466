import socket
import sys
import os
from _thread import *

print("Server starting...")
port = int(sys.argv[1])
host = socket.gethostname()
inputs = ["rock", "paper", "scissors"]

_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    _socket.bind((host, port))
except socket.error as e:
    print(str(e))

_socket.listen()
print("Server is ready for connections")

winner = "Something Went Wrong"

while True:

    player1_connection, addr1 = _socket.accept()
    print("Player 1 Connected")
    player1_connection.send("Hello Player 1".encode())

    player2_connection, addr2 = _socket.accept()
    print("Player 2 Connected")
    player2_connection.send("Hello Player 2".encode())

    player1_input = player1_connection.recv(1024).decode()
    player2_input = player2_connection.recv(1024).decode()

    if player1_input not in inputs:
        player1_connection.send("Invalid Input".encode())

    if player2_input not in inputs:
        player2_connection.send("Invalid Input".encode())


    if player1_input == player2_input:
        winner = f"Both players selected {player1_input}. It's a tie!"
    elif player1_input == "rock":
        if player2_input == "scissors":
            winner ="Rock smashes scissors! Player 1 Wins"
        else:
            winner ="Paper covers rock! Player 2 Wins"
    elif player1_input == "paper":
        if player2_input == "rock":
            winner ="Paper covers rock! Player 1 Wins"
        else:
            winner ="Scissors cuts paper! Player 2 Wins"
    elif player1_input == "scissors":
        if player2_input == "paper":
            winner = "Scissors cuts paper! Player 1 Wins"
        else:
            winner ="Rock smashes scissors! Player 2 Wins"

    print(winner)
    player1_connection.send(winner.encode())
    player1_connection.close()

    player2_connection.send(winner.encode())
    player2_connection.close()

    break

_socket.close()
