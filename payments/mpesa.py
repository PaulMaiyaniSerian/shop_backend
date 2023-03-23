import requests
import json
import base64
from datetime import datetime
from requests.auth import HTTPBasicAuth


CONSUMER_KEY = "xAGwUb1La3WeHYmODRv4MZMOOLajptSD"
CONSUMER_SECRET = "8O5PycxMJcCEy8A3"

def get_access_token():
    url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
   
    response = requests.get(url, auth=HTTPBasicAuth(CONSUMER_KEY, CONSUMER_SECRET))

    return  json.loads(response.text)["access_token"]


def stk_push(phone, amount):
    url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    businessShortCode = "174379"
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    transaction_type = "CustomerPayBillOnline"


    passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
    data_to_encode = businessShortCode + passkey + timestamp

    
    online_password = base64.b64encode(data_to_encode.encode())
    decode_password = online_password.decode('utf-8')

    access_token = get_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}

    data = {
        "BusinessShortCode": businessShortCode,
        "Password": decode_password,
        "Timestamp": timestamp,
        "TransactionType": transaction_type,
        "Amount": amount,
        "PartyA": phone,
        "PartyB": businessShortCode,
        "PhoneNumber": phone,
        "CallBackURL": "https://535c-196-110-41-101.in.ngrok.io/payments/api/mpesa/pay/webhook",
        "AccountReference": "Paul Serian Shop backend",
        "TransactionDesc": "Payment to pauls shop"
    }
    print(data)
    response = requests.post(url, json=data, headers=headers)
    print(response.text)