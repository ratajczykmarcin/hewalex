from datetime import datetime
import requests
import json


#---------------do uzupełnienia
login_key = "aaaa"
serial = bbbb
#---------------------------


payload = {
  "submit_login" : 1,
  "data" : login_key
  }

s = requests.Session()
try:
	login = s.post("https://ekontrol.pl/pl/login/", payload)
	checkLogin = json.loads(login.text)

	#print(checkLogin['response'])
	if checkLogin['response'] =="success":
		
		#to w sumie nie jest wykorzystane
		getdetails = s.get("https://ekontrol.pl/api/user/info")
		#print(getdetails.text)
		user = json.loads(getdetails.text)
		

		getdetails = s.get("https://ekontrol.pl/public/js/controllers_map/26_pl.js")
		#getdetails = s.get("https://ekontrol.pl/public/js/controllers_map/22_pl.js") - czasmi jest to 22_pl.js
		parameters = json.loads(getdetails.text)
		#print(parameters)

		getdetails = s.get("https://ekontrol.pl/api/device/values?serial={0}".format(serial))
		#print(getdetails.text)
		values = json.loads(getdetails.text)
		#print(values)

		getdetails = s.get("https://ekontrol.pl/api/device/ext-params?serial={0}".format(serial))
		#print(getdetails.text)
		extValue = json.loads(getdetails.text)
		controller_id = list(extValue.keys())[0]
		#print(controller_id)

		logout = s.get("https://ekontrol.pl/pl/logoff/")	
		close = s.close
		
		# Pobierz klucze (adresy parametrów) z drugiej listy 
		parameter_keys = values[controller_id].keys()

		# Iteruj przez wszystkie klucze
		for key in parameter_keys:
			# Pobierz wartość dla danego parametru
			parameter_value = values[controller_id][key]
			#print(parameter_value)

			# Pobierz numer parametru (adres) z klucza
			parameter_number = key[1:]  # Klucz jest postaci "pXXX", więc pobieramy numer XXX za pomocą slicingu
			#print(parameter_number)
			#print(parameters[parameter_number]['value'])

		
			if parameter_number in parameters:
				# Wpisz wartość do pierwszej listy
				parameters[parameter_number]['value'] = parameter_value

		new_parameters = {}
		for parameter_number, parameter in parameters.items():
			# Dodaj znak "p" do nazwy parametru
			parameter_name = f"p{parameter_number}"

			# Skopiuj parametr do nowej listy
			new_parameters[parameter_name] = parameter
						
		
		#jakieś pojedyncze wartości co nie występują w parametrach
		
		
		state = values.get(controller_id, {}).get('modem', None)
		new_parameters['modem'] = state
				
		state = values.get(controller_id, {}).get('state', None)
		new_parameters['state'] = state
				
		state = values.get(controller_id, {}).get('date_create', None)
		new_parameters['date_create'] = state		

		state = values.get(controller_id, {}).get('date_change', None)
		new_parameters['date_change'] = state		

		state = values.get(controller_id, {}).get('delay', None)
		new_parameters['delay'] = state	

		state = values.get(controller_id, {}).get('dt_when', None)
		new_parameters['dt_when'] = state	

		state = values.get(controller_id, {}).get('type_id', None)
		new_parameters['type_id'] = state

	
		#dodanie wartości z extValue
		for parameter_name, parameter in extValue[controller_id].items():
			
			# Skopiuj parametr do nowej listy
			new_parameters[parameter_name] = parameter
	
		json_data = json.dumps(new_parameters)
		print(json_data)
		
	else:
		print("ERROR LOGIN")
except:
	print("ERROR TRY")


