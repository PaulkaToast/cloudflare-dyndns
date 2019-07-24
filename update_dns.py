#!/usr/bin/env python
from requests import get
import CloudFlare
import config


def get_internet_ipv4():
    # external service to grab IP address from behind router
    ip = get('https://api.ipify.org').text
    return ip

def update_dns_record(ip):
    cf = CloudFlare.CloudFlare(
        email=config.cloudflare_email,
        token=config.cloudflare_api_key
    )

    dns_record = {
        'name': config.name,
        'type': 'A',
        'content': ip,
        'proxied': False
    }

    # we want to update an existing record so we must find its record id
    # just doing a post will create a new record instead of updating it
    existing_records = cf.zones.dns_records.get(config.zone_id)
    for record in existing_records:
        if record['name'] == config.name:
            cf.zones.dns_records.put(config.zone_id, record['id'], data=dns_record)



def main():
    print("Grabbing ipv4 address...")
    ip = get_internet_ipv4()

    print("Posting updated dns record...")
    update_dns_record(ip)

    print("Done.")

if __name__ == '__main__':
    main()


