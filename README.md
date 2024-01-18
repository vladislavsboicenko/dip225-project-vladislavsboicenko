## Projekts_Vladislavs Boičenko_231RDB387

### Paziņojums
Pirms programmas izmantošanas lūdzu, ievādiet savus datus "data" vietā, "user_data.csv" failā. "Study Program" kolonna vajag pilnīgi ievadiet studiju programmu, piemēram: Datorsistēmas (RDBD0).

### Projekta apraksts
**Izveidot automatizētu programmu ar tādām funkcijām kā:**
  1) Automātiska "ORTUS" tīmekļa (ortus.rtu.lv) atvēršana, atbilstoši studenta datiem (lietotājvārds, parole). E-studiju nodāļa automātiska atvēršana.

  2) Automātiska "Nodarbību grafiki" tīmekļa (nodarbibas.rtu.lv) atvēršana, atbilstoši studenta datiem (studiju programma, kurss, grupa).

**Programmā tiek izmantota Python bibliotēka Selenium.**
  - Bibliotēka tiek izmantota, lai veiktu automatizācijas uzdevumus interneta pārlūkā.
  - No bibliotēkas tiek importēti moduļi:
    ```
        - "webdriver", lai darboties ar dažādiem klasem un interneta pārlūkiem;
        - "Service", lai vadīt interneta pārlūku;
        - "By", lai meklētu elementus interneta pārlūkā;
        - "Keys", lai vadītu datora tastatūras taustiņus;
        - "time", lai veikt darbības ar laiku.
    ```
### Programmas apraksts
  - Tiek izmantotas "service" un "webdriver", lai darboties ar Chrome, automātiski atvērot to pēc programmas startēšanas un maksimālo Chrome izmēru.
    ```
    service = Service()
    option = webdriver.ChromeOptions()
    option.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=option)
    ```
    Ir izmantots input() un driver.quit(), lai aizvērtu Chrome pēc kaut kādu ievadē.

  - Tiek izmantota metodē "with open", lai atvērtu un lasītu informāciju no faila "user_data.csv". Ir izmantota universāla simbolu kodēšana "utf-8", kas ļauj pareizi lasīt informacīju atbilstoši vālodai.
    ```
    with open("user_data.csv", "r", encoding="utf-8") as file:
    next(file)
    for line in file:
        row=line.rstrip().split(",")
    ```
    - Tiek izmantoti mainīgie atbilstoši datiem no "user_data.csv".
      ```
      **piemērs:** login = row[1]
      ```
  - Tiek izmantota `driver.get()` metode, lai saņemtu atsauce un darboties ar to. Ir izmantots `time.sleep(2)`, lai gaidīt 2 sekundes.
    ```
    url = "https://id2.rtu.lv/openam/UI/Login?module=LDAP&locale=lv"
    driver.get(url)
    ```
  - Ir izmantota "find" metode, lai atrāst un ievadīt elementus, nospiežot datora tastatūras taustiņus, un dzēst elementus.
    ```
    find=driver.find_element(By.) (ID/CLASS_NAME/XPATH/NAME/LINK_TEXT)
    find.click()
    find.clear()
    find.send_keys()
    find.send_keys(Keys.)
    ```
  - Ir izmantots "while True" metode, lai ievadiet funkcijas numuru un izvadīt paziņojumu "error" nepareizas ievades gadījumā.






