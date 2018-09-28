from flask import Flask, request
import json
import requests
# from test_data import *

app = Flask(__name__)

#Global variable to use in multiple functions
URL = "http://gmapi.azurewebsites.net/"

#### Vehicle Information ####
@app.route("/vehicles/<int:vehicle_id>")
def vehicle_info(vehicle_id):
	"""This function returns the 'vehicles info' from getVehicleInfo GM's api"""
	url = "{}getVehicleInfoService".format(URL)
	response = requests.post(url, json={"id": str(vehicle_id), "responseType": "JSON"})
	gm_data = response.json()
	output = {}
	output["vin"] = gm_data["data"]["vin"]["value"]
	output["color"] = gm_data["data"]["color"]["value"]
	if gm_data["data"]["fourDoorSedan"]["value"] == "True":
		output["doorCount"] = 4
	else:
		output["doorCount"] = 2
	output["driveTrain"] = gm_data["data"]["driveTrain"]["value"]
	return json.dumps(output)

#### Security ####
@app.route("/vehicles/<int:vehicle_id>/doors")
def security_status(vehicle_id):
	"""Returns 'true/false' whether vehicle doors are locked or not"""
	url = "{}getSecurityStatusService".format(URL)
	response = requests.post(url, json={"id": str(vehicle_id), "responseType": "JSON"})
	gm_data = response.json()
	output = []
	data = gm_data["data"]["doors"]["values"]
	#Some vehicles might be a 4-door or 2-door
	for element in data:
		obj= {}
		obj["location"] = element["location"]["value"]
		obj["locked"] = element["locked"]["value"]
		obj["locked"] = bool(obj["locked"])
		output.append(obj)
	return json.dumps(output)

#### Fuel Range ####
@app.route("/vehicles/<int:vehicle_id>/fuel")
def fuel_range(vehicle_id):
	"""Returns the percentage of fuel"""
	url = "{}getEnergyService".format(URL)
	response = requests.post(url, json={"id": str(vehicle_id), "responseType": "JSON"})
	gm_data = response.json()
	output = {}
	if "tankLevel" not in gm_data["data"]:
		output["percent"] = None
	else:
		output["percent"] = gm_data["data"]["tankLevel"]["value"]
	return json.dumps(output)

#### Battery Range ####
@app.route("/vehicles/<int:vehicle_id>/battery")
def battery_range(vehicle_id):
	"""Returns the percentage of battery"""
	url = "{}getEnergyService".format(URL)
	response = requests.post(url, json={"id": str(vehicle_id), "responseType": "JSON"})
	gm_data = response.json()
	output = {}
	if "batteryLevel" not in gm_data["data"]:
		output["percent"] = None
	else:
		output["percent"] = gm_data["data"]["batteryLevel"]["value"]
	return json.dumps(output)

#### Start/Stop Engine ####
@app.route("/vehicles/<int:vehicle_id>/engine", methods=["POST"])
def vehicle_startstop_engine(vehicle_id):
	"""This function returns 'success' or 'error' (depending the command) from the actionEngineService"""
	url = "{}actionEngineService".format(URL)
	# print("type of request.json = {}".format(type(request.json)))
	# print("user has sent: {}".format(request.json))
	command = ""
	if request.json["action"] == "START":
		command = "START_VEHICLE"
	else:
		command = "STOP_VEHICLE"
	response = requests.post(url, json={"id": str(vehicle_id), "command": command, "responseType": "JSON"})
	gm_data = response.json()
	output = {}
	output["status"] = gm_data["actionResult"]["status"]
	if output["status"] == "EXECUTED":
		output["status"] = "success"
	else:
		output["status"] = "error"
	return json.dumps(output)
q
###################################

if __name__ == "__main__":
	#pass
	app.run(port=5000, host='0.0.0.0', debug=False)