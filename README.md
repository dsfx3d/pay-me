# :moneybag: payme

**payme** is collection of utilities for PayUMoney redirection based payment gateway integration. It includes a _`hasher`_ module to generate request hash when requesting payments and to check response hash recieved after payment transaction completion.

## Installation

```python
pip install payme
```

## Usage

```python
from payme.hashers import Hasher
```

## Example

### 1. module `hasher`

This module contains the class required to generate hash while making payment request to payu gateway via redirection. Same class also contain method to check hash recieved from payu payment gateway after payment request is processed and gateway redirects to requestee.

```python
payu_key    # merchant key from PayU Merchant Dashboard
payu_salt   # merchant salt from PayU Merchant Dashboard

hasher = Hasher(payu_key, payu_salt)


# data to be posted to PayU Gateway transaction request endpoint
# required keys
request_data = {
    'txnid':            'unique_id',
    'amount':           99,
    'productinfo':      'this is a product',
    'firstname':        'John',
    'email':            'johnsnow@example.com'
}


# you may also include upto 10 optional user difined fields
# example
request_data.update({
    'udf1': 'udf1',
    'udf2': 'udf2',
    'udf3': 'udf3',
    'udf4': 'udf4',
    'udf5': 'udf5',
    'udf6': 'udf6',
    'udf7': 'udf7',
    'udf8': 'udf8',
    'udf9': 'udf9',
    'udf10': 'udf10',
})


# hash string to be posted along request_data
request_hash = hasher.generate_hash(request_data)


# post data recived on success url after PayU Gateway redirection
response_data


# true if data is valid else false
hasher.check_hash(response_data)
```

### 2. `api` package

#### 2.1 module `inquiry`

This module contains class for making requests to payu payment inquiry api

```python
PAYU_KEY                                # merchant key from payu dashboard
PAYU_AUTH_HEADER                        # auth header from payu dashboard

TXN_ID  = '123xxx'                      # merchant txnid passed while making payment
TXN_IDS = ('54xxx', '133xxx')           # multiple merchant txnids



inquiry_api = inquiry.InquiryApi()

# returns status dict; check payu api reference for returned dict keys
payment_status_dict = inquiry_api.check_merchant_txn_status(PAYU_AUTH_HEADER, PAYU_KEY, TXN_ID)
# returns status dict; check payu api reference for returned dict keys
multiple_payments_status_dict = inquiry_api.check_merchant_txn_status(PAYU_AUTH_HEADER, PAYU_KEY, TXN_IDS)


# returns complete payment response details of transactions; check payu api reference for returned dict keys
payment_res_dict = inquiry_api.get_payment_response(PAYU_AUTH_HEADER, PAYU_KEY, TXN_ID)
multiple_payments_res_dict = inquiry_api.get_payment_response(PAYU_AUTH_HEADER, PAYU_KEY, TXN_IDS)
```

#### 2.2 module `refund`

This module contains class for making requests to payu payment refund api

```python
PAYU_KEY                                # merchant key from payu dashboard
PAYU_AUTH_HEADER                        # auth header from payu dashboard

PAYMENT_ID                              # payu payment id
REFUND_AMOUNT                           #



refund_api = refund.RefundApi()


# initiate refund process; check payu api reference for response dict keys
response = refund_api.init_refund_payment(PAYU_AUTH_HEADER, PAYU_KEY, PAYMENT_ID, REFUND_AMOUNT)

# if refund initiated
refund_id = response.get('result')


# get refund process details; check payu api reference for returned dict keys
refund_api.get_refund_details_by_refund_id(PAYU_AUTH_HEADER, PAYU_KEY, refund_id)
# or you can use
refund_api.get_refund_details_by_payment_id(PAYU_AUTH_HEADER, PAYU_KEY, PAYMENT_ID)

```

---

Goto PayU Money Developer Docs (https://developer.payumoney.com/redirect/) for detailed documentation and to understand utility of `hasher` module

Goto PayU Money Developer Docs (https://www.payumoney.com/dev-guide/apireference.html) for detailed documentation and to understand utility of `api` package
