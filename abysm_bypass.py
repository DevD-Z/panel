
import requests

def bypass_link(url):
    api_url = f"https://api.izen.lol/v1/bypass?url={url}"
    headers = {"x-api-key": api_key}
    response = requests.get(api_url, headers=headers)
    if response.status_code != 200:
        print("Abysm API call failed")
        return None
    data = response.json()
    if data.get("status") == "success":
        return data.get("result")
    else:
        print("Bypass failed")
        return None
