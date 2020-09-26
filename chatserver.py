import socket
import time
host = '127.0.0.1' #loopback address
port = 5000

clients = [] #list of all clients that will communicate with server
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #creating a socket object, AF_INET = ipv4 mode, DGRAM = UDP protocol, STREAM = tcp protocol
s.bind((host,port)) 
s.setblocking(0) #set to nonblocking, it will not block when it receives and will grab data, if nothing is available, throws error

quitting = False
print("Server started")
while not quitting:
    try:
        data, addr =s.recvfrom(1024) # try will throw error if no data is received, grabbing data and address that is coming into socket
        if "Quit" in str(data):
           quitting = True #quits server if one of the users send "Quit"
        if addr not in clients: #if the address received is not a part of the client list, append it to the list of clients
            clients.append(addr)
        
        print(time.ctime(time.time()) + str(addr) + ": :"+str(data))#printing timestamp + data sent + address
        for client in clients:
            s.sendto(data, client) #sending the received data/message to all clients on the list
    except:
        pass
s.close()