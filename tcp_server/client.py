import socket
import sys
import logging

if __name__ == '__main__':
    logging.basicConfig(
        format="%(asctime)s [PID:%(process)d] %(levelname)s: %(message)s",
        level=logging.DEBUG,
        datefmt='%d-%b-%y %H:%M:%S')

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5422)
    sock.connect(server_address)
    logging.info(f"Established connection")

    while True:
        try:
            data = sock.recv(9)
            logging.info(f"Got Data {str(data)}")
        except KeyboardInterrupt:
            break

    sock.close()
