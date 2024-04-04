
from socket import *
import sys 
from threading import Thread

#define port
port = 8000
# connected with TCP, bind the server and listened
serverSocket = socket(AF_INET, SOCK_STREAM) 
serverSocket.bind(('',port))
#it can have up to 5 in backlog waiting
serverSocket.listen(5)

def handle_client(connection):
    '''
    Handles the client's request by serving the requested file or a 404 error page.
    
    Parameters:
    - connection: The socket object representing the client connection.
    
    The function first attempts to read and send the requested file. If the file
    cannot be found, it sends a 404 error message along with a default 404 error page.
    '''
    try:
        message = connection.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        print(message)
             
        connection.send("HTTP/1.1 200 OK\r\n\r\n".encode())
          
        #ensure it accessible in browser, so it check User-Agent
        if 'Mozilla' in message:
            for i in range(0, len(outputdata)):
                connection.send(outputdata[i].encode())
        f.close()
        connection.close()
    #exception to not find file, persmission or dir
    except IOError:
        connection.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connection.send(open("templates/404.html").read().encode())
    finally:
        connection.close()

while True:
         print("Reeady to serve......")
        # Accept an incoming connection
         connectionSocket, addr = serverSocket.accept()
        #debugging puposes
         print("server connected by addresse: ", addr)
        # Spawn a new thread to handle the client, passing it the connection socket
         Thread(target=handle_client, args=(connectionSocket,)).start()
    
serverSocket.close()