import requests
from credentials import *
class Send_SMS:
    def send_text_message(number, message):
        url ="https://api.jive.com/messaging/v1/messages"
        headers={'Content-Type':'application/json', 'Authorization': Authrization.BEARER_TOKEN }
        r = requests.post(url,headers=headers ,json = {"ownerPhoneNumber": "+17734823900", "contactPhoneNumbers": [ number ], "body": message})
        print(r)


