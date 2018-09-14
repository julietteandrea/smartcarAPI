from flask import Flask, request
import json
from test_data import *


app = Flask(__name__)


# @app.route("/test")
# def testing():
# 	print(request.json)
# 	return json.dumps({"hello":"world"})

# @app.route("/echo", methods=["POST"])
# def testing2():
# 	print("request.json is")
# 	print(request.json)
# 	json_input = request.json
# 	return json.dumps(json_input)


# @app.route("/fuel", methods=["GET"])
# def fuel():
# 	return json.dumps({"fuel":30})

# @app.route("/test_id/<int:vehicle_id>", methods=["GET"])
# def test_id(vehicle_id):
# 	return json.dumps({"id":vehicle_id})

def is_valid_vehicle(vehicle_id):
	return vehicle_id in [1234, 1235]



"""Vehicle Info"""
@app.route("/vehicles/<int:vehicle_id>")
def vehicle_info(vehicle_id):
	return json.dumps(v_info[vehicle_id])

"""Fuel Range"""
@app.route("/vehicles/<int:vehicle_id>/fuel")
def vehicle_fuel(vehicle_id):
	return json.dumps(fuel_info[vehicle_id])

"""Battery Range"""
@app.route("/vehicles/<int:vehicle_id>/battery")
def vehicle_battery(vehicle_id):
	return json.dumps(battery_info[vehicle_id])

"""Security"""
@app.route("/vehicles/<int:vehicle_id>/doors")
def vehicle_security(vehicle_id):
	return json.dumps(security_info[vehicle_id])

"""Start/Stop Engine"""
@app.route("/vehicles/<int:vehicle_id>/engine", methods=["POST"])
def vehicle_startstop_engine(vehicle_id):
	print(request.json)
	json_input = request.json
	return json.dumps(json_input)

###################################

if __name__ == "__main__":
	#pass
	app.run(port=5000, host='0.0.0.0', debug=True)