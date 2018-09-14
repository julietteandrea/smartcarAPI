import unittest
import json
import requests

from test_data import *

import sys
#response.json was sending me an error. I created a function to try running response.json otherwise
#to let me know the cause of the error via response.content
def extract_json(response):
	try:
		return response.json()
	except json.decoder.JSONDecodeError:
		raise Exception("Unable to convert into JSON: {}",response.content)

class Testing(unittest.TestCase):

# 	def testingPrint(self):
# 		response = requests.get('http://localhost:5000/test')
# 		self.assertEqual(response.json(), {"hello":"world"})

# 	def test_echo(self):
# 		test_data = {"leeroy":"jenkifhffdffdns"}
# 		response = requests.post("http://localhost:5000/echo", json=test_data)
# 		self.assertEqual(response.json(), test_data)

	# def test_fuel(self):
	# 	expecting = {"fuel":30}
	# 	response = requests.get("http://localhost:5000/fuel")
	# 	self.assertEqual(response.json(), expecting)

# 	def test_id(self):
# 		url = "http://localhost:5000/test_id/1234"
# 		response = requests.get(url)
# 		self.assertEqual(response.json(), {"id":1234})


	def test_vehicle_info(self):
		for vehicle_id in VEHICLE_IDS:
			expecting = v_info[vehicle_id]
			response = requests.get("{}/vehicles/{}".format(URL, vehicle_id))
			self.assertEqual(extract_json(response), expecting)


	def test_fuel_range(self):
		for vehicle_id in VEHICLE_IDS:
			expecting = fuel_info[vehicle_id]
			response = requests.get("{}/vehicles/{}/fuel".format(URL, vehicle_id))
			self.assertEqual(extract_json(response), expecting)


	def test_battery_range(self):
		for vehicle_id in VEHICLE_IDS:
			expecting = battery_info[vehicle_id]
			response = requests.get("{}/vehicles/{}/battery".format(URL, vehicle_id))
			self.assertEqual(extract_json(response), expecting)

	def test_security(self):
		for vehicle_id in VEHICLE_IDS:
			expecting = security_info[vehicle_id]
			response = requests.get("{}/vehicles/{}/doors".format(URL, vehicle_id))
			self.assertEqual(extract_json(response), expecting)

	def test_startstop_engine(self):
		for vehicle_id in VEHICLE_IDS:
			response = requests.post("{}/vehicles/{}/engine".format(URL, vehicle_id), json=startstop_info[vehicle_id])
			self.assertEqual(extract_json(response), startstop_info[vehicle_id])

#############################

if __name__ == "__main__":
	unittest.main()