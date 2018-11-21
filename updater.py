# Python 3
from godaddypy import Client, Account
import pif
import logging
import time

def GetIpAddress():
    return pif.get_public_ip()

def LoginAccount():
    acct = Account(api_key='?', api_secret='?')
    client = Client(acct)
    return client

def UpdateIpAddress(client, ip):
    domains=client.get_domains()
    ret=True
    for domain in domains:
        try:
            client.update_ip(ip, domains=[domain])
            records=client.get_records(domain)
        except:
            logging.info("Fail to update: %s"%domain)
        for record in records:
            if record['type'] is 'A':
                if record['data'] != ip:
                    ret = False
    return ret

# main
logging.basicConfig(filename='/tmp/ddns_godaddy.log', format='%(asctime)s: %(levelname)s: %(message)s', level=logging.INFO)
current_ip = None
updated = False
while True:
    new_ip = GetIpAddress()
    updated = UpdateIpAddress(LoginAccount(), new_ip)
    if new_ip != current_ip:
        logging.info('ip address changed: %s -> %s'%(current_ip, new_ip))
        current_ip = new_ip
    logging.info("Update: %s"%updated)
    time.sleep(60)
logging.warning("Exit")
