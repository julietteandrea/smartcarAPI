from flask import Flask, request
import json
import requests
# from test_data import *


app = Flask(__name__)

#Global var to use in each function
URL = "http://gmapi.azurewebsites.net/"

"""Vehicle Info"""
@app.route("/vehicles/<int:vehicle_id>")
def vehicle_info(vehicle_id):
	"""This function returns the the 'vehicles info' from getVehicleInfo GM's api"""
	url = "{}getVehicleInfoService".format(URL)
	response = requests.post(url, json={"id": str(vehicle_id), "responseType": "JSON"})
	j = response.json()
	#created a new dict to only hold the data needed, neatly.
	output = {}
	output["vin"] = j["data"]["vin"]["value"]
	output["color"] = j["data"]["color"]["value"]
	if j["data"]["fourDoorSedan"]["value"] == "True":
		output["doorCount"] = 4
	else:
		output["doorCount"] = 2
	output["driveTrain"] = j["data"]["driveTrain"]["value"]
	return json.dumps(output)

"""Fuel Range"""
@app.route("/vehicles/<int:vehicle_id>/fuel")
def vehicle_fuel(vehicle_id):
	"""This function returns the {"fuel":%} from the getEnergyService GM's api"""
	url = "{}getEnergyService".format(URL)
	response = requests.post(url, json={"id": str(vehicle_id), "responseType": "JSON"})
	j = response.json()
	output = {}
	if "tankLevel" not in j["data"]:
		#In the case that the vehicle is an electric
		output["percent"] = "null"
	else:
		output["percent"] = j["data"]["tankLevel"]["value"]
	return json.dumps(output)


"""Battery Range"""
@app.route("/vehicles/<int:vehicle_id>/battery")
def vehicle_battery(vehicle_id):
	"""This function returns the {"batterylevel":%} from the getEnergyService GM's api"""
	url = "{}getEnergyService".format(URL)
	response = requests.post(url, json={"id": str(vehicle_id), "responseType": "JSON"})
	j = response.json()
	output = {}
	if "batteryLevel" not in j["data"]:
		#In the case that the vehicle isn't an electric
		output["percent"] = "null"
	else:
		output["percent"] = j["data"]["batteryLevel"]["value"]
	return json.dumps(output)

"""Security"""
@app.route("/vehicles/<int:vehicle_id>/doors")
def vehicle_security(vehicle_id):
	"""The function returns 'true or false' from the getSecurityStatusService if doors are locked from GM's api"""
	url = "{}getSecurityStatusService".format(URL)
	response = requests.post(url, json={"id": str(vehicle_id), "responseType": "JSON"})
	j = response.json()
	output = []
	data = j["data"]["doors"]["values"]
	#Some vehicles might be a 4-door or 2-door
	for element in data:
		print("element = {}".format(element))
		obj= {}
		obj["location"] = element["location"]["value"]
		obj["locked"] = element["locked"]["value"]
		obj["locked"] = bool(obj["locked"])
		output.append(obj)
	return json.dumps(output)

"""Start/Stop Engine"""
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
	j = response.json()
	output = {}
	output["status"] = j["actionResult"]["status"]
	if output["status"] == "EXECUTED":
		output["status"] = "success"
	else:
		output["status"] = "error"
	return json.dumps(output)

###################################

if __name__ == "__main__":
	#pass
	app.run(port=5000, host='0.0.0.0', debug=False)