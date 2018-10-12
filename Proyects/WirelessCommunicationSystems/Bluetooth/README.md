# Wireless Communication System using Bluetooth

Made by @Fernando_Cortez, @Felix_Quevedo, and @Luis_Serrano

Subject: **Computer Network**

Professor: **Dr. Moises Sanchez Adame**

University: **CETYS University, Tijuana**

#### Abstract
In the following document, the basics of Bluetooth technology will be explained and implemented between two devices. The architecture and frame structure will be presented and some cde will be written in order to trasnmit a simple string.

## Objective
Establish a wireless communication using Bluetooth between a transmitter and a receptor to control a process.

## Theoretical Framework

### Architecture
In order to create a Bluetooth system, the connection between a Master an a Slave device must be stablished. The moment this first connection is verified by the two devices, a piconect is created. 

![Bluetooth System](https://raw.githubusercontent.com/LuisS96/Redes_de_Computadoras/feature/Bluetooth/Proyects/WirelessCommunicationSystems/Bluetooth/Bluetooth_Net.png)

The piconet is the most basic network in a Bluetooth system, it can contain a single master and up to seven slaves. Furthermore, the a collection of piconets interconnectd by slaves is called a scatternet. It is important to mention that the maximum amount of nodes in a Bluetooth net is 255. 

The master and slave design allows the manufacturers to produce low-cost Bluetooth chips. The main disadvantage of this design is that the slaves are only capable of doing what a master tells them to.

It is important to mention that communication only occurs between a master and a slave, or a master and a master; no slave to slave communication is possible. 

### Protocols
- #### RFCOMM
Radio Frequency Communication (RFCOMM) is a set of transport protocols that provides emulation of serial ports `RS-232` over the L2CAP protocol, which establishes a Bluetooth communication. It supports up to 60 simultaneous connections between two bluetooth devices.

It exists two different types of devices:
- **Type 1**: end points like computers, smartphones, speakers, and many others.
- **Type 2**: part of the communication segment like modems, AP, etc.

There are no entities defined, therefore devices type 2 can communicate with devices of the same type.

- #### Bluetooth Protocol Stack
The BLuetooth Protocol Stack architecture can be grouped in three main layers: the physical layer, the datalink layer, and the upper layer. The following image shows how the diferent layers interact with each other:

![Bluetooth Architecture](https://raw.githubusercontent.com/LuisS96/Redes_de_Computadoras/feature/Bluetooth/Proyects/WirelessCommunicationSystems/Bluetooth/Bluetooth_Architecture.png)

### Physical Layer 
The bottom layer of the architecture (the physical radio layer), is the responsible for the correct radio transmission and modulation. It is te equivalent of the physical layer in the OSI and 802 models. It moves the data bits between the master and the slave. 

This layer uses a low-power system with a range of 10 meters and a 2.4 GHz band, this band is divided in 79 channels, each using 1 MHz. A process called adaptive frequency hopping is implemented with the porpuse of reducing interference from and to other RF signals; this is because early versions of Bluetooth used to collide their information with the data transmitted with 802.11 technology.

### Link Layers
In the Bluetooth architecture, the link control (baseband) layer is the one in charge to turn the raw bit stream into a frame and define some key formats. This layer is the equivalent of a MAC sublayer in a 802.11 architecture.

A key feature of this layer is that it creates a time division multiplexing, where the master defines a series of time slots and it transmits in the even slots, in contrast the slave transmits in the odd ones. Once the time slots are defined, the frames can be transmitted. These frames can be 1, 3, or 5 slots long; besides, the payload of the frame can be encrypted with a key which is selected when the connection between master and slave is created.

The link manager protocol creates link between master and slave, these are sets of logical channels that carry frames. When these links are created, a pairing procedure starts. The secure simple pairing method allows users to confirm that both devices are displaying the same PIN. This method uses a system generated PIN, which is safer than a user generated one.

After the pairing is complete, the link manager protocol will set the links; however, two main kinds of link can be established: Synchronous Connection Oriented (SCO), and Asynchronous ConnectionLess (ACL). As the name implies, a SCO link is used for real-time data transmission; here, frames are never retransmitted and forward error correction is used. In contrast, an ACL link manages packet-switched data which is available at irregular intervals. It is important to mention that a slave can only have a single ACL link to its master.

### Frame Structure
The frame format that Bluetooth technology uses can be separated in two forms: the basic rate data format, and the enhanced rate data format. Both forms star with an access code that identifies each master entity, followed by a header. The number of bits that each segment covers is depicted in the next image.

![Bluetooth Data Frame Rates](https://raw.githubusercontent.com/LuisS96/Redes_de_Computadoras/feature/Bluetooth/Proyects/WirelessCommunicationSystems/Bluetooth/Bluetooth_DataFrame.png)

If the frame is sent at a basic data rate, the rest of the frame is dedicated to the data package. It can carry up to 2744 bits for a five slot transmission. However, if the data is sent at an enhanced rate, the next 16 bits are use as a guard field and a synchronization pattern to switch into the faster data rate, which can carry two or three symbols per bit, allowing up to 8184 bits of data. This enhanced-frame ends with a two bit trailer.

#### Bluetooth Network Encapsulation Protocol (BNEP)
![BNEP Frame Structure](https://raw.githubusercontent.com/LuisS96/Redes_de_Computadoras/feature/Bluetooth/Proyects/WirelessCommunicationSystems/Bluetooth/Bluetooth_Frame_Format.png)

The contents of the frame and their respective names and number of bits are descrived below. This is exclusivo for the basic data rate frame.

- Access Code (72 bits): used for timing synchronization, offset, paging, and inquiry
- Header (54 bits)
  - Addr (3 bits): Temporary address assigned
  - Type (4 bits): Type of Packet
  - F (FLOW) (1 bit): Flow Control
  - A (ACK) (1 bit): Acknowledge (ACK)
  - S (SEQN) (1 bit): Contains sequence number for packet ordering 
  - Checksum (8 bits): Error check
- Data (0-2744 bits): Contains the data of the client

## Equipment and Material
- Raspberry Pi 3 Model B+ (2 units).
  - The Raspberry Pi 3 Model B+ has an integrated Bluetooth module.

## Development

### Software
To create the communication between the two Raspberry Pi, their integrated Bluetooth module were used. Fortunately, Python has an existing library that provides us with a simple way of using the integrated module. In order to use it, the line  `import bluetooth` must be at the top of our code.

### Communication

![Python version](https://img.shields.io/badge/python-v2.7-brightgreen.svg)

#### Server Code
```
import bluetooth

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

port=1
server_sock.bind(("", port))
server_sock.listen(1)

client_sock, address = server_sock.accept()
print "Accepted Connection from ", address

data = client_sock.recv(1024)
print "received [%s]" % data

client_sock.close()
server_sock.close()
```
#### Client Code
```
import bluetooth

bd_addr = "00:00:00:00:00:00" #Server MAC address

port = 1 #Port to be used
sock = bluetooth.BluetoothSocket (bluetooth.RFCOMM) #Create socket to use
sock.connect((bd_addr, port)) #Connect socket with the host

sock.send("Hello World!") #Send data to the server

sock.close() #Close communication
```

## Results and Analysis
As the two codes start running in their respective Raspberry Pi, the links are established and the communication starts to occur. When the Client connects its socket to the host, the message `Hello World!` is sent. At this time, the Server print the received data as:
```
received [Hello World!]
```
Clearly, Bluetooth communication takes place between our devices. 

## Conclusions
As we can see, the Bluetooth technology has taken place in our daily life, from almost every cellphone to gadgets like keyboards or mouses. Here, we recreated the most simple communication between devices; this code can be improved to create more extensive and complex communication. From controlling a simple LED to transmitting real-time audio files. The possibilities of improvement are at our reach.

It is important to emphasize that this technology is not perfect, security and communication issues can occur at any time. However this is an evolving topic, solutions and improvements are implemented with each released version.

## References
https://ecee.colorado.edu/~ecen4242/marko/Bluetooth/Bluetooth/SPECIFICATION/RFCOMM.htm
https://www.bluetooth.org/docman/handlers/DownloadDoc.ashx?doc_id=263754
