import requests
from django.conf import settings

def send_sms_via_smsc(phone_number, message):
    url = "https://smsc.kz/sys/send.php"
    params = {
        "login": settings.SMSC_LOGIN,
        "psw": settings.SMSC_PASSWORD,
        "phones": phone_number,
        "mes": message,
        "sender": settings.SMSC_SENDER,
        "fmt": 3,
    }
    response = requests.get(url, params=params)
    print(response.json())  
    return response.json()
