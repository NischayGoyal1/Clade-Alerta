from email import message
import requests
from twilio.rest import Client

API_TOKEN="cbda140c824cd1867548129e075d42d2"
API_SID="ACc353cc13386e614b9e7355593eb86e87"
PHN_NO='+18455168530'


client = Client(API_SID, API_TOKEN)
def sendsms(phn,name):
 message = client.messages \
                .create(
                     body=f"Hey {name}! \n There are chances of mild cyclones in your area so do take neccary precautions and follow the safety protocols \n Team Clade Alerta , Stay Safe",
                     from_=PHN_NO,
                     to=phn
                 )

sendsms("+917696073734","Vedant")

# +918742967471	

