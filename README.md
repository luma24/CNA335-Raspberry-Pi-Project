## What is a Pi-hole?
Pi-hole is a network-wide ad blocker.
I will install and set up a Pi-hole on Raspberry Pi to block advertisements on all devices connected to my home network.

## How does the Pi-hole work?
Pi-hole functions as an internal, private DNS server for my home network.
Usually the DNS server is running on the router. So, I will install Pi-hole on the Raspberry Pi and sets the Raspberry Pi to be the DNS for my home network.
Pi-hole will intercept any queries for known ad-serving domains and deny them access, so ads won’t be downloaded.

## Project Prerequisites:
- Raspberry Pi Zero W with Raspbian Lite image installed on it.

## Setting up Pi-hole on a Raspberry Pi. 
                                                                   
                               │ The Pi-hole is free, but powered by your donations:                │ 
                               │ https://pi-hole.net/donate/                                        │ 
                               │                                                                    │ 
                               │                                                                    │ 
                               │                                                                    │ 
                               │                                                                    │ 
                               │                                                                    │ 
                               │                                                                    │ 
                               │                                                                    |  
                               └────────────────────────────────────────────────────────────────────┘ 
                                                          <Ok>
##


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
## 

                               
                               |Select Upstream DNS Provider. To use your own, select Custom.       |
                               │                                                                    │ 
                               │                  Google (ECS)                                      │ 
                               |                                                                    |
                               |                      <Ok>                                          |  
                               └────────────────────────────────────────────────────────────────────┘ 
                               
                               
                               
                               
##
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
  
  ##
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
##
                                                                   
                               │ Do you want to use your current network settings as a static       │ 
                               │ address?                                                           │ 
                               │           IP address:    192.168.1.7/24                            │ 
                               │           Gateway:       192.168.1.1                               │ 
                               │                                                                    │ 
                               │                                                                    │ 
                               │                                                                    │ 
                               │                  <Yes>                     <No>                    │ 
                               └────────────────────────────────────────────────────────────────────┘ 
## 

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
                               
                               
                              
## 
  
                   
                   
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
                               
##
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
##
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
##
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
##
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
                                                                                                      
## To login to the Pi-hole, on a browser search
(use your Pi Ip address):
```
http://192.168.1.7/admin
```
## Add more Adlist sources
mobile.pipe.aria.microsoft.com
www.youtube-nocookie.com
ssl.google-analytics.com
## Project Sources:
https://blog.cryptoaustralia.org.au/instructions-for-setting-up-pi-hole/

https://javan.de/pihole-dns-blocklists-adlists-auto-updater/
