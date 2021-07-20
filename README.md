# Devpay Python SDK
A Python SDK for Devpay Payment Gateway Get your API Keys at https://devpay.io

<!-- LOGO -->
 <a href="https://devpay.io/" target="_blank"><img align="right" width=200px height=200px src="./Read me Assets/dev pay - logo.png" alt="Project logo"></a>

<!-- BADGES -->
<div>

![GitHub followers](https://img.shields.io/github/followers/dev-pay?style=social)
![GitHub](https://img.shields.io/github/license/dev-pay/python-sdk?style=plastic)
![GitHub contributors](https://img.shields.io/github/contributors/dev-pay/ios-sdk?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/dev-pay/ios-sdk?style=for-the-badge)
![GitHub Repo stars](https://img.shields.io/github/stars/dev-pay/ios-sdk?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues-raw/dev-pay/ios-sdk?style=for-the-badge)
[![MIT License][license-shield]](#)
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
</div>

## Integration
```
pip install git+https://github.com/dev-pay/node-js-sdk.git

```

## Usage
```python
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
