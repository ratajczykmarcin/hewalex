from datetime import datetime
from typing import Text
import requests
import json
import sys

#---------------do uzupełnienia
login_key = "aaaa"
id_controler = cccc
pass_instalator = dddd
#---------------------------

payload = {
  "submit_login" : 1,
  "data" : login_key
  }

payload_instalator = {
  "id" : 497,
  "pass": pass_instalator
  }

#sprawdzenie czy przy wywołaniu podana jest wartośc temepratury
if len(sys.argv) > 1:
    try:
        setTemperature = int(round(float(sys.argv[1])))
        
    except ValueError:
        
        setTemperature = 42
else:
    setTemperature = 42
    
#sprawdzenie zakresu
if 55 <= setTemperature <= 30:
	setTemperature = 42



try:
	s = requests.Session()

	login = s.post("https://ekontrol.pl/pl/login/", payload)
	checkLogin = json.loads(login.text)
	#print(checkLogin['response'])

	if checkLogin['response'] =="success":	
	
		instalator = s.post("https://ekontrol.pl/api/device/unlock-category/", payload_instalator)
		checkinstalator = json.loads(instalator.text)		
		#print("logowanie")
		#print(instalator.text)

		if checkinstalator['success'] == True:

			#--------------------------------walidacja
			#zmiana temperatury magazyn ciepła
			val = {"params[0][id]": 2880, "params[0][value]": setTemperature,  "cont": id_controler}
			validate = s.post("https://ekontrol.pl/pl/json/validate_params/", val)
			checkvalidate = json.loads(validate.text)		
			#print("validate")
			#print(validate.text)

			if checkvalidate['success'] == True:

				#-------------------------------porównanie 
				#zmiana temperatury magazyn ciepła
				par = {"params[0][id]": 2880, "params[0][value]": setTemperature,  "cont": id_controler}
				parse = s.post("https://ekontrol.pl/pl/json/parse_params/", par)
				checkparse = json.loads(parse.text)			
				#print("parse")
				#print(parse.text)

				if checkparse['success'] == True:

					#----------------------------------wysłanie parametru
					#zmiana temperatury magazyn ciepła
					doWyslania= {"params[0][key]": "reg_2880", "params[0][value]": setTemperature, "params[0][change]": 1,  "cont": id_controler}

					#print(doWyslania)
					ustaw = s.post("https://ekontrol.pl/pl/json/set_params/", doWyslania)
					ustawinstalator = json.loads(ustaw.text)
				
					if ustawinstalator['success'] == True:
						print("ok {0}".format(setTemperature))
					else:
						print("ERROR set {0}".format(setTemperature))		
				else:
					print("ERROR parse {0}".format(setTemperature))
			else:
				print("ERROR validate {0}".format(setTemperature))
		else:
			print("ERROR instalator {0}".format(setTemperature))


		logout = s.get("https://ekontrol.pl/pl/logoff/")	
		close = s.close		
	else:
		print("ERROR Login")
except:
	print("ERROR TRY")


