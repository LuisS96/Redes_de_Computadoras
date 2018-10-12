# Wireless Communication System using Xbee
## Abstract

## Objective
Establish a connection between a transmitter and a receiver by building a wireless communication system using Xbee.

## Theoretical Framework

### Architecture

### Protocols

### Physical Layer

### MAC Sublayer Protocol

### Frame Structure

## Materials
* 2 XBee devices of the same model (S1, S1 Pro, S2, S2 Pro or S2C)
* 2 XBee explorer dongles
* 2 Raspberry PIs with Raspbian installed and Internet access
* XCTU software installed from https://www.digi.com/products/xbee-rf-solutions/xctu-software/xctu

## Procedure
### Electric Circuit
The electric circuit implemented was simple, since it only consists of two raspberry pi, with one USB XBee explorer and an XBee connected to each Raspberry PI.

### Software
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

For models S1 and S1 Pro the extra parameter to configure is Source Address Bits MY. For the Coordinator XBee, MY = 0; on the other hand, for the End Device/Router XBee, MY = 1. Instead, if other model is used, the parameter to be modified is Channel Verifiction JV. In the case of the End Point, it is equal to 1, and with the Coordinator is 0. 

### Communication

## Results & Analysis
## Conclusion
## References
[1] https://internetofthingsagenda.techtarget.com/definition/RFID-radio-frequency-identification

[2] Tanenbaum, A., Wetherall, D. (2011). Computer Networks. (pp. 327-328). 

[3] https://internetofthingsagenda.techtarget.com/definition/RFID-radio-frequency-identification

[4] Tanenbaum, A., Wetherall, D. (2011). Computer Networks. (pp. 329).

[5] EPC Global Standard
