import requests

url = "https://sogramihqpama90.info53.com/BeyondTrust/api/public/v3/Auth/SignAppin"

payload = ""
headers = {
    'content-type': "application/json",
    'authorization': "PS-Auth key=db9aa6c089d28c3ae367da46ce42dc6515a81edba8a682f12745cc5a450af33cf57d4d53d9181fd0980ffe332e0bc402dcea24a8f016fbf72c75e338e32da443; runas=dm0001.info53.com\e455352;"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
