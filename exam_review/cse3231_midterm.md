-   What is the purpose of framing at the Data Link layer?

    -   It provides a way for a sender to transmit a set of bits that
        are meaningful to the receiver.

-   Explain the differences between the Stop-and-Wait protocol and the
    Sliding Window protocol at the Data Link layer

    -   **Stop and Wait** is the fundamental technique to provide
        reliable transfer under unreliable packet delivery system. After
        transmitting one packet, the sender waits for an acknowledgment
        (ACK) from the receiver before transmitting the next one.

    -   The main goal of the **Sliding Window** is to increase link
        utilization, we can send a group of frames and then wait for
        acknowledgement of those frames before we send additional frames

        -   However, we need to keep track of how many frames were sent
            and how many frames were acknowledged before we can continue
            transmitting

        -   The current group of frames is referred to as a "window" and
            it "slides" from one group to another as frames are received
            and ACK'd

        ```{=html}
        <!-- -->
        ```
        -   The sending node maintains a window of frames that it can
            send

            -   It must buffer them for possible re-transmission

            -   Window advances when acknowledgements are received, and
                new frames can be sent

        -   The receiving node maintains a window of frames that it can
            receive

            -   If a frame is lost, the receiver holds any newer frames
                in a buffer until lost frame is received

            -   Checks for errors before sending ACK

            -   Window advances with valid in-order arrivals

    -   Therefore, the main differences come down to how the data is
        sent/acknowledged. The Sliding Window approach will send frames
        even if there is no ACK; meanwhile Stop and Wait will not send
        any data until an ACK is received.

-   Explain the \"hidden node\" problem for wireless links and how IEEE
    802.11 solves it

    -   Problem

        -   There is one device between the middle of two Access Points,
            both APs try to send a packet but the device can only listen
            to one at a time hence a collision occurs. The two APs are
            not in range of one another. ![Diagram Description
            automatically
            generated](media/image1.png){width="2.3928576115485565in"
            height="1.586035651793526in"}

    -   Solution

        -   The exposed terminal problem is solved by the MAC (medium
            access control) layer protocol IEEE 802.11 RTS/CTS, with the
            condition that the stations are synchronized, and frame
            sizes and data speed are the same. RTS stands for Request to
            Send, and CTS stands for Clear to Send.

        -   A transmitting station sends a RTS frame to the receiving
            station. The receiving station replies by sending a CTS
            frame. On receipt of CTS frame, the transmitting station
            begins transmission.

        -   Any station hearing the RTS is close to the transmitting
            station and remains silent long enough for the CTS. Any
            station hearing the CTS is close to the receiving station
            and remains silent during the data transmission.

        -   In the above example, station STC hears does not hear RTS
            from station STA but hears CTS frame from station STB. So,
            it understands that STB is busy defers its transmission thus
            avoiding collision.

-   Explain the difference between virtual circuit switching and the
    Datagram, or connectionless, approach

    -   ![Table Description automatically
        generated](media/image2.png){width="4.896409667541557in"
        height="2.8928576115485565in"}

    -   Overall: Datagram needs more resources during runtime. VC
        Network needs more infrastructure to run, but is quicker and
        more reliable in the long run.

-   Describe how fragmentation is used to deal with different Maximum
    Transmission Unit (MTU) sizes

    -   If a packet is over the size limit of an MTU, it will be
        fragmented into pieces to fit through the MTU. Once it has been
        fragmented, it is not put together until it reaches its
        destination. The packet is fragmented which adds new information
        to allow the packet to be reassembled correctly. This
        information is the ident, offset and MF (more fragments) flag.
        The ident is the same for all packets in the fragmentation, the
        offset lets you know where this fits in the offset since the
        start in 8-byte blocks, and the MF flag alerts you to more
        fragments coming down the link (0 if none, 1 if more).

-   Describe the benefits and limitations of a best-effort,
    connectionless network model (IP) and be familiar with the format
    and fields in an IP packet header

    -   IP uses connectionless for data, best effort for delivery

    -   Pros

        -   Hosts can transmit packets without delay since no connection
            is needed before sending data

        -   Each packet is forwarded independently of previous packets
            that have been sent to the same destination. (Allows 2
            packets to go two different routes)

        -   A switch or link failure might not result in a lost packet
            because it may be possible to find an alternate route around
            the failure - routers will be updated frequently

    -   Cons

        -   However, when a host sends a packet, it has no way of
            knowing if the network can deliver it, how long it will take
            or if the destination host is even up and running

    -   Header Fields and Format

1.  Version (4 bits): most often v4

2.  Hlen (4 bits): number of 32-bit words in the header

3.  TOS (8 bits): type of service (not widely used)

4.  Length (16 bits): number of bytes in this datagram

5.  Ident (16 bits) and Flags/Offset (16 bits): supports fragmentation

6.  TTL (8 bits): number of hops this datagram has traveled

7.  Protocol (8 bits): demultiplex key (TCP=6, UDP=17)

8.  Checksum (16 bits): (header only)

9.  SrcAddr, DestAddr (32 bits each)

