from urllib.parse import urljoin
import requests

from . import BaseApi


class RefundApi(BaseApi):

    REFUND_PAYMENT_ENDPOINT = 'treasury/merchant/refundPayment'
    REFUND_DETAILS_BY_REFUND_ID_ENDPOINT = 'treasury/ext/merchant/getRefundDetails'
    REFUND_DETAILS_BY_PAYMENT_ID_ENDPOINT = 'treasury/ext/merchant/getRefundDetailsByPayment'




    def init_refund_payment(self, auth_header, key, payment_id, refund_amount):
        url = urljoin(self.BASE_URL, self.REFUND_PAYMENT_ENDPOINT)
        
        params = dict(merchantKey=key, paymentId=payment_id, refundAmount=refund_amount)
        return self.__post_request_endpoint(url, auth_header, **params)




    def get_refund_details_by_refund_id(self, auth_header, key, refund_id):
        url = urljoin(self.BASE_URL, self.REFUND_DETAILS_BY_REFUND_ID_ENDPOINT)
        
        params = dict(merchantKey=key, refundId=refund_id)
        return self.__get_request_endpoint(url, auth_header, **params)




    def get_refund_details_by_payment_id(self, auth_header, key, payment_id):
        url = urljoin(self.BASE_URL, self.REFUND_DETAILS_BY_PAYMENT_ID_ENDPOINT)
        
        params = dict(merchantKey=key, paymentId=payment_id)
        return self.__get_request_endpoint(url, auth_header, **params)