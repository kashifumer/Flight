# This class is responsible for talking to google sheets
import requests
import os
from dotenv import load_dotenv
load_dotenv()
SHEETY_ENDPOINT = os.environ.get('SHEETY_ENDPOINT')


class DataManager:

    def __init__(self):
        self.dictionary = {}

    def get_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        response.raise_for_status()
        self.dictionary = response.json()['prices']
        return self.dictionary

    def update_sheet(self):
        for data in self.dictionary:
            body = {
                'price': {
                    'iataCode': data['iataCode']
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{data['id']}", json=body)
            print(response.raise_for_status())