-   Describe the IP address format, including classes and subnets, and
    be able to explain the differences between the standard classes (A,
    B, C) and Classless Inter-Domain Routing (CIDR)

    -   Format

        -   192.168.1.12/24 --\> class C (/24) --\> first 24 bits in are
            the same

    -   Standard Classes

        -   always loses 255.255.255.255 and 0.0.0.0 because they are
            reserved

        -   Class A (8 bit): leading bit = 0

            -   total of \~120 networks

            -   16,777,214 (2\^24 -- 2) hosts per network (255.0.0.0)
                (0.0.0.0)

        -   Class B (16 bit): leading bits = 10

            -   total of \~16,000 networks

            -   65,534 (2\^16 -- 2) hosts per network (255.255.0.0)
                (0.0.0.0)

        -   Class C (24 bit): leading bits = 110

            -   can be \~2 million networks

            -   254 (2\^8 -- 2) hosts per network

    -   Classless Inter-Domain Routing (CIDR)

        -   Uses a **single entry** in forwarding table

        -   i.e.:

            -   ISP with 16 class C network numbers

                -   use *contiguous* class C addresses

            -   Assign network 192.4.16.x to 192.4.31.x

            -   First 20 bits of all addresses are the same

                -   Between class B (16 bit) and C (24 bit)

            -   Allows ISP to allocate any size of **common prefix**.

-   Explain the purpose of the Address Resolution Protocol (ARP), the
    Dynamic Host Configuration Protocol (DHCP) and the Internet Control
    Message Protocol (ICMP)

    -   ARP (Address Resolution Protocol) requests the MAC (Ethernet)
        address for a specific IP address \[IP $\rightarrow$ ARP → MAC\]

    -   DHCP

        -   A DHCP server is responsible for automatically providing
            configuration information to hosts

        -   There is normally at least one DHCP server for an
            administrative domain (IP network)

        -   The DHCP server maintains a pool of available IP addresses

        -   DHCP allows for a device to request an address from the
            server, and the server will send back the IP address that
            the device can use. It works on a lease system, and it will
            expire after so long. The DHCP address is mapped to the
            device MAC address via ARP.

    -   ICMP - A network-layer protocol that provides a variety of error
        messages that are sent back to the source host whenever a router
        or host is unable to process an IP datagram successfully. Used
        to tell if data is reaching somewhere in a timely manner.

        -   ![](media/image3.png){width="2.5625in"
            height="1.313280839895013in"}

-   Explain how congestion can occur in the Internet and how the
    Internet Protocol reduces congestion (Slide Deck
    Network-Layer-Part-3)

    -   Congestion results when too much traffic is entered into the
        network

    -   Traffic-aware routing (Slower)

        -   Choose routes depending on the volume of traffic, not just
            on the network topology

    -   Admission control (Middle)

        -   Virtual Circuits can use admission control to only add new
            traffic if the network has enough capacity

    -   Traffic throttling (Fast)

        -   Congested routers can signal hosts to slow the rate of
            transmission of traffic

    -   Load shedding (Fastest)

        -   Another method is for routers to drop packets (shedding
            traffic load) to reduce congestion

-   Explain the difference between distance vector routing and link
    state routing

    -   Distance Vector Routing

        -   It is a dynamic routing algorithm in which each router
            computes a distance between itself and each possible
            destination i.e. its immediate neighbors.

        -   The router shares its knowledge about the whole network to
            its neighbors and accordingly updates the table based on its
            neighbors.

        -   The sharing of information with the neighbors takes place at
            regular intervals.

        -   It makes use of **Bellman-Ford Algorithm** for making
            routing tables.

        -   **Problems**

            -   Count to infinity problem which can be solved by
                splitting horizon. 

            -   Good news spread fast and bad news spread slowly. 

            -   Persistent looping problem i.e. loop will be there
                forever.

    -   Link State Routing

        -   It is a dynamic routing algorithm in which each router
            shares knowledge of its neighbors with every other router in
            the network.

        -   A router sends its information about its neighbors only to
            all the routers through flooding.

        -   Information sharing takes place only whenever there is a
            change.

        -   It makes use of **Dijkstra's Algorithm** for making routing
            tables.

        -   **Problems**

            -   Heavy traffic due to flooding of packets. 

            -   Flooding can result in infinite looping which can be
                solved by using the **Time to live (TTL)** field. 

    -   ![Text Description automatically generated with medium
        confidence](media/image4.png){width="2.722995406824147in"
        height="2.1440682414698164in"}

-   Explain how Network Address Translation allows multiple nodes within
    a LAN to share one Internet facing IP address when interacting with
    computers outside the LAN

    -   NAT (Network Address Translation) works by taking one public IP
        and making a new class of private IPs only accessible within the
        local network. The router provides a set of IPs for the internal
        network, normally stemming from 192.168/172.16. Each computer
        gets an address from the router, and it is mapped to the public
        IP by specifying a port internally and a port externally.

-   Explain the DNS name resolution process that allows a node in one
    network to get the IP address associated with the hostname of a
    computer in another network

    -   Domain Name Service

    -   A name space defines the set of possible names

        -   A name space can be either flat (names are not divisible),
            or it can be hierarchical (with ways to group names)

    -   The DNS naming system maintains a collection of bindings of
        names to values

        -   the term name refers to the text name of the resource

        -   the value can be anything, but in this case, it is an IP
            address

    -   A resolution mechanism is a procedure that, when\
        given a name, returns the corresponding value

        -   A name server is a resolution mechanism that is available on
            a network and that can be queried by sending it a message

    -   Works via a Domain Hierarchy

        -   Root Name Server -\> .com ending server (.edu, .gov, etc)
            -\> Specific Site -\> Subdomains -\> Return IP to the
            computer asking

        -   Caching the IP mapping is done in case there is another
            lookup soon after.
