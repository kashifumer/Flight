# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from datetime import datetime, timedelta
from pprint import pprint


from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
data_manager = DataManager()
sheet_data = data_manager.get_data()
flight_search = FlightSearch()
ORIGIN_CITY_IATA = 'AKL'


for data in sheet_data:
    if len(data['iataCode']) == 0:
        from flight_search import FlightSearch
        flight_search = FlightSearch()
        data['iataCode'] = flight_search.find_iata_code(data['city'])
        sheet_data = data_manager.dictionary
        data_manager.update_sheet()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

# return_start_date = tomorrow + timedelta(days=7)
# return_end_date = six_month_from_today + timedelta(days=28)
# and difference between start and return start > 7 or < 28, logic similar to this should solve your problem


for destination in sheet_data:
    # flight = flight_search.find_flights(
    #     ORIGIN_CITY_IATA,
    #     destination['iataCode'],
    #     from_time=tomorrow,
    #     to_time=six_month_from_today,
    # )
    # pprint(flight)
    flight = flight_search.outbound(
        ORIGIN_CITY_IATA,
        destination['iataCode'],
        from_time=tomorrow,
        to_time=six_month_from_today,
    )
    pprint(flight)








    # if flight is not None and flight.price[0] < destination['lowestPrice']:
    #     notification_manager = NotificationManager()
    #     notification_manager.notification(f'Low price alert! Only {flight.price} to fly from {flight.origin_city}-'
    #                                       f'{flight.origin_airport} to {flight.destination_city}-'
    #                                       f'{flight.destination_airport}, from {flight.out_date} to {flight.return_date}')






























