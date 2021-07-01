import requests
import logging

API_ENDPOINTS = {
                'SANDBOX': {
                    'PAYSAFE': 'https://hosted.test.paysafe.com',
                    'DEVPAY': 'https://sandbox-api.tilled.com'
                },
                'PROD': {
                    'PAYSAFE': 'https://hosted.paysafe.com',
                    'DEVPAY': 'https://api.tilled.com',
                }
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

        uri = self.apiEndPoint('DEVPAY')
        uri = uri+'/v1/payment-providers/paysafe/api-key'
        logging.info("Reqeust - GET - %s ",uri)
        response = requests.get(uri,
            headers={"Authorization":"Bearer "+self.config.shareableKey,
                        "Content-Type":"application/json",
                        "Tilled-Account":self.config.accountId}
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
        payload = {
            "payment_token":paymentToken,
            "type":"card",
            "billing_details":{
                "amount":paymentDetail["amount"],
                "currency":paymentDetail["currency"],
                "address":paymentDetail["billingAddress"]
            }
        }
        uri = self.apiEndPoint('DEVPAY')
        uri = uri+'/v1/payment-methods'
        logging.info("Reqeust - POST - %s, Data - %s ",uri,str(payload))

        response = requests.post(uri,
            json=payload,
            headers={"Authorization":"Bearer "+self.config.shareableKey,
                        "Content-Type":"application/json",
                        "Tilled-Account":self.config.accountId}
            )
        logging.info("Response - %s",response.text)
        return response

    def paymentIntentResponse(self, paymentMethod,paymentDetail):
        payload = {
                "amount":paymentDetail["amount"],
                "type":"card",
                "currency":paymentDetail["currency"],
                "capture_method":"automatic",
                "payment_method_types":["card"],
                "payment_method_id":paymentMethod["id"],
                "confirm":True,
                "metaData":paymentDetail.get("metaData",{})
        }
        
        uri = self.apiEndPoint('DEVPAY')
        uri = uri+'/v1/payment-intents'
        logging.info("Reqeust - POST - %s, Data - %s ",uri,str(payload))
        response = requests.post(uri,
            json=payload,
            headers={"Authorization":"Bearer "+self.config.accessKey,
                        "Content-Type":"application/json",
                        "Tilled-Account":self.config.accountId}
            )
        logging.info("Response - %s",response.text)
        return response
