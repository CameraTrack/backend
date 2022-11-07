import socket
import logging
import random
import time
import sys

VEHICLE_PLATES = [
    "C777BA775","C567XC707","C551BM946","T928XP088","Y042BH750",
    "C565EA700","T446MC332","E592AH349","Y831KH352","C853YY289",
    "P688MB550","X396OE441","A723EX283","X18YT756","O345CM482"]

if __name__ == '__main__':
    logging.basicConfig(
        format="%(asctime)s [PID:%(process)d] %(levelname)s: %(message)s",
        level=logging.DEBUG,
        datefmt='%d-%b-%y %H:%M:%S')

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5422)
    sock.bind(server_address)
    sock.listen(5)

    while True:
        client, address = sock.accept()
        logging.info(f"Connection established: {address[0]}:{address[1]}")
        while True:
            try:
                number = random.choice(VEHICLE_PLATES)
                logging.info(f"Sending '{number}' number")
                client.send(bytes(number, 'utf-8'))
                time.sleep(5)
            except KeyboardInterrupt:
                break
            except BrokenPipeError:
                client.close()
                break

        client.close()
