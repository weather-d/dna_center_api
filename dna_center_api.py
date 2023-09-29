from dnacentersdk import DNACenterAPI as API
from pprint import pprint
import datetime


DT_OBJ = datetime.datetime(2023, 8, 22, 20, 41, 29, 0, datetime.UTC)
EP = str(int(DT_OBJ.timestamp())*1000)

DNAC = API(username="devnetuser", 
           password="Cisco123!", 
           base_url="https://sandboxdnac.cisco.com", 
           verify=False)

DEVICES = DNAC.devices.get_device_list()
CLIENTS = DNAC.clients.get_overall_client_health(timestamp=EP)

print(f'{"Hostname":33s} \
        {"|":1}{"Device Type":53s} \
        {"|":1}{"Uptime":15s}')

print('-'*130)

for DEVICE in DEVICES.response:
    print(f'{DEVICE.hostname:28s} \
             {"|":1}{DEVICE.type:48s} \
             {"|":1}{DEVICE.upTime:15s}')

print('-'*130)

print(f'{"Client Category":33s} \
        {"|":1}{"Number of Clients":53s} \
        {"|":1}{"Clients Score":15s}')

print('-'*130)

for CLIENT in CLIENTS.response:
    for score in CLIENT.scoreDetail:
        print(f'{score.scoreCategory.value:25s} \
                {"|":1}{score.clientCount:<45d} \
                {"|":1}{score.scoreValue:<15d}')

print('-'*130)