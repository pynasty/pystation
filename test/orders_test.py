import json
import unittest
import responses
import logging.config

from pystation.orders import ShipStationOrders
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
        self.orders = ShipStationOrders(None, None)

    @responses.activate
    def test_add_tag(self):

        def add_tag_callback(request):
            #   Can ignore headers and body in response for now, status is only important part
            payload = json.loads(request.body)
            if ('orderId' in payload and 
                'tagId' in payload and 
                 len(payload.keys()) == 2):

                return (200, '', '')
            else:
                return (400, '', '')

        responses.add_callback(
            responses.POST, 
            'https://ssapi.shipstation.com/Orders/AddTag',
            callback=add_tag_callback,
            content_type='application/json',
        )

        subject = self.orders.add_tag(orderId='123', tagId='456')
        self.assertTrue(subject)

        subject = self.orders.add_tag(orderId='123')
        self.assertFalse(subject)

        subject = self.orders.add_tag(tagId='123')
        self.assertFalse(subject)

        subject = self.orders.add_tag()
        self.assertFalse(subject)
    
    @responses.activate
    def test_create_label_for_order(self):
        def create_label_for_order_callback(request):
            #   Can ignore headers and body in response for now, status is only important part
            #   Not Full coverage, just will check for required fields for now
            payload = json.loads(request.body)
            if ('orderId' in payload and 
                'carrierCode' in payload and 
                'serviceCode' in payload and 
                'confirmation' in payload and 
                'shipDate' in payload and 
                'testLabel' in payload and 
                 len(payload.keys()) >= 6):

                return (200, '', '')
            else:
                return (400, '', '')

        responses.add_callback(
            responses.POST, 
            'https://ssapi.shipstation.com/Orders/CreateLabelForOrder',
            callback=create_label_for_order_callback,
            content_type='application/json',
        )

        subject = self.orders.create_label_for_order(
            orderId='123', carrierCode='USPS', serviceCode='123',
            confirmation=False, shipDate='s', testLabel=False)
        self.assertTrue(subject)

        subject = self.orders.create_label_for_order(
            carrierCode='USPS', serviceCode='123',
            confirmation=False, shipDate='s', testLabel=False)
        self.assertFalse(subject)

        subject = self.orders.create_label_for_order(
            orderId='123', serviceCode='123',
            confirmation=False, shipDate='s')
        self.assertFalse(subject)

        subject = self.orders.create_label_for_order(
            orderId='123', carrierCode='USPS', serviceCode='123',
            confirmation=False, testLabel=False)
        self.assertFalse(subject)

        subject = self.orders.create_label_for_order(
            orderId='123', carrierCode='USPS',
            confirmation=False, shipDate='s', testLabel=False)
        self.assertFalse(subject)

        subject = self.orders.create_label_for_order(
            orderId='123', carrierCode='USPS', serviceCode='123')
        self.assertFalse(subject)



    def test_create_order(self):
        pass

    def test_delete_order(self):
        pass

    def test_get_order(self):
        pass
        
    def test_hold_until(self):
        pass

    def test_list_orders(self):
        pass

    def test_list_orders_by_tag(self):
        pass

    def test_mark_order_as_shipped(self):
        pass

    def test_remove_tag(self):
        pass

if __name__ == '__main__':
    unittest.main()