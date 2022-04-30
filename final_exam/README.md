<div class="title-page">

# CSE3231 Final Exam Study Guide
### Grant Butler, Tyler Zars
#### gbutler2020@my.fit.edu | tzars2019@my.fit.edu
</div>
<div style="page-break-after: always; break-after: page;"></div>


<!---
Table Of Contents
--->
<div class="center">

# Table of Contents
</div>

<a id="tableRet">Sections</a>

[Transport Layer](#tl1)


<div style="page-break-after: always; break-after: page;"></div>

<div style="text-align: center;">

### Transport Layer
</div>

#### <a id="tl1">UDP and TCP</a>
Differences:

<div class="leftColumn">

<div style="text-align: center;">

##### TCP (Transport Control Protocol)
</div>

Advantages
- Connection oriented transport
  - Sender must establish connection before transmission
  - Sender notified of delivery or of error
- <span class="textPink">Byte-stream</span> service
  - Data transmission and reception are similar to file I/O
- Reliable delivery
  - Garuntees packets are assembled <span class="textPink">in order</span>

</div>

<div class="rightColumn">
<div style="text-align: center;">

##### UDP (User Datagram Protocol)
</div>

- Connectionless
  - Destination address and port number are added to transport segment's header and the segment is sent to the destination.
  - No confirmation of error or delivery (ACK) is returned.
    - Unreliable because of no ACK
- Advantages
  - Applications pass **<span class="textPink">directly</span>** to transport layer.
  - Data is transmitted _<span class="textPink">immediately</span>_. Will either reach the receiver or not at all.
  - Less to manage:
    - No _<span class="textPink">congestion-control</span>_ or retransmission mechanisms.
    - No Connection Establishment
    - No connection state
    - Results in small packet header
  - Messages can be sent in <span class="textPink">broadcast</span> or <span class="textPink">multicast</span> mode.
    - one to multiple receivers (multicast) or all nodes (broadcast)

</div>

<div style="page-break-after: always; break-after: page;"></div>

##### TCP Header Fields
|                     Field                      | Size[^1] (bits) |                                                                      Description                                                                      |
|:----------------------------------------------:|:---------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------:|
|                  Source Port                   |       16        |                                                   Identifies source port number (sender's TCP port)                                                   |
|                Destination Port                |       16        |                                                 Identifies destination port number (receiving port )                                                  |
|                Sequence Number                 |       32        |                                Used to number TCP segments. If SYN = 0, each byte is assigned a sequence number. [^2]                                 |
|             Acknowledgement Number             |       32        |                                           Indicates next sequence number that sending device is expecting.                                            |
|             Offset (Header Length)             |        4        |                                  Shows number of 32 bit words in header. Minimum size of 5 words (`0101` in binary).                                  |
|                    Reserved                    |      4 (6)      |                                                                   Always set to 0.                                                                    |
| <a id="tcpflagsRet">[TCP Flags](#tcpflags)</a> |        8        |                                                        Flags are: URG, ACK, PSH, RST, SYN, FIN                                                        |
|                     Window                     |       16        | The size of the receive window, which is the number of bytes beyond sequence number in Acknowledgement field that the receiver is willing to receive. |
|                    Checksum                    |       16        |                                                      Used for error checking of header and data.                                                      |
|                 Urgent Pointer                 |       16        |                                    Shows the end of urgent data so interrupted data streams can be continued. [^3]                                    |
|                  TCP Options                   |    variable     |        0 → End of Options List, 1 → No Operations (NOP, Pad), 2 → Maximum segment size, 3 → Window Scale, 4 → Selective ACK ok, 8 → Timestamp         |

##### <a id="tcpflags">[TCP Flags Explained](#tcpflagsRet)</a>
| Flag |                                                                                         Description                                                                                         |
|:----:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| URG  |                                                                                       Urgent Pointer.                                                                                       |
| ACK  |                                                                                       Acknowledgement                                                                                       |
| PSH  |                                                 Push function. TCP allows an application to specify that data is to be pushed immediately.                                                  |
| RST  | Reset connection. Receiver must respond immediately terminating the connection. Transfer of data ceases, so data in transit is lost. Used for abnormal close of TCP connection, unlike FIN. | 
| SYN  |                                                        Indicates synchronized sequence numbers. Source is beginning a new sequence.                                                         |
| FIN  |                                             Set when no more data is to come from sender. Used for good closing of TCP connection, unlike RST.                                              |

[^1]: 4 bits → nibble, 8 bits → byte, 32 bits → word
[^2]: If SYN = 1, then this is the initial sequence number. The sequence number of the first byte of data will then be this number + 1. _i.e._: Let first byte of data have this be 300. Then if a packet has 10 bytes, then the next packet sent will have a sequence number of `300 + 10 + 1 = 311`.
[^3]: When URG is set, the data is given priority.

<div style="page-break-after: always; break-after: page;"></div>

