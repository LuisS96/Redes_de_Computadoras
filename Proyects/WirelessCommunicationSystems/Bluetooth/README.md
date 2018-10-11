# Wireless Communication System using Bluetooth

Made by @Fernando_Cortez, @Felix_Quevedo, and @Luis_Serrano

Subject: **Computer Network**

Professor: **Dr. Moises Sanchez Adame**

University: **CETYS University, Tijuana**

#### Abstract

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

*UPPER LAYERS*

### Frame Structure
Basic rate data frame and enhanced rate data frame

![Bluetooth Data Frame Rates](https://raw.githubusercontent.com/LuisS96/Redes_de_Computadoras/feature/Bluetooth/Proyects/WirelessCommunicationSystems/Bluetooth/Bluetooth_DataFrame.png)


#### Bluetooth Network Encapsulation Protocol (BNEP)
![BNEP Frame Structure](https://www.ahirlabs.com/wp-content/uploads/2017/12/Frameformat.png)

- Access Code: used for timing synchronization, offset, paging, and inquiry
- Header
  - Addr: Temporary address assigned
  - Type: Type of Packet
  - F (FLOW): Flow Control
  - A (ACK): Acknowledge (ACK)
  - S (SEQN): Contains sequence number for packet ordering 
  - Checksum: Error check
- Data: Contains the data of the client

#### RFCOMM
![RFCOMM Frame Structure](https://image.slidesharecdn.com/presentation1-161027145507/95/bluetooth-14-638.jpg?cb=1477580222)
- Flag: Let knows where it starts (01111101)
- Address - 1 byte
- Control - 1 byte
- Length Indicator - 1 to 2 bytes
- Data
- FCS (Frame Check Sequence) - 1 byte
- Flag: Let knows ehre it ends (01111101)

## Equipment and Material
- Two Raspberry Pi 3 Model B+
- One protoboard
- One LED (Light-Emitting Diode)

## Development

### Electrical Circuit
### Software
To create the communciation between the two Raspberry Pi, their own bluetooth module were used.

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

## Conclusions

## References
https://ecee.colorado.edu/~ecen4242/marko/Bluetooth/Bluetooth/SPECIFICATION/RFCOMM.htm
https://www.bluetooth.org/docman/handlers/DownloadDoc.ashx?doc_id=263754
