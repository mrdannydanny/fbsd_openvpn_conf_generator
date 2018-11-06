# fbsd_openvpn_conf_generator

A python script that generates an openvpn config file for one or multiple clients.

## Requirements
* You need to be able to log in as root on your server via ssh (It's important
  to make it impossible to log in as root once you finish using this script).
* Python version 3 or higher must be installed locally on your system.

## How to use?
```
git clone https://github.com/danzarov/fbsd_openvpn_conf_generator.git && cd fbsd_openvpn_conf_generator

python3 conf_generator.py (It will ask for the client name and your vpn server ip address).
```

* Important: You can specify multiple clients separated by spaces (e.g., John Stuart James)
if you want to generate multiple config files at once.
