import logging
logger = logging.getLogger(__name__)

from urllib import parse

from pystation.connection import ShipstationAPI

class ShipStationShipments(ShipstationAPI):

    def list_shipments(self, **kwargs):
        params = parse.urlencode(kwargs)        
        return self.base_get('/Shipments?' + params)
    
    def create_label(self, **kwargs):
        return self.base_post(kwargs, '/Shipments/CreateLabel',
            status_codes={200, 201, 204})
    
    def get_rates(self, **kwargs):
        return self.base_post(kwargs, '/Shipments/GetRates',
            status_codes={200, 201, 204})

    def void_label(self, **kwargs):
        return self.base_post(kwargs, '/Shipments/VoidLabel',
            status_codes={200, 201, 204})
