# Wireless Communication System using WiFi
Made by @Fernando_Cortez, @Felix_Quevedo, and @Luis_Serrano

Subject: **Computer Network**

Professor: **Dr. Moises Sanchez Adame**

University: **CETYS University, Tijuana.**

#### Abstract
In the following document, it is explained how WiFi as a wireless communication system works and the way on how it was implemented between two wireless devices.

## Objective
Establish a wireless communication using WiFi between a transmitter and a receptor to control a process.

## Theoretical Framework

### Architecture
#### Types
- **Infrastructure**
The infrastructure is made by any device that can communicate with a work station through a wireless Local Area Network (LAN) or WiFi, this can only be done with an access point.

- **Ad hoc Network**
Any obstacle there can be between work stations that are linked together are referred as ad hocs.

- **Mixed Network**
A mixed network is developed when an infrastructure and an ad hoc network are combined, working simultaneously within.

#### Components
To create a network, components are needed, these are:
- **Access Point**
A type of routing device that can transmit and receive data using wireless networking. This devices have a limit of devices that can have access to the network.

- **Clients**
Devices that want to communicate with others and that can connect with an AP via the AP network.

- **Bridge**
A connector used to esblish a connection between wired networks and wireless networks.

![WiFi Communication Between Two Raspberry](https://github.com/LuisS96/Redes_de_Computadoras/blob/feature/WiFi/Proyects/WirelessCommunicationSystems/WiFi/WiFi_RaspberryPi.png)

### Protocols
- **IP address (Internet Protocol address).**
Sets a direction for packets to be delivered from the source host to the destination host. The packets are encapsulated for the data to be delivered. It first started as a connectionless datagram service now named User Datagram Protocol(UDP), now it is a connection-oriented Transmission Control Protocol (TCP).

The version used is IPv4 represented in the dot-decimal notation with a 32-bit integer value, IPv4 has runned out making of its successor IPv6 using 128-bit address represented as eight groups of four hexadecimal digits, providing approximately 4.3 billion addresses, 7.9 x 10^28 times as many as IPv4.

- **TCP (Transmission Control Protocol)**
Provides a reliable communication through a connection-oriented service between the server and the client, also known as a host-to-host connectivity at the transport layer of the TCP/IP model. This layer checks for data errors and provides the mechanisms to request retransmission of the lost data, therefore it guarantees that all the data received is correct and in order by keeping track of the 'segments'.

TCP is mainly used when using the internet such as the World Wide Web (WWW), File Transfer Protocol (FTP), Secure Shell, etc.

- **DHCP (Dynamic Host Configuration Protocol)**
Provides the Access Point's clients with IP addresses to be able to communicate with other hosts. 

- **IEEE 802.11**
A set of Media Access Control (MAC) and Physical Layer (PHY) specifications for implementing a WLAN communication in the 900 MHz and 2.4, 5, and 60 GHz frequency bands. These are widely used to allow devices to talk with each other and access the internet without being wired.
  - **Othogonal Frequency-Division Multiplexing (OFDM)**
  Method of encoding digital data on multiple carrier frequencies.
  
![802.11g Bandwidth channels](https://github.com/LuisS96/Redes_de_Computadoras/blob/feature/WiFi/Proyects/WirelessCommunicationSystems/WiFi/80211g_bandwidth.png)


### Physical Layer
The Physical layer defines the specifications for devices. It defines the relationship between a device and a transmission medium.

The PHY layer functions and services are:
- Establishment and termination of a connection to a medium.
- Participation in the process where the communication resources are effectively shared.
- Modulation or conversion between the representation of digital data in user equipment and the signals transmitted over a channel.

#### Sublayers
- **The Physical Layer Convergence Procedure (PLCP)** acts as an adaptation later.

- **The Clear Channel Assessment (CCA)** mode and building packets for different PHY technologies in which the PLCP is responsible for.

- **The Physical Medium Dependent (PMD)** specifies modulation and coding techniques. The PHY management layer takes care of the management issues.

The station management sub layer is responsible for co-odination of interaction between the Data Link Layer (DLL) and the PHY layers.

### MAC Sublayer Protocol
The MAC sub-layer provides the functional and procedural means to transfer data between network clients to detect errors that may occur on the physical layer, and possibly correct them. 

It also provides access to contention based and contention free traffic on different kinds of physical layers. The responsiblities in this layer are divided into:

- **MAC sub-layer**
Defines access mechanisms and packets formats

- **MAC management sub-layer**
Defines power management, security and roaming services.

### Frame Structure


## Equipment and Material
- **Raspberry Pi 3 Model B+ (2 units).** 
The Raspberry Pi 3 Model B+ have an integrated WiFi Module.

## Development
### Software
#### Access Point
A Raspberry Pi was set up as an Access Point in a standalone network (NAT) to develop the task. To set up the Raspberry Pi, the following instructions where made.

The Raspberry Pi nees to be up-to-date.
```
sudo apt-get update
sudo apt-get upgrade
```

`dnsmasq` is needed to configure the Raspberry Pi as a DHCP server and `hostapd` as the Access Point host. Both need to be downloaded and installed.
```
sudo apt-get install dnsmasq hostapd
```
When a file needs to be edited, add the following commands before the path of the file `sudo nano`.

Yet, a standalone network needs to be configured for the Raspberry Pi to act as a server, it needs to have a static IP Address.

The dhcpcd file needs to be configured with the static IP Address `/etc/dhcpcd.conf` and at the end of the file edit it with the following:
```
interface wlan0
  static ip_address=192.168.1.1/24
  nohook wpa_supplicant # Not to be run when the Raspberry Pi is initialized
```

The interface `wlan0` is usually used when using the Raspberry Pi module, if a USB dongle is used it would be `wlan1`.

The DHCP server, provided by dnsmasq has to be configured.
```
interface wlan0 # Interface in use
  dhcp-range=1192.168.1.2,192.168.1.10,255.255.255.0,24h
```
A range of IP addresses is configured that intended to be provided, it could go up to `10.0.0.254`, the netmask is also set according to our network class and a lease time of 24 hours (optional).

The Access point need to be configured through a new file `/etc/hostapd/hostapd.conf`.

Inside the file, the following information:
```
interface=wlan0
driver=nl80211 #The Raspberry's module driver
ssid=NameOfNetwork
hw_mode=g #Used 802.11g 2.4GHz band
channel=11 #Channel to use
wmm_enabled=0 #QoS support
macaddr_acl=0 #Controls MAC address filtering
auth_algs=1 #1=wpa 2=wep 3=both
wpa=2 #WPA2 only
wpa_passphrase=NetworkPassword
wpa_key_mgmt=WPA-PSK
```

Now, the Raspberry Pi needs to run this file when initialized at boot, the file `/etc/default/hostapd` needs to be configured where the line `#DAEMON_CONF` needs to be replaced by `DAEMON_CONF=/etc/hostapd/hostapd.conf`.

The Raspberry Pi is almost done, however a routing and masquerade need to be added.

By uncommenting the line `net.ipv4.ip_forward=1` at the file `/etc/sysctl.conf`, packets are accpeted to be forwared.

Later, a masquerade for outbound traffic if using `eth0`:
```
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
```

The iptables rule need to be saved `sudo sh -c "iptables-save > /etc/iptables.ipv4.nat"`, and for them to be configured every time when booting, at the file `/etc/rc.local` above "exit 0" the next line needs to be added `iptables-restore < /etc/iptables.ipv4.nat`.

Now we can reboot our Raspberry Pi which will act as an Access Point with the SSID and Passphrase created.

### Comunication
Two Raspberry Pis were used to be able to establish the communication, one as the server and the other as the client. As a team we decided to make it happen through TCP (Transmission Control Protocol) where the client and the server communicates between both as to UDP (User Datagram Protocol) which only the client does.

![Python version](https://img.shields.io/badge/python-v2.7-brightgreen.svg)

The following codeswhre made to establish this communication.

#### Server Code
```
import socket

TCP_IP = '10.0.0.1' #IP Address of the server
TCP_PORT = 5005 #Port used
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creates TCP socket
s.bind((TCP_IP, TCP_PORT)) #Associate the socket with the server address
s.listen(1) #Listens for incoming connections

connection, client_address = s.accept() #Opens connection with the client

while 1:
    data_recv = connection.recv(BUFFER_SIZE) #Data is read from the connection 
    data = "Acknowledge of data received"
    if not data_recv: break
    print data_recv
    connection.send(data) #Transmits data to client
connection.close() #When finished, connection with the client is closed
```

#### Client Code
```
import socket

TCP_IP = '192.168.1.1' #IP Address of the server
TCP_PORT = 5005 #Port used
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creates TCP socket
s.connect((TCP_IP, TCP_PORT)) #Attaches the socket with the server address
while 1:
	  data = "data"
	  s.send(data) #Sends data to the client
	  data_recv = s.recv(BUFFER_SIZE) #Receives data from the client
	  print data_recv
s.close() #Closes the connection through the socket
```

## Results and Analysis


## Conclusions


## References
https://public.cnrood.com/public/docs/WiFi_Physical_Layer_and_Transm_Meas.pdf
