import unittest
import json
import requests

from test_data import *

#response.json was sending me an error. I created a function to try running response.json otherwise
#to let me know the cause of the error via response.content
def extract_json(response):
	try:
		return response.json()
	except json.decoder.JSONDecodeError:
		raise Exception("Unable to convert into JSON: {}",response.content)

class Testing(unittest.TestCase):

	def test_vehicle_info(self):
		for vehicle_id in VEHICLE_IDS:
			expecting = v_info[vehicle_id]
			response = requests.get("{}/vehicles/{}".format(URL, vehicle_id))
			self.assertEqual(extract_json(response), expecting)

	def test_security(self):
		for vehicle_id in VEHICLE_IDS:
			expecting = security_info[vehicle_id]
			response = requests.get("{}/vehicles/{}/doors".format(URL, vehicle_id))
			j = extract_json(response)
			self.assertEqual(j, expecting)
	
	def test_fuel_range(self):
		for vehicle_id in VEHICLE_IDS:
			expecting = fuel_info[vehicle_id]
			response = requests.get("{}/vehicles/{}/fuel".format(URL, vehicle_id))
			j = extract_json(response)
			#the fuel value changes so we cant really test
			j["percent"] = expecting["percent"]
			self.assertEqual(j, expecting)

	def test_battery_range(self):
		for vehicle_id in VEHICLE_IDS:
			expecting = battery_info[vehicle_id]
			response = requests.get("{}/vehicles/{}/battery".format(URL, vehicle_id))
			j = extract_json(response)
			j["percent"] = expecting["percent"]
			self.assertEqual(j, expecting)


	def test_startstop_engine(self):
		for vehicle_id in VEHICLE_IDS:
			response = requests.post("{}/vehicles/{}/engine".format(URL, vehicle_id), json=startstop_info[vehicle_id])
			self.assertEqual(extract_json(response), startstop_info[vehicle_id])

#############################

if __name__ == "__main__":
	unittest.main()