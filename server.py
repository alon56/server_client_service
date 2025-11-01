""""

Author:Alon Fried

Program name:Service care

Description: A program that connects a client to a server and performs the requested command.

Date:11/1/25

"""
import socket
import logging
import datetime
import random


#constants
QUEUE_LINE = 5
MAX_PACKET = 4
HOST = '0.0.0.0'
PORT = 6767
SERVER_NAME = 'Alon_server'


def time() -> str:
    """
        A function that return the current time

        
        :return: The current time
        """
    return datetime.datetime.now().strftime("%H:%M:%S")


def name() -> str:
    """
        A function that return the server name

        :return: The server name
    """
    return SERVER_NAME


def rand() -> str:
    """
        A function that return a random number between 1 - 10 

        :return: A random number between 1 - 10 
    """
    return str(random.randint(1,10))


def handle_client(client_socket :socket.socket, client_address :tuple, client_counter:int):
    """
        A function that connects the client with the server, does as the command that the client requested

        :param message: client_socket that is used to connect the client
        :param message: client_address saves the client IP and port
        :param message: client_counter saves the current client number
        :return: sends the client request
    """
    try:
        while 1 == 1:
            command = client_socket.recv(MAX_PACKET).decode()
            if command == 'TIME':
                logging.info("Sending time")
                client_socket.send(time().encode())
            elif command == 'NAME':
                logging.info("Sending server name")
                client_socket.send(name().encode())
            elif command == 'RAND':
                logging.info("Sending Random number")
                client_socket.send(rand().encode())
            elif command == 'EXIT':
                logging.info("Client closed connection")
                client_socket.send('GoodBye!'.encode())
                break
            else:
                logging.info("Invalid command")
                client_socket.send("Invalid command".encode())
    except socket.error as msg:
        logging.info('received socket error ' + str(msg))
    finally:
        logging.info("finished with client number: " + str(client_counter))
        client_socket.close()


def start_server():
    """
        A function that connects the client to the server

        :return: If an error has accord prints the error
    """
    client_counter = 0
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        logging.info("Starting communication")
        server_socket.bind((HOST, PORT))
        server_socket.listen(QUEUE_LINE)
        while 1 == 1: 
            client_counter += 1
            client_socket, client_address = server_socket.accept()
            logging.info("server connection succeeded")
            handle_client(client_socket, client_address, client_counter)
    except socket.error as msg:
        logging.info("Connection failed," + ' received socket error ' + str(msg))
                

def main():
    start_server()      
        

if __name__ == "__main__":
    logging.basicConfig(
    level=logging.INFO,
    format=('%(asctime)s - %(levelname)s - %(message)s'),
    handlers=[
        logging.FileHandler("server_log.file")
    ]
    )
    assert name() == SERVER_NAME
    assert (int(rand()) >= 1) and (int(rand()) <= 10 )  
    main()