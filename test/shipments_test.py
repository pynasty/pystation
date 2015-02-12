import re
import json
import unittest
import responses
import logging.config

from urllib import parse

from pystation.shipments import ShipStationShipments
from pystation.connection import request

debug_logging_config = {
    'version' : 1,
    'disable_existing_loggers' : False,
    'formatters' : {
        'standard' : {
            'format' : '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level':'INFO',    
            'class':'logging.FileHandler',
            'filename' : 'order_tests.log'
        },  
    },
    'loggers': {
        'pystation': {
            'handlers': ['default'],
            'level': 'INFO',  
            'propagate': True  
        },
    }
}

logging.config.dictConfig(debug_logging_config)


class ShipStationOrdersTest(unittest.TestCase):

    def setUp(self):
        self.shipments = ShipStationShipments(None, None)

    @responses.activate
    def test_list_shipments(self):

        def list_shipments_callback(request):
            accepted_params = {
                'recipientName',
                'recipientCountryCode',
                'orderNumber',
                'orderId',
                'carrierCode',
                'serviceCode',
                'trackingNumber',
                'shipDateStart',
                'shipDateEnd',
                'voidDateStart',
                'voidDateEnd',
                'includeShipmentItems',
                'page',
                'pageSize',
            }

            parsed_url = parse.urlparse(request.url)
            params = parse.parse_qs(parsed_url.query)

            for param in params.keys():
                if not param in accepted_params:
                    return (400, '', '')

            return (200, '', '{"code" : 200}')


        url_re = re.compile(r'https?://ssapi.shipstation.com/Shipments?.*')
        responses.add_callback(
            responses.GET, 
            url_re,
            callback=list_shipments_callback,
            content_type='application/json',
        )

        subject = self.shipments.list_shipments()
        self.assertTrue(subject)

        subject = self.shipments.list_shipments(recipientName='name')
        self.assertTrue(subject)

        subject = self.shipments.list_shipments(recipientName='name', orderId='a')
        self.assertTrue(subject)

        subject = self.shipments.list_shipments(recipientName='name', orderId='a', page=5)
        self.assertTrue(subject)

        subject = self.shipments.list_shipments(non='name')
        self.assertFalse(subject)
    

    @responses.activate
    def test_create_label(self):
        pass

    @responses.activate
    def test_get_rates(self):
        pass

    @responses.activate
    def test_void_label(self):
        pass     

if __name__ == '__main__':
    unittest.main()