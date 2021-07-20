# Devpay Python SDK
A Python SDK for Devpay Payment Gateway Get your API Keys at https://devpay.io

<!-- LOGO -->
<a href="https://devpay.io/" target="_blank"><img align="left" width=200px src="https://devpay.io/wp-content/uploads/2021/07/Logo.png"></a>

<!-- BADGES -->
<div>

![GitHub followers](https://img.shields.io/github/followers/dev-pay?style=social)
![GitHub all releases](https://img.shields.io/github/downloads/dev-pay/python-sdk/total?style=plastic)
![GitHub last commit](https://img.shields.io/github/last-commit/dev-pay/python-sdk?style=plastic)
![GitHub](https://img.shields.io/github/license/dev-pay/python-sdk?style=plastic)
![GitHub language count](https://img.shields.io/github/languages/count/dev-pay/python-sdk?style=plastic)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/py?style=plastic)
![Maintenance](https://img.shields.io/maintenance/yes/2021?style=plastic)
![GitHub top language](https://img.shields.io/github/languages/top/dev-pay/python-sdk?style=plastic)
 
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
<!-- ROADMAP -->
## Please report any Issues

See the [open issues](https://github.com/dev-pay/node-js-sdk/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

<img align="right" width=200px src="https://bit.ly/2W1p9kD" alt="gif">

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request




<!-- CONTACT -->
## Connect with Devpay Inc <img src="https://bit.ly/2W1p9kD" width="60px" alt="handshake"/>
<a href="https://twitter.com/DevpayInc" target="_blank">
    <img src="https://bit.ly/3hQgnOJ" alt="twitter">
</a>
<a href="https://www.linkedin.com/showcase/devpay" target="_blank">
    <img src="https://bit.ly/3kBedoc" alt="linkedIN">
</a>
<a href="https://www.instagram.com/devpay/" target="_blank">
    <img src="https://bit.ly/2TrIXgc" alt="instagram">
</a>
<a href="https://devpay.io/" target="_blank">
    <img src="https://bit.ly/3rn81Bt" alt="website">
</a>

<!-- ACKNOWLEDGEMENTS -->
## Click Below for our API Documentation


<a href="https://docs.devpay.io/" target="_blank"><img align="left" width=300px src="https://bit.ly/2VUDkYB"></a>
