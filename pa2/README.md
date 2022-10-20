Programming Assighnemnt 2

To run open 2 terminals.

To start server run    
```
python server.py [PORT_NUMBER] [MAXIMUM_SEGMENT_SIZE] [PACKET_CORRUPT_PROBABILITY]
example:  python client.py 5001 4 .2   //port 5001, segments will be length of 4, 20% corruption probability
```
To start client run
```
python client.py [PORT_NUMBER] [MAXIMUM_SEGMENT_SIZE] [PACKET_CORRUPT_PROBABILITY]
example:  python client.py 5001 4 .2   //port 5001, segments will be length of 4, 20% corruption probability
```

In the client you will be prompted for an inout which when you enter the client
will send the input to the server at which point the server will translate the
message to 'pirate talk', and sent the translated message back to the client.

See pirate.csv for translations