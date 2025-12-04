
"""Helper utilities para tests.

Contiene helpers para obtener un WebDriver (`get_driver`), realizar
login rápido en SauceDemo (`login_saucedemo`) y obtener rutas absolutas a
archivos de datos (`get_file_path`).
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# URL y credenciales de prueba (utilizadas por los helpers)
URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


def get_driver():
    """Crea y devuelve una instancia de `webdriver.Chrome`.

    - Usa `webdriver-manager` para instalar/obtener el chromedriver adecuado.
    - Devuelve el driver con `implicitly_wait(5)` configurado.

    Nota: se dejaron opciones comentadas para permitir añadir flags
    (ej. `--start-maximized`) si se quiere ejecutar en modo headless u
    con otras configuraciones.
    """
    # Opciones de Chrome (descomentarlas para personalizar)
    # options = Options()
    # options.add_argument("--start-maximized")

    # Instalar/obtener el binario del driver y crear el servicio
    service = Service(ChromeDriverManager().install())

    # Crear el WebDriver
    driver = webdriver.Chrome(service=service)

    # Espera implícita para elementos (reduce flakiness en tests simples)
    driver.implicitly_wait(5)
    return driver
    # Alternativa con options: webdriver.Chrome(service=service, options=options)


def login_saucedemo(driver):
    """Realiza login en SauceDemo usando las credenciales por defecto.

    Este helper navega a `URL`, espera que el campo de usuario sea clickable
    y rellena los inputs. Se hace click en el botón de login.

    Observación: en el código actual el envío del `USERNAME` aparece dos veces
    (una a través de WebDriverWait().send_keys y otra con find_element().send_keys).
    Se mantiene así para no alterar el comportamiento existente, aunque
    en condiciones normales bastaría con una sola llamada.
    """
    driver.get(URL)

    # Esperar hasta que el input de usuario sea clickable y enviar usuario
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "user-name"))
    ).send_keys(USERNAME)

    # Nota: envío redundante del username (preservado del código original)
    driver.find_element(By.NAME, "user-name").send_keys(USERNAME)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()


def get_file_path(file_name, folder="data"):
    """Construye y devuelve la ruta absoluta a un archivo dentro de la carpeta `data`.

    - `file_name`: nombre del fichero (ej: `data_login.csv`).
    - `folder`: carpeta donde buscar (por defecto `data`).

    La función calcula la ruta relativa desde la carpeta `utils` y la devuelve
    como ruta absoluta para ser consumida por los tests.
    """
    # Ruta relativa al directorio actual del módulo
    current_file = os.path.dirname(__file__)
    file_path = os.path.join(current_file, "..", folder, file_name)

    # Devolver la ruta absoluta
    return os.path.abspath(file_path)



