### CSE3231: Computer Networks
###### **Assignment #3:** Socket Programming
Grant Butler | [gbutler2020@my.fit.edu](mailto:gbutler2020@my.fit.edu)
- - -
The purpose of this assignment was to write a program that sends a UDP packet to a server and receives a reply. I wrote the program in Python, as that was the easiest to set up.

###### Code:
`main.py`:
```python
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

```
</br>

`terminal output`:
```

```
