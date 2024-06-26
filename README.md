1 Inštalácia nástroja Selenium
Multiplatformový nástroj pre automatizované testovanie webových aplikácií https://www.seleniumhq.org/.

Stiahnuť a nainštalovať Selenium verziu kompatibilnú s aktuálnou verziou Python. V čase aktualizovania dokumentácie sme použili Selenium verziu 4.18.1 kompatibilnú s Python verziou 3.12.

Do príkazového riadku (cmd) zadať pre inštaláciu Selenium knižníc:

·       pip install -U selenium

2 Vyhľadávanie elementov pomocou selektorov
Na vyhľadanie a lokalizáciu elementov v aplikácií webovej stránky MKZBGIS v rámci testovacieho prostredia sme použili dva druhy selektorov – CSS a XPATH selector v prehliadačoch Microsoft Edge, Mozilla Firefox a Google Chrome. Pre každý typ prehliadača sú tieto selektory odlišné, nie je univerzálny pre všetky typy prehliadačov, špeciálne pre XPATH selector, pretože jeho identifikácia je možná dvomi spôsobmi: “Copy XPATH” alebo “Copy full XPATH”. Navyše, v rámci prehliadača Google Chrome identifikujeme každú akciu kombináciou vyššie uvedených selektorov.

Spomínané selektory sa javia ako najvhodnejšie z ponuky všetkých selektorov.

3 Postup vyhľadania elementov pomocou CSS a XPATH selektorov
Vo webovom prehliadači na požadovanej URL adrese po kliknutí pravým tlačidlom myši na vybraný element zvolíme možnosť „Preskúmať/Inspect“. Následne sa zobrazí HTML štruktúra vybraného elementu a po kliknutí pravým tlačidlom myši zvolíme možnosť „Kopírovať/Copy“ -> Copy XPATH/Full XPATH/CSS Selector

4         Python skript
4.1       Import balíkov, modulov a tried
Pre správne spustenie kódu a lokalizáciu elementov, je potrebné naimportovať požadované balíky, moduly a triedy – balík Selenium, modul webdriver a selenium.webdriver.common.by a triedu By (obrázok č. 2)

4.2       URL adresa
Pre testovacie scénare je potrebné vložiť presnú URL adresu, na ktorej sa bude testovať

URL - https://test-zbgis2023.skgeodesy.sk/mkzbgis-76ad218b-8807-4c9e-9697-e534b77197a9/sk/zakladna-mapa/login?pos=48.800000,19.530000,8

4.3       Premenné
Pre potreby testovania užívateľského prihlasovania, sme použili testovacie meno a heslo (obrázok č. 3).

4.4       Spustenie webdrivera
Slúži na inicializáciu požadovaného prehliadača pomocou Selenium webdriver a jeho presmerovanie na nami určenú URL adresu (obrázok č. 4)

4.5       Automatická navigácia kurzova myši na požadované tlačidlá
Nasledujúce akcie v skripte odkazujú na navigáciu kurzora na požadované tlačidlá v URL adrese s cieľom dosiahnuť požadovaný výsledok, t.j. každý pohyb kurzora musí byť zaznamenaný v kóde vrátane skopírovaného funkčného selektora (obrázok č. 5). Postup pri získania priameho odkazu na konkrétny selektor je zaznamenaný v sekcií 3.1. Ďalšie kroky v tejto sekcií Python skriptu sú principiálne rovnaké a nebudeme ich analyzovať.
