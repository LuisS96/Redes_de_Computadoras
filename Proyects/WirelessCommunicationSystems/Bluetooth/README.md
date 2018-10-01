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
### Protocols
- #### RFCOMM
Radio Frequency Communication (RFCOMM) is a set of transport protocols that provides emulation of serial ports `RS-232` over the L2CAP protocol, which establishes a Bluetooth communication. It supports up to 60 simultaneous connections between two bluetooth devices.

It exists two different types of devices:
- **Type 1**: end points like computers, smartphones, speakers, and many others.
- **Type 2**: part of the communication segment like modems, AP, etc.

There are no entities defined, therefore devices type 2 can communicate with devices of the same type.

### Physical Layer
### MAC Sublayer Protocol
### Frame Structure
#### Bluetooth
![Bluetooth Frame Structure](https://www.ahirlabs.com/wp-content/uploads/2017/12/Frameformat.png)

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
(image)
- Flag: Let knows where it starts.
- Address
- Control
- Length Indicator
- Information
- FCS (Frame Check Sequence)
- Flag: Let knows ehre it ends.

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
