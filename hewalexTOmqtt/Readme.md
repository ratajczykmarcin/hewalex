# Odczyt/zapis z serwera ekontrol dla pomp ciepła Hewalex.

<h2> Pliki python</h2>



<h3> - hewalexTOmqtt.py - odczyt parametów z serwera</h3>

Plik umieść bezpośrednio w katalogu config w HA.Dla niektórych pomp parametry są wysyłane w 22_pl.js. Odpowiednio zedytuj plik. Lub sprawdź u siebie. Zerknij w screen jakSprawdzicParametry.png.

<pre>getdetails = s.get("https://ekontrol.pl/public/js/controllers_map/26_pl.js")
#getdetails = s.get("https://ekontrol.pl/public/js/controllers_map/22_pl.js")</pre>



# Ustawienia w plikach .py

aaaa - należy podać ciąg znaków logowania do ekontrol. Ciąg wygenerowany jest przez skrypty na stronie ekontrol.pl podczas logowania. Można go podejrzeć w przeglądarce w narzędziu dla developerów. Zobaczcie screeny.

bbbb - numer seryjny sterownika. Znajdziesz go w ekontrol.pl -> mój profil -> urządzenia -> sterowniki -> numer seryjny

eeee - username do brokera mqtt

ffff - hasło do brokera

<h3> - Wywołanie w HA </h3>

<pre>
sensor:
  - platform: command_line
    name: "Hewalex command line"
    command: "python3 /config/hewalexTOmqtt.py"
    scan_interval: 60
    unique_id: "hewalex_commandLine"
</pre>

<h3> - hewalex.yaml - plik yaml z konfiguracją sensorów MQTT w HA</h3>

W configuration.yaml dodaj 
<pre>mqtt: !include_dir_merge_named mqtt</pre>

Plik hewalex.yaml wrzuć do katalogu w HA o nazwie mqtt

