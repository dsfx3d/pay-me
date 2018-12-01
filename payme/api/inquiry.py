from urllib.parse import urljoin
import requests

from . import BaseApi



class InquiryApi(BaseApi):

    CHECK_MERCHANT_TXN_STATUS_ENDPOINT = 'payment/payment/chkMerchantTxnStatus'
    GET_PAYMENT_RESPONSE_ENDPOINT = 'payment/op/getPaymentResponse'



    def __assert_valid_args(self, auth_header, key, txn_ids):

        if type(txn_ids) == list or type(txn_ids) == set:
            assert len(txn_ids) <=50, 'maximum 50 txn ids allowed'

            txn_ids = '|'.join(txn_ids)

        assert type(txn_ids) == str, 'positional arg 1 (txn_ids) must be of type str, list or set'
        return txn_ids




    def __request_inquiry_endpoint(self, url, auth_header, key, txn_ids):
        txn_ids = self.__assert_valid_args(auth_header, key, txn_ids)
        params = dict(merchantKey=key, merchantTransactionIds=txn_ids)

        return self.__post_request_endpoint(url, auth_header, **params)




    def check_merchant_txn_status(self, auth_header, key, txn_ids):
        url = urljoin(self.BASE_URL, self.CHECK_MERCHANT_TXN_STATUS_ENDPOINT)
        return self.__request_inquiry_endpoint(url, auth_header, key, txn_ids)




    def get_payment_response(self, auth_header, key, txn_ids):
        url = urljoin(self.BASE_URL, self.GET_PAYMENT_RESPONSE_ENDPOINT)
        return self.__request_inquiry_endpoint(url, auth_header, key, txn_ids)