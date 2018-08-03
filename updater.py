# Python 3
from godaddypy import Client, Account
import pif

def GetIpAddress():
    return pif.get_public_ip()

def LoginAccount():
    acct = Account(api_key='dLDURGMppCcr_RKTah5s9vNhDWikvvwAd8a', api_secret='test')
    client = Client(acct)
    return client

def UpdateIpAddress(client, ip):
    domains=client.get_domains()
    ret=True
    for domain in domains:
        client.update_ip(ip, domains=[domain])
        records=client.get_records(domain)
        for record in records:
            if record['type'] is 'A':
                if record['data'] != ip:
                    ret = False
    return ret

# main
UpdateIpAddress(LoginAccount(), GetIpAddress())