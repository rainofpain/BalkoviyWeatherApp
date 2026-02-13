import requests

def api_request(link: str):
    
    response = requests.get(link)
    data_dict = response.json()

    return data_dict