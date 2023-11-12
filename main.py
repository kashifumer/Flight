# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from datetime import datetime, timedelta
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
import os
from dotenv import load_dotenv
load_dotenv()
data_manager = DataManager()
sheet_data = data_manager.get_data()
flight_search = FlightSearch()
email_password = os.environ.get('EMAIL_PASSWORD')
ORIGIN_CITY_IATA = 'AKL'

# Make sure the iataCode in not missing on the sheet! Less API requests :)
# for data in sheet_data:
#     if len(data['iataCode']) == 0:
#         from flight_search import FlightSearch
#         flight_search = FlightSearch()
#         data['iataCode'] = flight_search.find_iata_code(data['city'])
#         sheet_data = data_manager.dictionary
#         data_manager.update_sheet()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))


for destination in sheet_data:
    flight = flight_search.find_flights(
        ORIGIN_CITY_IATA,
        destination['iataCode'],
        from_time=tomorrow,
        to_time=six_month_from_today,
    )
    if flight is not None and flight['price'] < destination['lowestPrice']:
        notification_manager = NotificationManager('heykashif@gmail.com', email_password)
        subject = 'Low Price Alert'
        body = f"Only ${flight['price']}, {flight['cityFrom']}-{flight['flyFrom']} -- {flight['cityTo']}-{flight['flyTo']} " \
               f"on {flight['local_departure'].split('T')[0]} \n Link - {flight['deep_link']}"
        notification_manager.send_email(subject=subject, body=body)


for destination in sheet_data:

    outbound_flight = flight_search.outbound(
        ORIGIN_CITY_IATA,
        destination['iataCode'],
        from_time=tomorrow,
        to_time=six_month_from_today,
    )

    inbound_string = (outbound_flight['local_departure'])
    timestamp = datetime.strptime(inbound_string, '%Y-%m-%dT%H:%M:%S.%fZ')
    inbound_from_timestamp = timestamp + timedelta(days=7)
    inbound_to_timestamp = timestamp + timedelta(days=28)

    inbound_flight = flight_search.inbound(
        destination['iataCode'],
        ORIGIN_CITY_IATA,
        from_time=inbound_from_timestamp,
        to_time=inbound_to_timestamp,
    )

    if outbound_flight is not None and inbound_flight is not None and outbound_flight['price'] + inbound_flight['price'] < destination['lowestPrice']:
        price = outbound_flight['price'] + inbound_flight['price']
        notification_manager = NotificationManager('heykashif@gmail.com', email_password)
        subject = 'Low Price Alert'
        body = f"Only ${price}, {outbound_flight['cityFrom']}-{outbound_flight['flyFrom']} -- " \
               f"{outbound_flight['cityTo']}-{outbound_flight['flyTo']} " \
               f"on {outbound_flight['local_departure'].split('T')[0]} \n Outbound Link - {outbound_flight['deep_link']}" \
               f"\n Inbound Link - {inbound_flight['deep_link']}"
        notification_manager.send_email(subject=subject, body=body)


































