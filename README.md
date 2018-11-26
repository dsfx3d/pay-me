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

```python
payu_key    # merchant key from PayU Merchant Dashboard
payu_salt`` # merchant salt from PayU Merchant Dashboard

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

---

Goto PayUMoney Developer Docs (https://developer.payumoney.com/redirect/) for detailed documentation and to understand utility of this package