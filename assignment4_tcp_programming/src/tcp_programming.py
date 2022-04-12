import socket
import re


def get_html(host, port):
    request = f'GET / HTTP/1.1\r\n{host}\r\n\r\n'

    # open the socket as TCP → SOCK_STREAM since TCP connects a data stream
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))  # connect to the server
        sock.send(request.encode())  # send the request to the server
        response = sock.recv(4096)  # get response from server
        html = repr(response)  # get html doc text from response data

    return html


def main():
    host = '0.cloud.chals.io'
    port = 23456

    original_html = get_html(host, port)
    print('part 1\n' + original_html + '\n\n')  # part 1 done

    # now to parse the other link
    link_regex = re.compile(r'HREF="(?:[^"]|"")*"')  # regex for the href
    href_str = link_regex.search(original_html).group()  # getting the string

    embedded_link = f'{host}{str(href_str)[7:-1]}'  # pronto!
    new_html = get_html(str(embedded_link), port)
    print('part 2 ' + new_html)


main()
