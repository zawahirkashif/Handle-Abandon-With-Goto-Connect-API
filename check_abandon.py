
import requests
import datetime, pytz
from datetime import timedelta
import pandas as pd
from pandas import DataFrame
from credentials import *

class Cart_Data:
    def abandon_cart_data():
        customer_data = []
        created_time_max = datetime.datetime.now(pytz.timezone('US/Central')) - timedelta(hours= Authrization.TOTAL_DURATION )
        iso_date = created_time_max.replace(microsecond=0).isoformat()
        # input_time = iso_date 
        print(iso_date)
        post_url=f'https://{Authrization.API_KEY}:{Authrization.ADMIN_API}@{Authrization.STORE_URL}/api/{Authrization.API_VERSION}/{Authrization.ABANDON_END_POINT}{iso_date}'
        print(post_url)
        response = requests.request("GET", post_url)
        for details in response.json()['checkouts']:

            accept_marketing = details['buyer_accepts_marketing']
            email = details['email']
            customer_details = details['customer']
            customer_phone = details['phone']

            customer_name = customer_details['first_name']
            try:
                contact_details = customer_details['default_address']
                phone = contact_details['phone']
            except:
                phone = ""
            for product in details['line_items']:
                vendor = product['vendor']
            
            product = {
                    "Customer_Name": customer_name,
                    "Accept_Marketing": accept_marketing,
                    "Email": email,
                    "Primary": customer_phone,
                    "Secondary": phone,
                    "Vendor": vendor
            }
            customer_data.append(product)
        df = pd.DataFrame(customer_data)

        abandon_cart_data = df[(df['Vendor'] != "Jordan") & (df['Vendor'] != "Nike") ]
        # abandon_cart_data.drop_duplicates(subset="Secondary", keep=False, inplace=True)
        return abandon_cart_data


Cart_Data.abandon_cart_data()
