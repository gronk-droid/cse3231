import socket

SENDING_ADDRESS = 'gbutler2020@my.fit.edu'


def send_email(host, port, address, body):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        


def main():
    host = '0.cloud.chals.io'
    port = 32907


main()
