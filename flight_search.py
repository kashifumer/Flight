# This class is responsible for talking to the Flight Search API.
import requests
from requests. exceptions import HTTPError
IATA_URL = 'https://api.tequila.kiwi.com/locations/query'
FIND_CHEAP_FLIGHTS_URL = 'https://api.tequila.kiwi.com/v2/search'
API_KEY = 'HTeTgrth2whx7oQyEARIWZlbgqWo1gmh'
headers = {
    'apikey': API_KEY,
}

class FlightSearch:
    def find_iata_code(self, city):
        query = {'term': city}
        response = requests.get(IATA_URL, headers=headers, params=query)
        response.raise_for_status()
        result = response.json()
        return result['locations'][0]['code']

    def find_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        query = {
            'fly_from': origin_city_code,
            'fly_to': destination_city_code,
            'date_from': from_time.strftime('%d/%m/%Y'),
            'date_to': to_time.strftime('%d/%m/%Y'),
            'nights_in_dst_from': 15,
            'nights_in_dst_to': 30,
            'curr': 'NZD',
            'max_stopovers': 4,
        }
        try:
            response = requests.get(FIND_CHEAP_FLIGHTS_URL, params=query, headers=headers)
            response.raise_for_status()
        except HTTPError as e:
            if e.response.status_code == 422:
                print(f"HTTP Error {e.response.status_code}: {e.response.text} {query['fly_to']}")
            return None
        try:
            data = response.json()['data'][0]
        except IndexError:
            print(f'No flights found for {destination_city_code}')
            return None
        return data



































