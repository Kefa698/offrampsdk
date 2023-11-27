import requests
import json
from requests.auth import HTTPBasicAuth
from django.conf import settings





def get_access_token():
    client_id = settings.SAFARICOM_AUTH_KEY
    client_secret = settings.SAFARICOM_AUTH_CONSUMER_SECRET
    token_endpoint = settings.SAFARICOM_AUTH_ENDPOINT
    print(token_endpoint)
    params = {'grant_type': 'client_credentials'}
    try:
        res = requests.get(token_endpoint,auth=HTTPBasicAuth(client_id, client_secret), params=params, verify=True)
        response = json.loads(res.text)
        access_token = response['access_token']
        return access_token
    except KeyError:
        return False
    except Exception as error:
        print('TOKEN ERROR:', str(error))
        return False
    