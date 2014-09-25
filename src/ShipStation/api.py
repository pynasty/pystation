import json

class ShipStationAPI(object):
	#	TODO: Add ShipStation API Access params here
	def __init__(self):
		#	TODO: Connect to ShipStation here
		pass

	#	TODO: General ShipStation access methods will go here


class JSONWrapper(object):
	def __init__(self, json_text):
		try:
			self.i_ds = json.JSONDecoder().decode(json_text)
		except:
			self.i_ds = None

	def to_string(self):
		"""
		Convert Item to JSON string

		:return:
			A String representation of the JSON internal data structure
		"""
		if self.i_ds != None:
			return json.JSONEncoder().encode(self.i_ds)
		else:
			return ''

	def _safe_get_element(self, path):
		"""
		Get a Child element in the JSON data structure
 
		:param path:
			String path ('TODO: String example here')

		:return:
			Element or None
		"""

		#	This is all wrong, JSON is more than just a key value pair thing, it has a hierarchy and needs to be treated as parent child relationship ...

		if self.i_ds == None: return None

		elements = path.split('.')
		d = None

		for e in elements:
			d = self.i_ds[e]

		return d

	def _safe_get_element_text(self, path):
		"""
		Get an element as a String
		
		:param path:
			String path ('TODO: String example here')

		:return:
			String or None

		"""
		e = self._safe_get_element(path)

		if e is not None:
			return e.to_string()
		else:
			return ''







