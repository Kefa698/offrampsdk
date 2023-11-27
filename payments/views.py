
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.api_auth import get_access_token
from django.conf import settings
from .serializers import MobileSerializer
import requests,json, uuid, base64,datetime

# Create your views here.
class ConvertToFiat(APIView):
    serializer_class = MobileSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        access_token = get_access_token()
        print("access token", access_token)
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {access_token}'
            }
        if not serializer.is_valid():
          return Response({"message":serializer.errors})
        amount = request.data.get('amount')
        mobile_number = request.data.get('mobile_number')
        initiator_password = str(settings.INITIATOR_PASSWORD)
        certificate = str(settings.SANDBOX_CERTIFICATE)
        security = initiator_password + certificate
        message = security.encode('ascii')
        credential = base64.b64encode(message)


        # serializer.save()

        # africastalking.initialize(settings.AFRICAS_TALKING_USERNAME,settings.AFRICAS_TALKING_API_KEY)
        # print({"afri_username":settings.AFRICAS_TALKING_USERNAME,"afri_key":settings.AFRICAS_TALKING_API_KEY})
        # sms = africastalking.SMS
        # recipient = ["+"+mobile_number]
        # sender = "M-MONEY"
        # message = "You have received kES"+amount

        payload = {    
            "OriginatorConversationID": str(uuid.uuid4()),
            "InitiatorName": settings.INITIATOR_NAME,
            "SecurityCredential":str(credential),
            "CommandID":settings.COMMANDID,
            "Amount":amount,
            "PartyA":"6579327",
            "PartyB":mobile_number,
            "Remarks":"here are my remarks",
            "QueueTimeOutURL":"https://smartnyumba.com",
            "ResultURL":"https://smartnyumba.com",
            "Occassion":"Christmas"
        }
        try:
            res = requests.post(settings.SAFARICOM_B2C_ENDPOINT,headers=headers,json=payload)
            print(res.text)
            #if(res.status==200):
                
            json_response = json.loads(res.text)
            return Response({"safaricom":json_response})
        except Exception as e:
            return Response({"error":e})
        # message = 'You shall receive'+amount+'KES'
        # sender_id = "254sms"
        # phone = mobile_number
        # api_key = settings.SMS_KEY
        # username = settings.SMS_USERNAME
        # sms_url = 'https://api.254sms.com/version1/sendsms'
        # header = {
        # 'Content-Type': 'application/json',
        # }
        # data = {
        #     'username':username,
        #     'api_key':api_key,
        #     'sender_id':sender_id,
        #     'phone':phone,
        #     'message':message
        # }
        # sms_response = requests.post(sms_url,headers=header,json=data)
        # print(sms_response)
        # if sms_response.status_code==200:
        #     return Response({"sms_sending":sms_response})
        # else:
        #     return Response({"sms_sending":sms_response})
class ConvertToCrypto(APIView):
    serializer_class = MobileSerializer
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if not serializer.is_valid():
          return Response({"message":serializer.errors})
        access_token = get_access_token()
        endpoint = settings.SAFARICOM_STK_PUSH
        Business_short_code = settings.BUSINESS_SHORT_CODE

        timestamp = f"{datetime.datetime.now():%Y%m%d%H%M%S}"

        

        pass_key = settings.SAFARICOM_PASS_KEY

        message = str(Business_short_code)+ pass_key + timestamp
        print("message",message)
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        password = base64_bytes.decode('ascii')

        print(password)

        print("pass key", pass_key)

        
        headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}'
        }
        amount = request.data.get('amount')
        mobile_number = request.data.get('mobile_number')

        print(headers)
        payload = {    
                    "BusinessShortCode": Business_short_code,    
                    "Password": password,    
                    "Timestamp": timestamp,    
                    "TransactionType": "CustomerPayBillOnline",    
                    "Amount": 10,    
                    "PartyA":mobile_number,    
                    "PartyB":174379,    
                    "PhoneNumber":mobile_number,    
                    "CallBackURL": "https://smartnyumba.com/apps/user/api/v1/services/mpesa-callback/",    
                    "AccountReference":"Test",    
                    "TransactionDesc":"Test"
                }
        response = requests.post(endpoint, json=payload, headers=headers)
        print(response.text)
        if response.status_code == 200:
            json_response = json.loads(response.text)
            # Service.MerchantRequestID = json_response['MerchantRequestID']
            # Service.CheckoutRequestID = json_response['CheckoutRequestID']

            # Service.save()

            return Response({
                'status': True,
                'message': 'Payment initiated'
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'status': False,
                'message': 'Check Keys!'
            }, status=status.HTTP_400_BAD_REQUEST)

