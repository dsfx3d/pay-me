from hashlib import sha512




class Hasher:
    
    LIVE_ENDPOINT = 'https://secure.payu.in/_payment'
    TEST_ENDPOINT = 'https://sandboxsecure.payu.in/_payment'
    REQUIRED_HASH_SEQUENCE = 'txnid|amount|productinfo|firstname|email'
    OPTIONAL_HASH_SEQUENCE ='udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10'





    def __init__(self, key, salt):
        self.key = key
        self.salt = salt





    def generate_hash(self, data):
        # request hash formula is:
        # sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
        assert type(data) == dict, 'arg `data` must be a dict'

        # add key        
        hash_str = f'{self.key}|'
        
        # add required values
        try:
            data['amount'] = str(float(data['amount']))
            hash_str += '|'.join([data[k] for k in self.REQUIRED_HASH_SEQUENCE.split('|')])
        except KeyError as e:
            raise Exception(f'key {e} missing from arg data')
        
        hash_str += '|'

        # add user defined values
        hash_str += '|'.join([data.get(k, '') for k in self.OPTIONAL_HASH_SEQUENCE.split('|')])
        # add salt
        hash_str += f'|{self.salt}'
        
        hashh = hash_str.encode('utf-8')
        return sha512(hashh).hexdigest().lower()





    def check_hash(self, data):
        # response hash formula is:
        # sha512(additionalCharges|SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
        assert type(data) == dict, 'arg `data` must be a dict'

        # extract hash keys
        required_hash_keys = reversed(self.REQUIRED_HASH_SEQUENCE.split('|'))
        optional_hash_keys = reversed(self.OPTIONAL_HASH_SEQUENCE.split('|'))
        hash_str = ''
        
        # add additional charges only if applied
        if data.get('additionalCharges'):            
            ad_charges = data.get('additionalCharges')
            hash_str += f'{ad_charges}|'
        
        try:
            # add salt
            hash_str += self.salt
            # add status
            hash_str += f'|{data["status"]}|'
            # add user defined values
            hash_str += '|'.join([data.get(key, '') for key in optional_hash_keys])

            hash_str += '|'

            # add required values
            hash_str += '|'.join([str(data[key]) for key in required_hash_keys])
        except KeyError as e:
            raise Exception(f'key {e} missing from arg data')
        
        # add key
        hash_str += f'|{self.key}'
        
        hashh = hash_str.encode('utf-8')
        return (sha512(hashh).hexdigest().lower() == data.get('hash'))