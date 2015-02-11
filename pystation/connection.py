import logging
logger = logging.getLogger(__name__)

from requests import HTTPError

import requests
import json

base_url = 'https://shipstation.p.mashape.com'

def request(method, url, **kwargs):
    res = requests.request(method, url, **kwargs)
    res.connection.close()

    return res

class APIResult(object):
    def __init__(self, message, success, response):
        self.success = success
        self.message = message
        self.response = response

class ShipstaionAPI(object):
    def __init__(self, api_user, api_secret, mashape_key):
        self.api_user = api_user
        self.api_secret = api_secret
        self.mashape_key = mashape_key

    def api_call(self, url, method, valid_codes, **kwargs):
        try:
            headers = kwargs.get('headers', {})
            headers['X-Mashape-Key'] = self.mashape_key
            headers['Content-Type'] = 'application/json'
            kwargs['headers'] = headers

            res = request(method, url, auth=(self.api_user, self.api_secret), **kwargs)
            if res.status_code not in valid_codes:
                result = APIResult('Status code check failed for code {}'
                        .format(res.status_code),
                        False, 
                        res
                )
            else:
                result = APIResult(None, True, res)

        except HTTPError as e:
            result = APIResult('Exception thrown:{}'.format(e), False, None)

        return result

    def base_put(self, data, end, status_codes={201, 204}):
        api_res = self.api_call(base_url + 
            end, 'PUT', status_codes, data=json.dumps(data))

        if not api_res.success:
            logger.warning('PUT Failed for endpoint %s with message %s \n' +
                        'and content %s for payload %s', api_res.response.url, 
                        api_res.message, api_res.response.text, json.dumps(data))

        return api_res.success

    def base_post(self, data, end, status_codes={201, 204}):
        api_res = self.api_call(base_url + 
            end, 'POST', status_codes, data=json.dumps(data))

        if not api_res.success:
            logger.warning('PUT Failed for endpoint %s with message %s \n' +
                        'and content %s for payload %s', api_res.response.url, 
                        api_res.message, api_res.response.text, json.dumps(data))

        return api_res.success

    def base_get(self, end, status_codes={200}):
        api_res = self.api_call(base_url + end, 'GET', status_codes)

        if api_res.success:
            res = api_res.response.json()
            return res
        else:
            logger.warning('GET Failed for endpoint %s with message: %s',
                api_res.response.url, api_res.message)

        return None