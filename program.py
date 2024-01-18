import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

service = Service()
option = webdriver.ChromeOptions()
option.add_argument("--start-maximized")

def ortus():
    driver = webdriver.Chrome(service=service, options=option)
    with open("user_data.csv", "r", encoding="utf-8") as file:
        next(file)
        for line in file:
            row=line.rstrip().split(",") 
            login = row[1]
            password = row[2]

    url = "https://id2.rtu.lv/openam/UI/Login?module=LDAP&locale=lv"
    driver.get(url)
    time.sleep(2)

    find=driver.find_element(By.ID, "IDToken1")
    find.clear()
    find.send_keys(login)

    find=driver.find_element(By.ID, "IDToken2")
    find.clear()
    find.send_keys(password)

    find=driver.find_element(By.NAME, "Login.Submit")
    find.click()

    find=driver.find_element(By.LINK_TEXT, "Studentiem")
    find.click()

    input()
    driver.quit()

def nodarbibas():
    driver = webdriver.Chrome(service=service, options=option)
    with open("user_data.csv", "r", encoding="utf-8") as file:
        next(file)
        for line in file:
            row=line.rstrip().split(",") 
            study_program = row[3]
            course = row[4]
            group = row[5]

    url = "https://nodarbibas.rtu.lv/"
    driver.get(url)
    time.sleep(2)

    find=driver.find_element(By.CLASS_NAME, "filter-option")
    find.click()

    find=driver.find_element(By.XPATH, '//input[@class="form-control"]')
    find.send_keys(study_program)
    find.send_keys(Keys.ENTER)

    find=driver.find_element(By.ID, "course-id")
    find.send_keys(course)

    find=driver.find_element(By.ID, "group-id")
    find.send_keys(group)

    input()
    driver.quit()

while True:
    function = input("\nSelect 1 or 2\n\n1 - ortus.rtu.lv\n2 - nodarbibas.rtu.lv\n\n")

    if function == "1":
        ortus()
        break
    elif function == "2":
        nodarbibas()
        break
    else:
        print("\nerror")

