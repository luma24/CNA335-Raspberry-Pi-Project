# CNA330 Raspberry-Pi Final Project
## What is a Pi-hole?
Pi-hole is a network-wide ad blocker.
I will install and set up a Pi-hole on Raspberry Pi to block advertisements on all devices connected to my home network.

## what is the benefit of using Pi-hole?
#### - PI-HOLE CAN MAKE YOUR NETWORK FASTER:
Pi-hole work at the DNS level.  So when an ad is blocked, it’s actually prevented from being downloaded 
in the first place because the DNS query is intercepted. Since these ad images, videos, and sounds are not being downloaded, your network will perform better.
#### -  PI-HOLE CAN PROTECT YOUR NETWORK FROM MALWARE:
We can add additional block lists to your installation that will prevent domains that are known to serve malware or act as a phishing site from ever entering your network.
#### -  PI-HOLE CAN BLOCK ADS IN NON-TRADITIONAL PLACES:
Advertisements in smart TVs and mobile apps can’t be blocked by browser-based ad blockers because smart TVs and  mobile apps don’t run in a browser.  This is where Pi-hole shines; since the ads are prevented at the network level (before the ads reach the device), you can prevent ads from appearing on Internet-connected devices that aren’t 
a Web browser.
## How does the Pi-hole work?
Pi-hole functions as an internal, private DNS server for my home network.
Usually the DNS server is running on the router. So, I will install Pi-hole on the Raspberry Pi and sets the Raspberry Pi to be the DNS for my home network.
Pi-hole will intercept any queries for known ad-serving domains and deny them access, so ads won’t be downloaded.

## Project Prerequisites:
- Raspberry Pi Zero W with Raspbian Lite image installed on it.

## Setting up Pi-hole on a Raspberry Pi. 
### First update and upgrade your pi by running these commands:
```
sudo apt-get update
sudo apt-get upgrade
```
### It might you need curl tool, to install it:
```
sudo apt-get install curl
```
## To install Pi-hole, run this command:
```
curl -sSL https://install.pi-hole.net | bash
```
### Follow this instruction to finish the installation: (press enter to continue)

                               │Pi-hole automated installer                                         │ 
                               │This installer will transform your device into a network-wide       |
                               | ad blocker!                                                        |
                               |                                                                    │ 
                               │                                                                    │ 
                               │                              <Ok>                                  |
                               └────────────────────────────────────────────────────────────────────┘   
### Press enter to continue
  
                                                                   
                               │ The Pi-hole is free, but powered by your donations:                │ 
                               │ https://pi-hole.net/donate/                                        │ 
                               │                                                                    │ 
                               │                                                                    │ 
                               │                                                                    │ 
                               │                                                                    │ 
                               │                                                                    │ 
                               │                                                                    │ 
                               │                          <Ok>                                      |  
                               └────────────────────────────────────────────────────────────────────┘ 
                                                          
### Pi-hole server needs a STATIC IP ADDRES, hit enter to continue


                                                      Static IP Needed 
                               │                                                                    │ 
                               │                                                                    │ 
                               │                                                                    │ 
                               │ The Pi-hole is a SERVER so it needs a STATIC IP ADDRESS to         │ 
                               │ function properly.                                                 │ 
                               │                                                                    │ 
                               │ In the next section, you can choose to use your current network    │ 
                               │ settings (DHCP) or to manually edit them.                          │ 
                               │                                                                    │
                               │                                                                    │ 
                               │                                                                    │ 
                               │                               <Ok>                                 │ 
                               │                                                                    │  
                               └────────────────────────────────────────────────────────────────────┘ 
### Here I will select Google (ECS) as a Upstream DNS Provider

                               
                               |Select Upstream DNS Provider. To use your own, select Custom.       |
                               │                                                                    │ 
                               │                  Google (ECS)                                      │ 
                               |                                                                    |
                               |                      <Ok>                                          |  
                               └────────────────────────────────────────────────────────────────────┘ 
                               
                               
                               
                               
### Hit enter to continue
                                 Pi-hole relies on third party lists in order to block ads.         │ 
                               │                                                                    │ 
                               │ You can use the suggestion below, and/or add your own after        │ 
                               │ installation                                                       │ 
                               │                                                                    │ 
                               │ To deselect the suggested list, use spacebar                       │ 
                               │                                                                    │ 
                               │    [*] StevenBlack  StevenBlack's Unified Hosts List               │ 
                               │                                                                    │ 
                               │                                                                    │ 
                               │                                                                    │ 
                               │                 <Ok>                     <Cancel>                  │  
                               └────────────────────────────────────────────────────────────────────┘ 
  
### Select the protocol and hit the enter
                                Select Protocols (press space to toggle selection)                  │ 
                               │                                                                    │ 
                               │    [*] IPv4  Block ads over IPv4                                   │ 
                               │    [*] IPv6  Block ads over IPv6                                   │ 
                               │                                                                    │ 
                               │                                                                    │ 
                               │                                                                    │ 
                               │                                                                    │ 
                               │                                                                    │ 
                               │                 <Ok>                     <Cancel>                  │ 
                               │                                                                    │ 
                               └────────────────────────────────────────────────────────────────────┘ 
### Here I will use this Ip Address
                                                                   
                               │ Do you want to use your current network settings as a static       │ 
                               │ address?                                                           │ 
                               │           IP address:    192.168.1.7/24                            │ 
                               │           Gateway:       192.168.1.1                               │ 
                               │                                                                    │ 
                               │                                                                    │ 
                               │                                                                    │ 
                               │                  <Yes>                     <No>                    │ 
                               └────────────────────────────────────────────────────────────────────┘ 
