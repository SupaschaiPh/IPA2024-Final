import json
import requests
requests.packages.urllib3.disable_warnings()

# Router IP Address is 10.0.15.181-184
api_url = "10.0.15.184"

# the RESTCONF HTTP headers, including the Accept and Content-Type
# Two YANG data formats (JSON and XML) work with RESTCONF 
headers = headers = {"Accept": "application/yang-data+json",
                     "Content-type": "application/yang-data+json"
                     }
basicauth = ("admin", "cisco")


def create():
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": "Loopback65070242",
            "type": "iana-if-type:softwareLoopback",
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": "172.30.242.1",
                        "netmask": "255.255.255.0"
                    }
                ]
            }
        }
    }

    resp = requests.post(
        f"https://{api_url}/restconf/data/ietf-interfaces:interfaces/",
        data=json.dumps(yangConfig),
        auth=basicauth,
        headers=headers,
        verify=False
    )
    if (resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 65070242 is created successfully"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
        return "Cannot create: Interface loopback 65070242"


def delete():
    resp = requests.delete(
        f"https://{api_url}/restconf/data/ietf-interfaces:interfaces/interface=Loopback65070242",
        auth=basicauth,
        headers=headers,
        verify=False
    )

    if (resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 65070242 is deleted successfully"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
        return "Cannot delete: Interface loopback 65070242"


def enable():
    yangConfig = {
        "ietf-interfaces:interface": {
            "enabled": True
        }
    }

    resp = requests.patch(
        f"https://{api_url}/restconf/data/ietf-interfaces:interfaces/interface=Loopback65070242",
        data=json.dumps(yangConfig),
        auth=basicauth,
        headers=headers,
        verify=False
    )

    if (resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 65070242 is enabled successfully"

    else:
        print('Error. Status Code: {}'.format(resp.status_code))
        return "Cannot enable: Interface loopback 65070242"


def disable():
    yangConfig = {
        "ietf-interfaces:interface": {
            "enabled": False
        }
    }

    resp = requests.patch(
        f"https://{api_url}/restconf/data/ietf-interfaces:interfaces/interface=Loopback65070242",
        data=json.dumps(yangConfig),
        auth=basicauth,
        headers=headers,
        verify=False
    )

    if (resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 65070242 is shutdowned successfully"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
        return "Cannot shutdown: Interface loopback 65070242"


def status():
    api_url_status = f"https://{api_url}/restconf/data/ietf-interfaces:interfaces-state/interface=Loopback65070242"

    resp = requests.get(
        api_url_status,
        auth=basicauth,
        headers=headers,
        verify=False
    )

    if (resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        response_json = resp.json()
        admin_status = response_json["ietf-interfaces:interface"]["admin-status"]
        oper_status = response_json["ietf-interfaces:interface"]["oper-status"]
        if admin_status == 'up' and oper_status == 'up':
            return "Interface loopback 65070242 is enabled"
        elif admin_status == 'down' and oper_status == 'down':
            return "Interface loopback 65070242 is disabled"
    elif (resp.status_code == 404):
        print("STATUS NOT FOUND: {}".format(resp.status_code))
        return "No Interface loopback 65070242"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))

