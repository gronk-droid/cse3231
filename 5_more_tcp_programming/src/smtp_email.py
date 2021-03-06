import socket

SENDING_ADDRESS = 'gbutler2020@my.fit.edu'


def send_email(host, port, address, body):
    # the different sends
    # ehlo = 'EHLO gbutler2020'
    mail_from = 'MAIL FROM:<gbutler2020@my.fit.edu>\r\n'
    rcpt_to = f'RCPT TO:<{address}>\r\n'
    data = "DATA\r\n"
    message = f'{body}'
    quit = "QUIT\r\n"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))

        # ehlo send and recv
        # sock.send(ehlo.encode())
        resp = sock.recv(4096)
        print(repr(resp))

        # mail_from
        sock.send(mail_from.encode())

        # rcpt_to
        sock.send(rcpt_to.encode())

        # data
        sock.send(data.encode())

        # message
        sock.send(message.encode())

        # quit
        sock.send(quit.encode())
        resp = sock.recv(4096)
        print(repr(resp))


def main():
    host = '0.cloud.chals.io'
    port = 32907

    body = 'Subject: gbutler2020 - Assignment # 5\r\nFrom: gbutler2020@my.fit.edu\r\nTo: wallen@fit.edu\r\nContent-Type: text/html\r\n<h3>Hello,</h3><ul><li>I am <em>gbutler2020</em></li><li>This is my Assignment # 5</li><ul>\r\n.\r\n'

    address = 'wallen@fit.edu'
    # address = 'gbutler2020@my.fit.edu'

    send_email(host, port, address, body)


main()
