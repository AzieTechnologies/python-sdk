import requests
import logging

API_ENDPOINTS = {
                'SANDBOX': {
                    'PAYSAFE': 'https://hosted.test.paysafe.com',
                },
                'PROD': {
                    'PAYSAFE': 'https://hosted.paysafe.com',
                },
                'DEVPAY':"https://api.devpay.io"
            }

class RestClient:
    def __init__(self, config):
        self.config = config

        if config.debug:
            logging.basicConfig(level=logging.INFO)

    def apiEndPoint(self, service):
        server = 'PROD'
        if self.config.sandbox:
            server = 'SANDBOX'
        return API_ENDPOINTS[server][service]

    def providerAPIKeyResponse(self):

        uri = API_ENDPOINTS['DEVPAY']
        uri = uri+'/v1/general.svc/paysafe/api-key'
        logging.info("Reqeust - POST - %s ",uri)

        requestDetails = {
                "DevpayId":self.config.accountId,
                "token":self.config.accessKey
        }
        if self.config.sandbox:
            requestDetails["env"] = "sandbox"

        payload = {
                "RequestDetails":requestDetails
        }

        response = requests.post(uri,
            json=payload,
            headers={"Content-Type":"application/json", 'User-Agent': 'dev-pay client'}
            )
        logging.info("Response - %s",response.text)
        return response

    def tokenizedResponse(self, providedKey,obj):
        uri = self.apiEndPoint('PAYSAFE')
        uri = uri+'/js/api/v1/tokenize'
        
        logging.info("Reqeust - POST - %s, Data - %s ",uri,str(obj))

        response = requests.post(uri,
            json=obj,
            headers={"X-Paysafe-Credentials":"Basic "+providedKey,
                        "Content-Type":"application/json"}
            )
        logging.info("Response - %s",response.text)
        return response

    def paymentMethodResponse(self, paymentToken,paymentDetail):
        paymentMethodInfo = {
            "payment_token":paymentToken,
            "type":"card",
            "billing_details":{
                "amount":paymentDetail["amount"],
                "currency":paymentDetail["currency"],
                "address":paymentDetail["billingAddress"]
            }
        }

        requestDetails = {
                "DevpayId":self.config.accountId,
                "token":self.config.accessKey
        }
        if self.config.sandbox:
            requestDetails["env"] = "sandbox"

        payload = {
                "PaymentMethodInfo":paymentMethodInfo,
                "RequestDetails":requestDetails
        }

        uri = API_ENDPOINTS['DEVPAY']
        uri = uri+'/v1/paymentmethods/create'
        logging.info("Reqeust - POST - %s, Data - %s ",uri,str(payload))


        response = requests.post(uri,
            json=payload,
            headers={"Content-Type":"application/json", 'User-Agent': 'dev-pay client'}
            )
        logging.info("Response - %s",response.text)
        return response

    def paymentIntentResponse(self,paymentMethod, paymentDetail):
        
        paymentIntentsInfo = {
                "amount":paymentDetail["amount"],
                "type":"card",
                "currency":paymentDetail["currency"],
                "capture_method":"automatic",
                "payment_method_types":["card"],
                "payment_method_id":paymentMethod["id"],
                "confirm":True,
                "metaData":paymentDetail.get("metaData",{})
        }

        requestDetails = {
                "DevpayId":self.config.accountId,
                "token":self.config.accessKey
        }
        if self.config.sandbox:
            requestDetails["env"] = "sandbox"

        payload = {
                "PaymentIntentsInfo":paymentIntentsInfo,
                "RequestDetails":requestDetails
        }
        
        uri = API_ENDPOINTS['DEVPAY']
        uri = uri+"/v1/general/paymentintent"
        logging.info("Reqeust - POST - %s, Data - %s ",uri,str(payload))
        # Added custom User-Agent to avoid 403 HTTP error
        response = requests.post(uri,
            json=payload,
            headers={"Content-Type":"application/json",
                'User-Agent': 'dev-pay client',
            })
        logging.info("Response - %s",response.text)
        return response