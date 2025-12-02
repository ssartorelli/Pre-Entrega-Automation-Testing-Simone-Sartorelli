
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
URL = "https://www.saucedemo.com/"
#USERNAME = "standard_user"
#PASSWORD = "secret_sauce"

def get_driver():
    #options = Options()
    #options.add_argument("--start-maximized")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    #time.sleep(5)
    driver.implicitly_wait(5)
    return driver
    #driver = webdriver.Chrome(service=service, options=options)

def login_saucedemo(driver):
    
    driver.get(URL)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "user-name"))).send_keys(USERNAME)
    driver.find_element(By.NAME,"user-name").send_keys(USERNAME)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()
    #time.sleep(7)
    

def get_file_path(file_name, folder="data"):
#Ruta Relativa
    current_file = os.path.dirname(__file__) #EL ARCHIVO DONDE ESTOY
    file_path = os.path.join(current_file,"..",folder,file_name)

    #../data/data_login.csv=> rel
    return os.path.abspath(file_path)



