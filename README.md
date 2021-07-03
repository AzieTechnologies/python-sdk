# Devpay Python SDK
A Python SDK for Devpay Payment Gateway Get your API Keys at https://devpay.io


## Integration
```
pip install git+https://github.com/dev-pay/node-js-sdk.git

```

## Usage
```
   paymentDetails = { "amount":<amount>,
                "currency":"usd",
                "card":{"cardNum":"XXXX111111000000",
                        "cardExpiry":{"month":"MM","year":"YYYY"},
                        "cvv":"321"},
                "billingAddress":{"country":"US",
                                    "zip":"38138",
                                    "state":"TN",
                                    "street":"stree",
                                    "city":"city"}
               }

   config = Config(accountId="ACC_ID",
        shareableKey="SHAREABLE_KEY",
        accessKey="ACCESS_KEY");
#  config.debug = True
   config.sandbox = True
   devpayClient = DevpayClient(config)
   try:
     paymentIntent = devpayClient.confirmPayment(paymentDetails)
     print(json.dumps(paymentIntent, indent = 3))
   except Exception as e:
     print("Error - ",e)

```
