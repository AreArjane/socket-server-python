from socket import *
import sys 

# Create a TCP/IP socket
serverSocket = socket(AF_INET, SOCK_STREAM)
port = 8000
server_ip = '127.0.0.1'
serverSocket.bind((server_ip, port))
serverSocket.listen(1)

print('Ready to serve.....')

while True:
    connectionSocket, addr = serverSocket.accept() 
    try:
        # Receive the client's request message
        message = connectionSocket.recv(1024).decode()
        # Extract the requested file name from the message [1] is after /
        filename = message.split()[1]
        

        try:
            
            with open(filename[1:]) as f:
                outputdata = f.read()    
            connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
            print(message)

            if 'Mozilla' in message:
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode())
           
        except FileNotFoundError:
            
             # If the requested file was not found, send HTTP status code 404 Not Found
            connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
            # Send the content of the 404.html file located in templates directory
            connectionSocket.send(open("templates/404.html").read().encode())


    except OSError as e:
        print(f"OS error: {e}")
        connectionSocket.send("HTTP/1.1 500 Internal Server Error\n\n".encode())
        connectionSocket.send("Internal Server Error".encode())
    finally:
        connectionSocket.close()

# Close the server socket and exit the program
serverSocket.close()
sys.exit()