### This is an IP Conflict warning 

                                                    FYI: IP Conflict 
                               │                                                                    │ 
                               │ It is possible your router could still try to assign this IP to a  │ 
                               │ device, which would cause a conflict.  But in most cases the       │ 
                               │ router is smart enough to not do that.                             │ 
                               │ If you are worried, either manually set the address, or modify the │ 
                               │ DHCP reservation pool so it does not include the IP you want.      │ 
                               │ It is also possible to use a DHCP reservation, but if you are      │ 
                               │ going to do that, you might as well set a static address.          │ 
                               │                                                                    │ 
                               │                                                                    │ 
                               │                                                                    │ 
                               │                                                                    │ 
                               │                               <Ok>                                 │    
                               └────────────────────────────────────────────────────────────────────┘ 
                               
                               
                              
### Install the web admin interface, click enter to continue 

                               |  Do you wish to install the web admin interface?                   │ 
                               │                                                                    │ 
                               │    (*) On (Recommended)                                            │ 
                               │    ( ) Off                                                         │ 
                               │                                                                    │ 
                               │                                                                    │ 
                               │                                                                    │ 
                               │                                                                    │ 
                               │                                                                    │ 
                               │                 <Ok>                     <Cancel>                  │   
                               └────────────────────────────────────────────────────────────────────┘ 
                               
### Install the web server
                               │ Do you wish to install the web server (lighttpd) and required PHP  │ 
                               │ modules?                                                           │ 
                               │                                                                    │ 
                               │ NB: If you disable this, and, do not have an existing web server   │ 
                               │ and required PHP modules (sqlite3 xml json intl) installed, the    │ 
                               │ web interface will not function. Additionally the web server user  │ 
                               │ needs to be member of the "pihole" group for full functionality.   │ 
                               │                                                                    │ 
                               │    (*) On (Recommended)                                            │ 
                               │    ( ) Off                                                         │ 
                               │                                                                    │ 
                               │                                                                    │ 
                               │                                                                    │ 
                               │                 <Ok>                     <Cancel>                  │ 
                               │                                                                    │ 
                               └────────────────────────────────────────────────────────────────────┘ 
### log queries on
                                           Do you want to log queries?                              │ 
                               │                                                                    │ 
                               │    (*) On (Recommended)                                            │ 
                               │    ( ) Off                                                         │ 
                               │                                                                    │ 
                               │                                                                    │ 
                               │                                                                    │ 
                               │                                                                    │ 
                               │                                                                    │ 
                               │                 <Ok>                     <Cancel>                  │    
                               └────────────────────────────────────────────────────────────────────┘ 
### Here I will select ``` show everything```, and hit enter to continue
                                 Select a privacy mode for FTL.                                     │ 
                               │ https://docs.pi-hole.net/ftldns/privacylevels/                     │ 
                               │                                                                    │ 
                               │    (*) 0  Show everything                                          │ 
                               │    ( ) 1  Hide domains                                             │ 
                               │    ( ) 2  Hide domains and clients                                 │ 
                               │    ( ) 3  Anonymous mode                                           │ 
                               │                                                                    │ 
                               │                                                                    │ 
                               │                                                                    │ 
                               │                                                                    │ 
                               │                 <Ok>                     <Cancel>                  │   
                               └────────────────────────────────────────────────────────────────────┘ 
### Installation Complete, click enter
                                                  Installation Complete! 
                               │                                                                    │ 
                               │ Configure your devices to use the Pi-hole as their DNS server      │ 
                               │ using:                                                             │ 
                               │                                                                    │ 
                               │ IPv4:        192.168.1.7                                           │ 
                               │ IPv6:        Not Configured                                        │ 
                               │                                                                    │ 
                               │ If you set a new IP address, you should restart the Pi.            │ 
                               │                                                                    │ 
                               │ The install log is in /etc/pihole.                                 │ 
                               │                                                                    │ 
                               │ View the web interface at http://pi.hole/admin or                  │ 
                               │ http://192.168.1.7/admin                                           │ 
                               │                                                                    │ 
                               │ Your Admin Webpage login password is U6a2QhEm                      │ 
                               │                                                                    │ 
                               │                               <Ok>                                 │ 
                               │                                                                    │ 
                               └────────────────────────────────────────────────────────────────────┘ 
###  After finish the installation, login to the Pi-hole                                                                                                    
### To login to the Pi-hole, on a browser search, then login using you Pi password
(use your Pi Ip address):
```
http://192.168.1.7/admin
```

### Also you can add more Adlist sources
After you login to the Pi-hole Go to``` setting ```> ```Adlist ```> ```group management pages```
Add these Addresses and then run pihole -g or or update your gravity list online after modifying the adlists. 
```
mobile.pipe.aria.microsoft.com
www.youtube-nocookie.com
ssl.google-analytics.com
```
### Test the Pi-hole
Tes the Pi-hole out by re-configuring an individual computer to use Pi-hole's DNS service.
To do this, change the DNS server on the computer you want to test, to the IP address of the Pi-hole server (In my case is 192.168.1.7)

### Re-configure the router 
We can reconfigure the home router to use the Pi-hole as a DNS server.

## Project Sources:
https://blog.cryptoaustralia.org.au/instructions-for-setting-up-pi-hole/

https://javan.de/pihole-dns-blocklists-adlists-auto-updater/
