

URL = "http://localhost:5000"
VEHICLE_IDS = [1234, 1235]

v_info = {}
v_info[1234] = {"vin": "123123412412",
						"color": "Metallic Silver",
						"doorCount": 4,
						"driveTrain": "v8"}

v_info[1235] = {"vin": "1235AZ91XP",
						"color": "Forest Green",
						"doorCount": 2,
						"driveTrain": "electric"}


security_info = {}
security_info[1234] = [
						{"location": "backLeft",
							"Locked": True},
						{"location": "frontRight",
							"locked": False},
						{"location": "frontLeft",
							"locked": False},
						{"location": "backRight",
							"locked": True}
						]

security_info[1235] = [
						{"location": "frontLeft",
							"locked": False},
						{"location": "frontRight",
							"locked": True}
							]
fuel_info = {}
fuel_info[1234] = {"percent": 79.37}
fuel_info[1235] = {"percent": 0}

battery_info = {}
battery_info[1234] = {"percent": 0}
battery_info[1235] = {"percent": 74.04}


startstop_info = {}
startstop_info[1234] = {"status": "EXECUTED"}
startstop_info[1235] = {"status": "FAILED"}

					