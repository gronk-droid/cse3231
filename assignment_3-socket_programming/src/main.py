import socket
HOST = '34.74.19.25'
PORT = 30315
SERVER_ADDR = (HOST, PORT)
email = 'gbutler2020@my.fit.edu'


def main():
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soc.sendto(email.encode(), SERVER_ADDR)
    print('sent: ', email)
    data = soc.recvfrom(1024)
    print('received: '+data[0].decode())


main()
