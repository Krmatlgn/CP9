# Anonymous Security Tool

This Python tool is designed to enhance your online anonymity by configuring and managing the Tor network, changing MAC addresses, and generating random passwords. It's ideal for security professionals who need a way to ensure privacy while conducting network-related activities.

## Features

- **Tor Configuration & Management**: Restart the Tor service and change your Tor identity for anonymous browsing.
- **MAC Address Randomization**: Change the MAC address of your network interface to maintain anonymity.
- **Password Generation**: Generate random passwords for securing your connections.
- **IP Address Rotation**: Change your IP address through the Tor network for additional privacy.
  
## Installation

1. Clone this repository to your local machine:
   git clone https://github.com/username/anonymous-security-tool.git
   cd anonymous-security-tool
   
Install the required dependencies:
sudo apt update
sudo apt install tor macchanger python3-pip
pip3 install requests

Run the tool:
python3 anonymous_security_tool.py

The tool will:

Install necessary dependencies.
Generate a random Tor password.
Restart the Tor service.
Change your network interface's MAC address.
Change your Tor identity and get a new IP address.
The tool will continue running, periodically changing your MAC address, Tor identity, and IP address every 2 minutes.

Disclaimer
This tool is for educational and research purposes only. Always ensure that you comply with local laws and regulations when using this tool. The tool interacts with Tor and other security services, and it's important to understand the ethical implications of using such technologies.
