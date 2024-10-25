from netmiko import ConnectHandler
from pprint import pprint

device_ip = "10.0.15.184"
username = "admin"
password = "cisco"

device_params = {
    "device_type": "cisco_ios",
    "ip": device_ip,
    "username": username,
    "password": password,
}


def gigabit_status():
    ans = ""
    with ConnectHandler(**device_params) as ssh:
        up = 0
        down = 0
        admin_down = 0
        result = ssh.send_command("show interfaces", use_textfsm=True)
        #print(result)
        for count,status in enumerate(result):
            if  status["interface"].startswith("Gigabit"):
                ans += status["interface"] + " " + status["link_status"]
                if count != len(ans)-1:
                    ans += ", "
                if status["link_status"] == "up":
                    up += 1
                elif status["link_status"] == "down":
                    down += 1
                elif status["link_status"] == "administratively down":
                    admin_down += 1
                ans += " "
        ans += f"-> {up} up, {down} down, {admin_down} administratively down"
        
        #pprint(result)
        print(ans)
        return ans
