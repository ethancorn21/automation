from netmiko import ConnectHandler
import getpass
import os
import dotenv
from dotenv import load_dotenv

load_dotenv()

'''dsw1 = ConnectHandler(
    device_type="cisco_ios",
    host="10.0.99.1",
    username="admin",
    password="cisco.dsw1.2025",
)'''
password = os.getenv("DSW1_PASS")
username = os.getenv("DSW1_USER")
print(password)
print(username)

# create a function that asks for device, then pings all other known
#  IP's from that device