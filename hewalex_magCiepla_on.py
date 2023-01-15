from datetime import datetime
from typing import Text
import requests
import json
import datetime


#---------------do uzupełnienia
login_key = "aaaa"
id_controler = cccc
pass_instalator = dddd #standardowe hasło: 1305
#---------------------------

payload = {
  "submit_login" : 1,
  "data" : login_key
  }

payload_instalator = {
  "id" : 497,
  "pass": pass_instalator
  }

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

			#wstepnie wylacz magazyn ciepła
			doWyslania = {"params[0][key]": "reg_2879", "params[0][change]": 1, "params[1][key]": "reg_3088", "params[1][change]": 1, "params[2][key]": "reg_3089", "params[2][change]": 1, "cont": id_controler}
				
			weekday = datetime.datetime.today().weekday()
					
			#po-piąt
			if weekday in [0, 1, 2, 3, 4]:
				doWyslania = {"params[0][key]": "reg_2879", "params[0][value][]":  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], "params[0][change]": 1, "params[1][key]": "reg_3088", "params[1][change]": 1, "params[2][key]": "reg_3089", "params[2][change]": 1, "cont": id_controler}
			
			#sobota
			if weekday == 5:
				doWyslania = {"params[0][key]": "reg_2879", "params[0][change]": 1, "params[1][key]": "reg_3088", "params[1][value][]":  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], "params[1][change]": 1, "params[2][key]": "reg_3089", "params[2][change]": 1, "cont": id_controler}

			#niedziela
			if weekday == 6:
				doWyslania = {"params[0][key]": "reg_2879", "params[0][change]": 1, "params[1][key]": "reg_3088", "params[1][change]": 1, "params[2][key]": "reg_3089",  "params[2][value][]":  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], "params[2][change]": 1, "cont": id_controler}

			ustaw = s.post("https://ekontrol.pl/pl/json/set_params/", doWyslania)
			ustawinstalator = json.loads(ustaw.text)
			#print(doWyslania.text)
			#print("ustaw")
			#print(ustaw.text)

			if ustawinstalator['success'] == True:
				
				print("ok ON")

			else:
				print("ERROR SEND")
		else:
			print("ERROR LOGIN INSTALER")


		logout = s.get("https://ekontrol.pl/pl/logoff/")	
		close = s.close		
	else:
		print("ERROR LOGIN")
except:
	print("ERROR TRY")


