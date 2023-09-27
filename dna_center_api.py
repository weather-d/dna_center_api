from dnacentersdk import DNACenterAPI as API
from pprint import pprint
import datetime
import calendar

ep = str(int(datetime.datetime(2023, 8, 22, 20, 41, 29, 0, datetime.UTC).timestamp())*1000)

DNAC = API(username="devnetuser", password="Cisco123!", base_url="https://sandboxdnac.cisco.com", verify=False)

DEVICES = DNAC.devices.get_device_list()
CLIENTS = DNAC.clients.get_overall_client_health(timestamp=ep)

for DEVICE in DEVICES.response:
    pprint(f"Hostname:  {DEVICE.hostName}, Type: {DEVICE.type}, Uptime: {DEVICE.upTime}")


print('{0:25s}{1:1}{2:45s}{3:1}{4:15s}'.format("Client Category", "|", "Number of Clients", "|", "Clients Score"))
for CLIENT in CLIENTS.response:
    for score in CLIENT.scoreDetail:
        print('{0:25s}{1:1}{2:<45d}{3:1}{4:<15d}'.format(score.scoreCategory.value, "|", score.clientCount, "|", score.scoreValue))