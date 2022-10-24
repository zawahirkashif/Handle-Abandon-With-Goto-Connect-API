import time
from check_abandon import *
from create_code import *
from send_sms import *
def send_message_data():
    customer_data = Cart_Data.abandon_cart_data()
    customer_data = customer_data[customer_data['Secondary'].notna() | customer_data['Primary']]
    complete_data = customer_data.replace(to_replace ='[\+, ,\(,\),-]', value = '', regex = True)
    complete_data_number = complete_data.replace(to_replace ='(^1)', value = '', regex = True)
    print(complete_data_number)
   
    for name, market, email, primary, secondary, vendor in complete_data_number.itertuples(index=False):
        sms_body = '''Wait, Don't Go..!! \nGet an Additional 15% Discount on Your Entire Order. Add “{0}15” Promo Code to Avail This Offer. Hurry Up This Is a Limited Time Offer
        '''.format(name.upper())
        Create_Discount.create_discounts("{0}15".format(name.upper()))
        primary_phone = '+1{0}'.format(primary)
        secondary_phone = '+1{0}'.format(secondary)
        if primary is None:
            print("Send_SMS_Primary")
            Send_SMS.send_text_message('+17739319991',sms_body)
            print(primary_phone)
            # Send_SMS.send_text_message(primary_phone,sms_body)
        else:
            print("Send_SMS_Secondary")
            Send_SMS.send_text_message('+17738376666',sms_body)
            print(secondary_phone)
            # Send_SMS.send_text_message(secondary_phone,sms_body)
        time.sleep(5)

send_message_data()