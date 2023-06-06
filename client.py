import sys
import socket
import logging

def kirim_data():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.basicConfig(format='%(message)s', level=logging.WARNING)
    server_address = ('0.0.0.0', 45000)
    logging.warning(f"[CLIENT]::OPENING_SOCKET...\t \"{server_address[0]}:{server_address[1]}\"")
    sock.connect(server_address)

    try:
        # Send data
        message = 'TIME' + chr(13) + chr(10)
        logging.warning(f"[CLIENT]::SENDING...\t\t \"{message[:-2]}\"")
        sock.sendall(message.encode())
        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            logging.warning(f"[SERVER]::RECEIVED...\t\t \"{data}\"")
    finally:
        logging.warning("[CLIENT]::CLOSING_SOCKET...")
        logging.warning("================================================")
        sock.close()
    return

if __name__=='__main__':
    for i in range(1,10):
        kirim_data()
