import logging
import requests



class InquiryApi:

    CHECK_MERCHANT_TXN_STATUS_ENDPOINT = 'payment/payment/chkMerchantTxnStatus'
    GET_PAYMENT_RESPONSE_ENDPOINT = 'payment/op/getPaymentResponse'


    def __init__(self, base_url=None):
        self.log = logging.getLogger('InquiryApi')

        self.BASE_URL = 'https://www.payumoney.com/'

        if not base_url is None:
            self.BASE_URL = base_url



    def __request_endpoint(self, url, key, txn_ids, auth_header):

        if type(txn_ids) == list or type(txn_ids) == set:
            assert len(txn_ids) <=50, 'maximum 50 txn ids allowed'

            txn_ids = '|'.join(txn_ids)

        assert type(txn_ids) == str, 'positional arg 1 (txn_ids) must be of type str, list or set'


        params = dict(merchantKey=key, merchantTransactionIds=txn_ids)
        headers = dict(authorization=auth_header)

        response = requests.post(url, data=params, headers=headers)
        return response.content





    def check_merchant_txn_status(self, auth_header, key, txn_ids):
        url = self.BASE_URL + self.CHECK_MERCHANT_TXN_STATUS_ENDPOINT
        return self.__request_endpoint(url, key, txn_ids, auth_header)


    def get_payment_response(self, auth_header, key, txn_ids):
        url = self.BASE_URL + self.GET_PAYMENT_RESPONSE_ENDPOINT
        return self.__request_endpoint(url, key, txn_ids, auth_header)