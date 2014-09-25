import unittest
from ShipStation.api import JSONWrapper

class TestJSONWrapper(unittest.TestCase):

	"""
		Methods to Test
	"""
	s0 = None
	s1 = '[{"display": "JavaScript Tutorial","url": "http://www.w3schools.com/js/default.asp"},{"display": "HTML Tutorial","url": "http://www.w3schools.com/html/default.asp"},{"display": "CSS Tutorial","url": "http://www.w3schools.com/css/default.asp""}]'
	s2 = '{"employees":[{"firstName":"John", "lastName":"Doe"}, {"firstName":"Anna", "lastName":"Smith"}, {"firstName":"Peter", "lastName":"Jones"}]}'
	s3 = '{"glossary": {"title": "example glossary","GlossDiv": {"title": "S","GlossList": {"GlossEntry": {"ID": "SGML","SortAs": "SGML","GlossTerm": "Standard Generalized Markup Language","Acronym": "SGML","Abbrev": "ISO 8879:1986","GlossDef": {"para": "A meta-markup language, used to create markup languages such as DocBook.","GlossSeeAlso": ["GML", "XML"]},"GlossSee": "markup"}}}}}'
	

	def test_to_string(self):

		"""
		Testing the Null Case
		"""

		subject = JSONWrapper(self.s0)
		self.assertEqual('', subject.to_string())

		"""
		Other test cases are wierd, json elements order gets changed, this test not too important, skip for now
		"""

	def test_safe_get_element(self):

		"""
		Testing the Null Case
		"""

		subject = JSONWrapper(self.s0)
		self.assertEqual(None, subject._safe_get_element('irrelevent'))

		"""
		Simple Test Case
		"""
		subject = JSONWrapper(self.s1)
		self.assertEqual(None, subject._safe_get_element(""))

	def test_safe_get_element_text(self):
	
		"""
		Testing the Null Case
		"""

		subject = JSONWrapper(self.s0)
		self.assertEqual('', subject._safe_get_element_text('irrelevent'))

if __name__ == '__main__':
    unittest.main()