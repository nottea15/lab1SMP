import requests

class APIClient:
    def __init__(self, api_url):
        self.api_url = api_url

    def get_data(self):
        response = requests.get(self.api_url)
        return response.json()

