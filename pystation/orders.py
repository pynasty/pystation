import logging
logger = logging.getLogger(__name__)

from urllib import parse

from pystation.connection import ShipstationAPI

class ShipStationOrders(ShipstationAPI):

    def add_tag(self, **kwargs):
        return self.base_post(kwargs, '/Orders/AddTag', status_codes={200})

    def create_label_for_order(self, **kwargs):
        return self.base_post(kwargs, '/Orders/CreateLabelForOrder', 
            status_codes={200, 201, 204})

    def create_order(self, **kwargs):
        return self.base_post(kwargs, '/Orders/CreateOrder',
            status_codes={200, 201, 204})

    def delete_order(self):
        pass

    def get_order(self, order_id):
        return self.base_get('/Orders/' + order_id)
        
    def hold_until(self, **kwargs):
        return self.base_post(kwargs, '/Orders/HoldUntil',
            status_codes={200, 201, 204})

    def list_orders(self, **kwargs):
        params = parse.urlencode(kwargs)
        return self.base_get('/Orders/List?' + params)

    def list_orders_by_tag(self, **kwargs):
        params = parse.urlencode(kwargs)
        return self.base_get('/Orders/ListByTag?' + params)

    def mark_order_as_shipped(self, **kwargs):
        return self.base_post(kwargs, '/Orders/MarkAsShipped',
            status_codes={200, 201, 204})

    def remove_tag(self, **kwargs):
        return self.base_post(kwargs, '/Orders/RemoveTag',
            status_codes={200, 201, 204})