# Odczyt/zapis z serwera ekontrol dla pomp ciepła Hewalex.

<h2> Pliki python</h2>



<h3> - hewalex.py - odczyt parametów z serwera</h3>
<h3> - hewalex_magCiepla_on.py - ustawienie harmonogramu magazynu ciepła w danym dniu</h3>

  Program sprawdza dzień tygodnia i ustawia harmonogram magazynu dla całego dnia (wszystkie godziny.)

<h3> - hewalex_magCiepla_on.py - usunięcie harmonogramu magazynu ciepła</h3>

  Kasuje wszystkie ustawione godziny w harmonogramie.

<h3> - hewalex_set_2880.py - ustawienie temperatury dla magazynu ciepła</h3>

  Ustawia temperaturę dla magazynu ciepła. Wartość temperatury należy podać przy wywołaniu programu. Jak jej nie podamy ustawimy 42 stC.

# Ustawienia

aaaa - należy podać ciąg znaków logowania do ekontrol. Ciąg wygenerowany jest przez skrypty na stronie ekontrol.pl podczas logowania. Można go podejrzeć w przeglądarce w narzędziu dla developerów.  

bbbb - numer seryjny sterownika. Znajdziesz go w ekontrol.pl -> mój profil -> urządzenia -> sterowniki -> numer seryjny

cccc - Controller_ID - numer można odczytać w liście parametrów zwracanych przez serwer ekontrol. Więc najpierw skonfiguruj i uruchom hewalex.py.

<h2> Node-Red</h2>

<pre> </pre>
