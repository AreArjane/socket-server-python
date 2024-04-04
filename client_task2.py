#TASK 3
import argparse
import ipaddress
from socket import *

def check_port(val):
    '''
        Description
        -This function validate the port number, number of siffer and as it in the valid format
        Param
        -Val: port number to validate
        Returns
        -Port number as an integers
        Raises
        -argparse.ArgumentTypeError: If the input is not a valid integer or is out of the allowed range.
    '''
    try:
        value = int(val)
    except ValueError:
        raise argparse.ArgumentTypeError('An integer are required for port number')
    if value not in range(1024, 65535 + 1):
        raise argparse.ArgumentTypeError("Invalid port. It must be within the range [1024,65535]")
    return value

def check_ip(address):
    """
    Description:
    Validates the IP address to ensure it is in the correct format
    Parameters:
    -address: The IP address to validate
    Returns:
    -The validated IP address as a string and accept only 127.0.0.1
    Raises:
    -argparse.ArgumentTypeError: If the input is not a valid IP address
    """
    try:
        val = ipaddress.ip_address(address)
        ip = str(val)
        if ip == '127.0.0.1':
            return val
        else:
            raise ValueError
    except ValueError:
        raise argparse.ArgumentTypeError("Invalid IP.  It must in this format: 127.0.0.1")
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
    requests a file, and prints the server's response. The connection is killed after that
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
           #process Get request to server
           headers_req = f"GET /{args.filename} HTTP/1.1\r\nHost: {args.ip}:{args.port}\nUser-Agent: Command-Line\r\n\r\n"
           #retrive data from server
           client_sd.sendall(headers_req.encode())
           
           recieved_line = client_sd.recv(4096)
           print(recieved_line.decode())
          
           client_sd.close()
           
               
# Run the main function
if __name__ == "__main__":
    main()