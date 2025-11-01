""""

Author:Alon Fried

Program name:Customer care

Description: A program that connects the client to the server and prints its request on the screen

Date:11/1/25

"""


import socket
import logging


#constants
SERVER_IP = '127.0.0.1'
SERVER_PORT = 6767
MAX_POCKET = 1024

def Connect_Client():
    """
        Connects the client and executes the requested command.

        
        :return: Prints the client request
        """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((SERVER_IP, SERVER_PORT))
        logging.info("client connected successfully")
        while 1 == 1:
            command = input("Enter command (TIME / NAME / RAND / EXIT): ").strip().upper()
            if len(command) == 0:
                logging.info("client inserted a empty command")
                continue
            client_socket.send(command[:4].ljust(4).encode())
            response = client_socket.recv(MAX_POCKET).decode()
            if response == 'GoodBye!':
                logging.info("Finished with client")
                print("thank u for using our service, have a good day!")
                client_socket.close()
                break
            print("Server response:", response)
            
    except socket.error as msg:
        logging.error("client connection filed")
        print("socket error: " + str(msg))
    finally:
        logging.info("client request of closing connection succeeded")
        client_socket.close()


def main():
    Connect_Client()
    

if __name__ == "__main__":
    logging.basicConfig(
    level=logging.INFO,
    format=('%(asctime)s - %(levelname)s - %(message)s'),
    handlers=[
        logging.FileHandler("client_log.file")
    ]
)
    main()
        


