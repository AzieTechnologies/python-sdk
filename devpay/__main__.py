# Standard library imports
import sys
import json

# Devpay imports
import devpay_client
from devpay_client import DevpayClient
from devpay_client import Config

def main():
   paymentDetails = { "amount":132,
                "currency":"usd",
                "card":{"cardNum":"XXXX111111000000",
                        "cardExpiry":{"month":"10","year":"2024"},
                        "cvv":"321"},
                "billingAddress":{"country":"US",
                                    "zip":"38138",
                                    "state":"TN",
                                    "street":"123 ABC Lane",
                                    "city":"Memphis"}
               }

   config = Config(accountId="ACC_ID",
        shareableKey="SHAREABLE_KEY",
        accessKey="ACCESS_KEY");
#    config.debug = True
   config.sandbox = True
   devpayClient = DevpayClient(config)
   try:
     paymentIntent = devpayClient.confirmPayment(paymentDetails)
     print(json.dumps(paymentIntent, indent = 3))
   except Exception as e:
     print("Error - ",e)

if __name__ == "__main__":
    main()
