# Program 4

## To Run 

This program will run indefinitely so use ctrl+c
on all terminals to stop

Go to pa4 folder

Open 2 or more terminals

For the all nodes use command:
 
> python node.py [Send Port][Recv Port][# of Packets in Queue][Is Head][Node #]

Setting up the program is a little tricky.

### Send and Recv Port
You need to be attentive to the 'Send Port' and 
'Recv Port' variables. We need to set them up so that 
all the nodes connect in a circle like pattern.

For example a shcema like this needs to have the ports
set up like so
> V represents a connection
 
> Node 1, Node 1 Send Port = Node 2 Recv Port
>
>  V
> 
> Node 2, Node 2 Send Port = Node 3 Recv Port
>
> V
> 
> Node 3, Node 3 Send Port = Node 1 Recv Port
> 
>  V
> 
> Node 1

So if we were to make 3 terminals the commands we would run
would look like
> Node 1 (Head Node)
> >python node.py [6001][6000][5][1][1]
> 
> Node 2
> >python node.py [6002][6001][2][0][2]
>
> Node 3
> >python node.py [6000][6002][4][0][3]

But remember to run the Head Node terminal last.

### Head Node
The head node is what starts the initial sending of the
packet. So first start up all terminals besides the 
head node terminal. And once you have done that you can 
start the head node adn the sending will begin. 

>For the head node make sure to set the 'Is Head' variable to 1

>For the non-head node make sure to set the 'Is Head' variable to 0


### # of Packets in Queue and Node #.
'# of Packets in Queue' and 'Node #' are up to your discretion

# Video Link
https://montana.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=7a4ccb64-364a-47e6-b12a-af6900511669