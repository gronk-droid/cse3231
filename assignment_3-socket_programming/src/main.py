import socket


HOST = '34.74.19.25'
PORT = 30315
email = 'gbutler2020@my.fit.edu'


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
        soc.connect((HOST, PORT))
        soc.sendall(email.encode())
        print('sent: ', email)
        data = soc.recv(1024)
        print('Received: '+data.decode())


main()
