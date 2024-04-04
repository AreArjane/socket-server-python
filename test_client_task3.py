#TASK 3
import argparse

from socket import *
from client_task2 import check_ip, check_port

# Setup argparse for command line argument parsing
parser = argparse.ArgumentParser(
    prog="ClientConnection",
    description="Try to run the server with IP, port and filename",
    epilog="run with -i IP -p PORTNR -f filename"
    )

# IP address argument
parser.add_argument("-i", "--ip", default="10.0.0.2", required=True)
# Port number argument
parser.add_argument("-p", "--port", type=check_port, required=True)
# Filename argument
parser.add_argument("-f", "--filename", required=True)

# Parse the command line arguments
args = parser.parse_args()


def main():
    '''
    Connects to a server using specified IP address and port
    requests a file, keep-alive connecting to server. 
    '''
    # Create a socket object for the client
    client_sd = socket(AF_INET, SOCK_STREAM)

    # Check if required arguments are provided
    if not args.ip and not args.port and not args.filename:
        parser.error("You should run with -i [IPadresse] -p [port number] -f [filename]")
    else:
            # Connect to the server
           client_sd.connect((args.ip, args.port))
           
           print(f"connected to server {args.ip} with port {args.port}")
          
           recieved_line = client_sd.recv(4096)
           print(recieved_line.decode())
          
           client_sd.close()
           
               
# Run the main function
if __name__ == "__main__":
    main()