# This class is responsible for sending notifications with the deal flight details.
from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()
from flight_search import FlightSearch
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')


class NotificationManager:

    def notification(self, message):
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=message,
            from_='+17622485658',
            to='+64223827851',
        )
        print(message.status)





