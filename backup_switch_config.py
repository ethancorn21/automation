from netmiko import ConnectHandler
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

date = datetime.now().strftime("%Y-%m-%d")
backup_dir = "./backups"

device_inventory = [
    {"device_type":"cisco_ios", "host":"10.0.99.1", "hostname":"dsw1", "username":os.getenv("DSW1_USER"), "password":os.getenv("DSW1_PASS")},
    {"device_type":"cisco_ios", "host":"10.0.99.2", "hostname":"asw1", "username":os.getenv("ASW1_USER"), "password":os.getenv("ASW1_PASS")}
]

for device in device_inventory:
    hostname = device.pop("hostname")
    connection = ConnectHandler(**device) # opens connection to device
    output = connection.send_command("show running-config") # connection is given method and saved to var
    current_dir = os.path.join(backup_dir,date)
    os.makedirs(current_dir,exist_ok=True)

    full_path = os.path.join(current_dir, hostname + ".txt")

    with open(full_path,"w") as file:
        file.write(output)
