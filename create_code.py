import requests
from credentials import *
class Create_Discount:
    def create_discounts(customer_name, once_per_customer = "true"):
        json_input = {
        "discount_code": {
        "code": customer_name
                         }
                     }
        post_url=f"https://{Authrization.API_KEY}:{Authrization.ADMIN_API}@{Authrization.STORE_URL}/api/{Authrization.API_VERSION}/price_rules/{Authrization.PRICE_RULE}/"
        print(post_url)
        requests.post(post_url+Authrization.END_POINT, json=json_input)
        return
 