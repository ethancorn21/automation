## UTILITY TO ADD:
## allow user to pick switch
## menu for quick show commands
##      option to allow for "custom" command to be sent
## 

from netmiko import ConnectHandler
##net_connect is the connection handler
net_connect = ConnectHandler(
    device_type="cisco_ios",
    host="10.0.99.1",
    username="admin",
    password="cisco.dsw1.2025",
)

def command_to_switch():
    command = input("Please enter command to send to switch: ")
    return net_connect.send_command(command)

running = True
while running:
    if command_to_switch!="quit":
        print(command_to_switch())
    else:
        break
print("you have exited the switch")

    