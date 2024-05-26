# This class is responsible for talking to google sheets
import requests
SHEETY_ENDPOINT = 'https://api.sheety.co/6e46dcf33f155c3a29e2aeb53bfbd031/flightDeals/prices'


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









