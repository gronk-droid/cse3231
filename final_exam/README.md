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

## Transport Layer
</div>

### <a id="tl1">UDP and TCP</a>
Differences:

<div class="leftColumn">

<div style="text-align: center;">

#### TCP (Transport Control Protocol)
</div>

Advantages
- Connection oriented transport
  - Sender must establish connection before transmission
  - Sender notified of delivery or of error
- <span class="textPink">Byte-stream</span> service
  - Data transmission and reception are similar to file I/O
- Reliable delivery
  - Garuntees packets are assembled <span class="textPink">in order</span>

Connection Management
- Connection
  - Three way connection increases probability that both endpoints know that connection was acccepted.
- Termination
  - Four way handshake requires two FIN and two ACK to complete. Ensures proper termination of connection occurs.

</div>

<div class="rightColumn">
<div style="text-align: center;">

#### UDP (User Datagram Protocol)
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

#### TCP Header Fields
|                     Field                      | <a id="sizeRet">[Size](#size)</a> (bits) |                                                                      Description                                                                      |
|:----------------------------------------------:|:---------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------:|
|                  Source Port                   |       16        |                                                   Identifies source port number (sender's TCP port)                                                   |
|                Destination Port                |       16        |                                                 Identifies destination port number (receiving port )                                                  |
|                Sequence Number                 |       32        |                                Used to number TCP segments. If SYN = 0, each byte is assigned a sequence number. <sup><a id="seqRet">[*](#seq)</a></sup>                                 |
|             Acknowledgement Number             |       32        |                                           Indicates next sequence number that sending device is expecting.                                            |
|             Offset (Header Length)             |        4        |                                  Shows number of 32 bit words in header. Minimum size of 5 words (`0101` in binary).                                  |
|                    Reserved                    |      4 (6)      |                                                                   Always set to 0.                                                                    |
| <a id="tcpflagsRet">[TCP Flags](#tcpflags)</a> |        8        |                                                        Flags are: URG, ACK, PSH, RST, SYN, FIN                                                        |
|                     Window                     |       16        | The size of the receive window, which is the number of bytes beyond sequence number in Acknowledgement field that the receiver is willing to receive. |
|                    Checksum                    |       16        |                                                      Used for error checking of header and data.                                                      |
|                 Urgent Pointer                 |       16        |                                    Shows the end of urgent data so interrupted data streams can be continued. <sup><a id="urgRet">[+](#urg)</a></sup>                                    |
|                  TCP Options                   |    variable     |        0 → End of Options List, 1 → No Operations (NOP, Pad), 2 → Maximum segment size, 3 → Window Scale, 4 → Selective ACK ok, 8 → Timestamp         |


<div class="footnote">
<sub>

- - -
<a id="size">[Size](#sizeRet)</a>: 4 bits → nibble, 8 bits → byte, 32 bits → word
<a id="seq">[Sequence Number](#seqRet)</a>: If SYN = 1, then this is the initial sequence number. The sequence number of the first byte of data will then be this number + 1. _i.e._: Let first byte of data have this be 300. Then if a packet has 10 bytes, then the next packet sent will have a sequence number of `300 + 10 + 1 = 311`.
<a id="urg">[Urgent Pointer](#urgRet)</a>: When URG is set, the data is given priority.
</sub>
</div>
<div style="page-break-after: always; break-after: page;"></div>

#### <a id="tcpflags">[TCP Flags Explained](#tcpflagsRet)</a>
| Flag |                                                                                         Description                                                                                         |
|:----:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| URG  |                                                                                       Urgent Pointer.                                                                                       |
| ACK  |                                                                                       Acknowledgement                                                                                       |
| PSH  |                                                 Push function. TCP allows an application to specify that data is to be pushed immediately.                                                  |
| RST  | Reset connection. Receiver must respond immediately terminating the connection. Transfer of data ceases, so data in transit is lost. Used for abnormal close of TCP connection, unlike FIN. |
| SYN  |                                                        Indicates synchronized sequence numbers. Source is beginning a new sequence.                                                         |
| FIN  |                                             Set when no more data is to come from sender. Used for good closing of TCP connection, unlike RST.                                              |



<div style="page-break-after: always; break-after: page;"></div>

### TCP Flow Control

TCP needs to control amount of data a sender transmits to avoid overwhelming the receiver.

<div style="text-align: center;">

##### Congestion Control vs Flow Control
</div>

<div class="leftColumn">

##### Congestion Control
- focuses on preventing too much data in <span class="textPink">network</span>.
- uses Retransmission Timeout (RTO) and Round Trip Time (RTT)
  - RTT is different for each path a packet takes.
- A router might only be able to handle 100 Mb/s total, but two senders could send more than that.
</div>

<div class="rightColumn">

##### Flow Control
- Tries to prevent senders from overrunning <span class="textPink">capacity of receivers</span>.
  - Can't prevent congestion at routers.
- Uses sliding window to control traffic in transit.
  - Uses <span class="textPink">AdvertisedWindow</span> to indicate how much data it can handle.
  - Measures in bytes, not packets.
  - Limits how many unacknowledged bytes can be in transit at a time.
  - TCP vs Data-Link Sliding Windows
    - Data-Link layer controls transmission of frames over links between adjacent nodes.
      - one sender at a time
      - always arrive in order sent (unless frames are lost)
    - TCP deals with end-to-end flow
      - each receiver can have multiple senders
      - each packet can follow a different path
  - Header uses these fields to manage flow control:
    - _<span class="textPink">SequenceNum</span>_
    - _<span class="textPink">Acknowledgement</span>_
    - _<span class="textPink">AdvertisedWindow</span>_
</div>

<div style="page-break-after: always; break-after: page;"></div>

#### TCP Congestion Control: Additive Increase and Multiplicative Decrease (AIMD)

TCP Source sets the CongestionWindow based on level of congestion it _perceives_ in the network.
- Involves <span class="textPink">decreasing</span> congestion window when congestion goes up and <span class="textGreen">increasing</span> the congestion window when level of congestion goes down.
- This is called _<span class="textPink">Additive Increase / Multiplicative Decrease</span>_ (AIMD).

<div class="leftColumn">

#### Additive Increase
- Every successful send from source that is a _CongestionWindow_'s worth of packets adds the equivalent of 1 to CongestionWindow.
  - Success is measured as one ACK per RTT.
- Increase is slower than decrease and avoids too rapid an increase in transmission rate.
</div>

<div class="rightColumn">

##### Multiplicative Decrease
- Easier to understand in terms of packets, despite <span class="textPink">CongestionWindow</span> being measured in bytes.
  - _e.g.:_
    - CongestionWindow is 16 packets
    - If a loss is detected, CongestionWindow is set to 8.
    - Additional losses go → 4, 2, 1.
</div>

##### Slow Start
1. Source starts _CongestionWindow_ at one packet.
2. Sends one packet.
2. ACK arrives → _CongestionWindow_ += 1.
3. Two packets are sent.
4. Two ACKs → _CongestionWindow_ += 2.

Trend: TCP effectively **doubles** every RTT.

1. **Slow Start** begins by doubling _CongestionWindow_ size.
2. When threshold is reached, switches to _additive increase_.
3. When packet is lost, _CongestionWindow_ goes to 1 and slow start repeats.

<div style="page-break-after: always; break-after: page;"></div>

#### TCP Timeout and RTT

##### Timeout
Timeout period must be long enough to allow longer paths. If a packet is lost, multiple packets can be sent out before timeout expires. Receiver can't ACK because missing packet caused a gap in _SequenceNum_. Sender can reach _CongestionWindow_ limit while waiting for timeout.

**Fast Retransmission and _Duplicate Acknowledgements_**
Receiver sends ACK for later packets, but with ACK number of last packet before lost packet--_i.e._ <span class="textPink">duplicate acknowledgements</span>.
- Tells sender that at least one packet hasn't arrived, but later ACK's indicate some later packets arrived.
- Duplicate ACK number tells sender which packet wasn't received.

Sender can _resend_ missing packet without waiting for timeout to expire. This is called _fast retransmission_ and can trigger transmission of lost packets sooner than regular timeout.
- Not triggered until _<span class="textPink">three duplicate ACK's</span>_ arrive.
- Sender knows packed was lost, and halves _slow start threshold_ and goes into slow start.

Fast Recovery
- Lost packed decreases _CongestionWindow_ to one and starts slow start.
- Fast retransmission signals congestion, and instead of lower _CongestionWindow_, fast recovery uses ACKs in transit to trigger sending of new packets.
- Removes slow start phase when fast retransmit detects lost packet.

<div style="page-break-after: always; break-after: page;"></div>

##### Round Trip Time (RTT)
Retransmission TimeOut (RTO) is based on <span class="textPink">Round Trip Time</span> (RTT) for a given connection.
- At connection, sender and receiver determine RTT and sender uses that for RTO.
- Sender calulates an average RTT to deal with delays.

Determining RTT:
- Sender and receiver both need RTT, so they put timestamps in options field to track send and receive times.
- A _Smoothed RTT_ (SRTT) is calculated based on the SRTT averaged over time and the most recent RTT.
<div class="center">

$SRTT = \alpha*SRTT + (1 - \alpha)RTT$ where $\alpha = 0.9$
</div>

- Smoothed RTT calculation was revised to include _variance_ in RTT.
  - **Variance** measures how much RTT changes over time.
<div class="center">

$VarRTT = \beta * VarRTT + (1 - \beta) * |SRTT - RTT|$ where $\beta = 0.75$
</div>

- Retransmission TimeOut (RTO) is calculated as follows:
<div class="center">

$RTO = SRTT + 4$<sup>++</sup> $*\ VarRTT$
</div>

<sub>++(multiplying by 4 is based on experimentation)</sub>

<div style="page-break-after: always; break-after: page;"></div>

#### IP Checksum
Header Checksum: 16 bits
- A checksum on the header only. Since some header fields change, it is _<span class="textPink">recomputed</span>_ and verified each time the header is processed.
- Algorithm:
  - 16 bit one's complement of the one's complement sum of all 16 bit words in the header. The value of the checksum field is zero.

IP Checksum Example:
1. break sequence into 16-bit words
2. Add 16-bit values. Each carry-out produced is added to the LSb.
3. Invert all bits to get one's complement.

Header to check:
<div class="center">

$$
\begin{aligned}
&1000\ 0110\ 0101\ 1110\\
&1010\ 1100\ 0110\ 0000\\
&0111\ 0001\ 0010\ 1010\\
&1000\ 0001\ 1011\ 0101\\
\end{aligned}
$$
</div>

<div style="page-break-after: always; break-after: page;"></div>

Add 16-bit values 2 at a time and convert to one's complement:
<div class="center">

$$
\begin{aligned}
&1000\ 0110\ 0101\ 1110 && first\ val\\
+\ &1010\ 1100\ 0110\ 0000 && second\ val\\
\overline{\ \ }&\overline{\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ }\\
1\ &0011\ 0010\ 1011\ 1110 && carry-out\\
+\ &0000\ 0000\ 0000\ 0001 && add\ to\ LSb\\
\overline{\ \ }&\overline{\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ }\\
&0011\ 0010\ 11011\ 1111\\
+\ &0111\ 0001\ 0010\ 1010 && third\ val\\
\overline{\ \ }&\overline{\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ }\\
0\ &1010\ 0011\ 1110\ 1001 && no\ carry-out\\
+\ &1000\ 0001\ 1011\ 0101 && fourth val\\
\overline{\ \ }&\overline{\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ }\\
1\ &0010\ 0101\ 1001\ 1110 && carry-out\\
+\ &0000\ 0000\ 0000\ 0001 && add\ to\ LSb\\
\overline{\ \ }&\overline{\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ }\\
&0010\ 0101\ 1001\ 1111 && one's\ complement\ sum\\
&&& flip\ bits\\
&1101\ 1010\ 0110\ 0000 && one's\ complement\\
\end{aligned}
$$
</div>

Thus, the 16 bit checksum is `1101 1010 0110 0000`.

<div style="page-break-after: always; break-after: page;"></div>

## Applications
