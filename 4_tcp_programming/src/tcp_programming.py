import socket
import re


def get_html(host, port, page):
    request = f'GET {page} HTTP/1.1\r\n{host}\r\n\r\n'

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

    main_page = '/'
    main_html = get_html(host, port, main_page)
    print(host + main_page)
    print(main_html, end='\n\n')  # part 1 done

    # now to parse the other link
    link_regex = re.compile(r'HREF="(?:[^"]|"")*"')  # regex for the href
    href_str = link_regex.search(main_html).group()  # getting the link

    # substring magic
    sub_page = f'{href_str[7:-1]}'
    sub_html = get_html(host, port, sub_page)
    print(host + sub_page)
    print(sub_html, end='\n\n')  # part 2 done


main()
