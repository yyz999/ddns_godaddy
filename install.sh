#!/bin/bash
#
# Deploy python3 script and a runner shell to /bin/ddns_godaddy

sudo rm -rf /bin/ddns_godaddy
sudo mkdir /bin/ddns_godaddy
sudo cp updater.py /bin/ddns_godaddy/ddns_godaddy_prod.py
sudo cp run /bin/ddns_godaddy/
sudo chmod +x /bin/ddns_godaddy/run


## Monitor ddns_godaddy process
#  check process ddns_godaddy with pidfile /var/run/ddns_godaddy.pid
#  start = "/bin/ddns_godaddy/run start"
#  stop = "/bin/ddns_godaddy/run stop"