import json
import requests



class BaseApi:


    def __init__(self, base_url=None):
        self.BASE_URL = 'https://www.payumoney.com/'

        if not base_url is None:
            self.BASE_URL = base_url




    def __post_request_endpoint(self, url, auth, **params):

        headers = dict(authorization=auth)

        response = requests.post(url, data=params, headers=headers)
        return json.loads(response.content.decode('utf-8'))



    def __get_request_endpoint(self, url, auth, **params):

        headers = dict(authorization=auth)

        response = requests.get(url, params=params, headers=headers)
        return json.loads(response.content.decode('utf-8'))
