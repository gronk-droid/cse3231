import socket
HOST = '34.74.19.25'
PORT = 30315
email = 'gbutler2020@my.fit.edu'


def main():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect((HOST, PORT))
    soc.sendto(email.encode(), (HOST, PORT))
    print('sent: ', email)
    data = soc.recv(1024)
    print('Received: '+data[0].decode())


main()
