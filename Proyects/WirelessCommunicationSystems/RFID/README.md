# Wireless Communication System using RFID
## Abstract
In the following document, the wireless communication system Radio Frequency Identification (RFID) will be explained and how this technology works and configured.

## Objective
Establish a connection between a transmitter and a receiver by building a wireless communication system using RFID.

## Theoretical Framework

### Architecture
RFID systems consist of three components: a scanning antena, a transreceiver and a transponder or commonly called tag. The first two items are usually combined into a single artifact called a reader. Tags are generally composed of an antenna and memory only, so they don't have a battery or power source other than the power obtained by a carrier activation signal from the reader. [1]

![RFID Architecture](https://github.com/LuisS96/Redes_de_Computadoras/blob/feature/RFID/Proyects/WirelessCommunicationSystems/RFID/RFID.jpg)

An RFID network then consists of a group of readers and tags that will communicate with each other, with the restriction that readers can only communicate to tags and they only respond to the raeader's commands and queries. Tags cannot communicate between them, and multiple readers may try to communicate to a subset of the tags another reader is interacting with. Another problem is how to manage low power consumption communication with the tags since they harness their power from RF signals. Both situations are solved with the protocols RFID use as it will be explained in detail. [2]

### Protocols
#### EPC Radio-Frequency Identity Protocol
This protocol defines the physical and logical requirements for a Radio Frequency Identification (RFID) system operating in the 860 MHz - 960 MHz frequency range. The system is composed by Readers and Tags.

The Reader transmits information to a Tag by modulating an RF signal in the frequencies range mentioned before. The Tag receives both information and operating energy from the RF signal.

The Reader receives information from a Tag by transmitting a continuous-wave (CW) signal to the Tag; the Tag responds by modulating the reflection ocoefficient of its antenna. The system is ITF, meaning that a Tag modulates its antenna reflection with an information signal only after being directed by the Reader.

### Physical Layer
The RFID physical layer defines how bits are sent between tags and readers. There are three main type of RFID systems: LF RFID (low frequency) which range from 30 kHz to 500 kHz; HF RFID (high frequency) whose frequency band is delimited from 3 MHz to 30 MHz; UHF RFID with a frequency set going from 300 MHz to 960 MHz. The distance range depends on the frequency type implemented. LF can transmit from a couple of inches to less than six feet; HF can go to more feet distance; finally, UHF can be read from more than 25 feet away. [3]

In contrast to other physical layers, the reader is always transmitting a signal, regardless of whether it is the reader or tag that is communicating. The reader transmits a fixed carrier signal from which the tags get the power they need to run. The method used by the tag to communicate with the reader is called backscatter, which is a low-energy way for it to create a weak signal that shows up in the reader, by bouncing the latter's signal or absorbing it. Since the tag signal is weak, communication to the reader is limited to a low rate and inhibits the tags from sensing transmissions from other ones. [4]

To send data to the tags, the reader uses two amplitude levels, being the lower one the transition between two bits. A 0 bit is represented with a shorter period between low-power states, and a 1 bit is given by a longer period. Tags responses consist of the alternation of its backscatter signal in fixed intervals. 0s have more pulses than 1s, and the reader interprets between this two types of signals.

### MAC Sublayer Protocol
Generally, there will be an unknown number of tags nearby, so it is necessary for the reader to inventory all the tags in range; however, broadcasting a query to ask all tags to send their identifiers may cause data collision if all tags reply right away. This situation is similar to the Hawaiian isle computers trying to communicate between theme, so the protocol used is slotted ALOHA, which suits well the problem that tags cannot hear their neighbors. 

The sequence of messages used to identify the surrounding tags starts with a Query message in the first slot (slot 0). Each of the next Qrepeat messages sent advances to the next slot. The reader must also specify the range of slots over which the tags will randomize transmissions; afterwards, each tag picks a random slot in which their reply will be sent. The reply is consists of a 16-bit random number inside a RN16 message. If there is no collision, the reader is able to receive the message and replies back with an ACK (acknowledge) message, to tell the tag that it can now send its identifier. Once its identifier gets to the reader, the the tag stops responding to new Query messages until all the remaining tags were identified. 

Among other operations the reader can perform, there is the slot range adjustment. If the reader sees too many slots with no responses or too many slots with collisions, it readjusts the range of slots used by the tags by sending a QAdjust message. Furthermore, the reader can perform a subset selection operation on the tags, so that collect responses from tags that meet a certain criteria. The reader also has the ability to to write data to tags as they are identified to store instance specific information to different tags.

### Frame Structure
The frame structure and size depend on the type of message the reader wants to send to the tag, as well as the type of reply the tag will transmit back. The most common command, the Query command, has the following format:

![Query Command Frame](https://github.com/LuisS96/Redes_de_Computadoras/blob/feature/RFID/Proyects/WirelessCommunicationSystems/RFID/Query%20Command%20Frame.PNG)

The first four bits of all reader messages specify the command type, in this case, 1000 denotes a Query command. The next three parameters specify the physical layer parameters that modify the frequency link, data rate and modulation format, and pilot tone inclusion in reader-tag transmissions.   Sel chooses which tags will respond to this reader's Query command. Session chooses the tag session where to send the Query command for the inventory round. Target chooses whether the tags with flag A or with flag B should take part in the inventory round. Q is a very important parameter, since it specifies the number of slots in the current round. The CRC field is a 5 bit error checking code, shorter than other CRCs because the RFID frames are shorter than in other technologies. The other commands will have a similar format to his one. [5].

## Materials
* 2 Raspberry PIs
* 1 MFRC522 card
* 1 RFID tag or RFID card
* 8 Male-to-Female jumpers
* 1 Small breadboard

## Procedure

### Electric Circuit
The pinout of the MFRC522 chip to the Raspberry PI is the following:

![RFID Main Logo](https://github.com/LuisS96/Redes_de_Computadoras/blob/feature/RFID/Proyects/WirelessCommunicationSystems/RFID/RFID-Diagram.png)

* **SDA** connects to **Pin 24**.
* **SCK** connects to **Pin 23**.
* **MOSI** connects to **Pin 19**.
* **MISO** connects to **Pin 21**.
* **GND** connects to **Pin 6**.
* **RST** connects to **Pin 22**.
* **3.3V** connects to **Pin 1**.


### Software
First, install the python development tools if missing.
```
sudo apt-get install python2.7-dev
```

Then, the Python Py-PI module is added to the Raspberry.
```
cd ~
git clone https://github.com/lthiery/SPI-Py.git
```
and then installed:
```
cd ~/SPI-Py
sudo python setup.py install
```

Finally, clone the SimpleMFRC522 repository to use its module.
```
cd ~
git clone https://github.com/pimylifeup/MFRC522-python.git
```

### Communication
Create a tag writer python script that has the following lines of code:

```
#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

try:
        text = raw_input('´Type the data you want to write to your tag: ')
        print "Now place your tag to write"
        reader.write(text)
        print "Written"
finally:
        GPIO.cleanup()
```

And a tag reader python script:

```
#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

try:
        id, text = reader.read()
        print(id)
        print(text)
finally:
        GPIO.cleanup()
```

Run the writer as a super user to write a new string to your tag, and then run the reader script to see the contents of the tag (or card).
## Results & Analysis
Running the writer code once and then the reader script gives the following result. No problems happened with the communication of the MFRC522 and the tag.

## Conclusion
Nowadays, the use of Radio Frequency Identification (RFID) is finding its place in several different applications and social contexts. The low cost and convenience of RFID tags is helping the market integrate these systems in places from package identification, security tags, personnel accessing ID, and even public transport. 

In this low-power demanding world, RFID systems can be easily developed and implemented. Here, we implemented a simple and understandable way to read and write data into our own tag. The RFID module allowed us to create the bases of a whole RFID system, that can grow and become as simple or complex as our necessities require. 

## References
[1] Rouse, M. (2017). RFID (radio frequency identification). Recovered from: https://internetofthingsagenda.techtarget.com/definition/RFID-radio-frequency-identification

[2] Tanenbaum, A., Wetherall, D. (2011). Computer Networks. (pp. 327-328). 

[3] Rouse, M. (2017). RFID (radio frequency identification). Recovered from: https://internetofthingsagenda.techtarget.com/definition/RFID-radio-frequency-identification

[4] Tanenbaum, A., Wetherall, D. (2011). Computer Networks. (pp. 329).

[5] EPC Global Standard

[6] PiMyLifeUp, (2017). How to setup a Raspberry Pi RFID RC522 Chip. Recovered from: https://pimylifeup.com/raspberry-pi-rfid-rc522/
