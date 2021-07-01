from rest_client import RestClient

class Config:
    def __init__(self,accountId, shareableKey, accessKey):
        self.shareableKey = shareableKey
        self.accountId = accountId
        self.accessKey = accessKey
        self.debug = False
        self.sandbox = False

class DevpayClient:
  def __init__(self, config):
    self.config = config
    self.restClient = RestClient(config)

  def confirmPayment(self, paymentDetails):
    response = self.restClient.providerAPIKeyResponse()
    providedKey = response.json()["provider_api_key"]

    token_resp = self.tokenize(providedKey, paymentDetails)
    paymentToken = token_resp["paymentToken"]
    paymentMethod = self.createPaymentMethod(paymentToken, paymentDetails)
    paymentIntent = self.createPaymentIntent(paymentMethod, paymentDetails)
    return paymentIntent

  def tokenize(self,providedKey, paymentDetails):
    response = self.restClient.tokenizedResponse(providedKey,paymentDetails)
    return response.json()

  def createPaymentMethod(self,paymentToken, paymentDetails):
    response = self.restClient.paymentMethodResponse(paymentToken,paymentDetails)
    return response.json()

  def createPaymentIntent(self,paymentMethod, paymentDetails):
    response = self.restClient.paymentIntentResponse(paymentMethod,paymentDetails)
    return response.json()