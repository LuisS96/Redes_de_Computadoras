# Wireless Communication System using Xbee
## Abstract

## Objective
Establish a connection between a transmitter and a receiver by building a wireless communication system using Xbee.

## Theoretical Framework

### Architecture
The typical ZigBee architecture can be organized in seven distinct layers, where the two on the bottom corresponds to the IEEE 802.15.4 standard; the rest of these layers allows the creation of a mesh network that makes use of the 802.15.4 radio links.

 ADD PHOTO

The 802.15.14 standard provides 16 channels on the 2.4GHz band, these channels are numbered from 11 to 26. Since ZigBee only uses the nonbeacon-enabled mode of 802.15.4, there is no possibility to access the network in a deterministically mode nor to reserve bandwidth. Furthermore, ZigBee restricts PAN IDs in the range of 0x0000 to 0x3FFF; this is only a subset of the 802.15.4 range.

ZigBee Node Types

-End Device 

-Router

-Coordinator

### Protocols

Application support sublayer

ZigBee Device Object

ZigBee Cluster Library

Application Framework

### Physical Layer


### MAC Sublayer Protocol

### Frame Structure

## Materials
* 2 XBee devices of the same model (S1, S1 Pro, S2, S2 Pro or S2C)
* 2 XBee explorer dongles
* 2 Raspberry PIs with Raspbian installed and Internet access
* XCTU software installed from https://www.digi.com/products/xbee-rf-solutions/xctu-software/xctu

## Procedure
Insert both XBee to the XBee explorers and connect them to the COM ports of your computer. Open the XCTU software and press the upper left magnifying glass button to discover the XBee devices connected to the computer. Select all COM ports and keep pressing "Next" with the default parameters to find the devices, and add them. Click on on of the devices from the left side list to open its configuration panel on the right. There are some parameters to be modified in XCTU to enable communication between both XBees, such as the PAN ID, Channel, Destination Address and Coordinator Mode. There is an extra parameter that changes depending on the model of the Xbees. First, the common parameters for all models will be explained:

For the Coordinator XBee:
* Channel is the same as the End Device/Router Xbee. Can be left as the default value C.
* PAN ID is also the same as the other XBee. In this case, it was left as 1234.
* Coordinator Mode is enabled.
* Destination Address Low is FFFF (Broadcast).

For the End Device/Router XBee:
* Channel is the same as the End Device/Router Xbee. Can be left as the default value C.
* PAN ID is also the same as the other XBee. In this case, it was left as 1234.
* Coordinator Mode is disabled
* Destination Address Low is 0 (Point to network's coordinator).

JV, MY


### Electric Circuit
### Software
### Communication

## Results & Analysis
## Conclusion
## References
[1] https://internetofthingsagenda.techtarget.com/definition/RFID-radio-frequency-identification

[2] Tanenbaum, A., Wetherall, D. (2011). Computer Networks. (pp. 327-328). 

[3] https://internetofthingsagenda.techtarget.com/definition/RFID-radio-frequency-identification

[4] Tanenbaum, A., Wetherall, D. (2011). Computer Networks. (pp. 329).

[5] EPC Global Standard

[6] Hersent, O., Boswarthick, D., & Elloumi, O. (2011). The internet of things : key applications and protocols. Retrieved from https://ebiblio.cetys.mx:4153

[7] Eady, F. (2010). Hands-on zigbee : implementing 802. 15. 4 with microcontrollers. Retrieved from https://ebiblio.cetys.mx:4153
