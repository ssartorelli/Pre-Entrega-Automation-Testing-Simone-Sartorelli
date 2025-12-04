"""Page object para la página de login (saucedemo).

Contiene los localizadores y acciones para abrir la página y realizar el login
utilizando las credenciales provistas en `utils.helpers`.
"""

from utils.helpers import URL, PASSWORD, USERNAME
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage:
    # Localizadores para los campos y botón de la página de login
    _INPUT_NAME = (By.NAME, "user-name")        # campo de nombre de usuario
    _INPUT_PASSWORD = (By.NAME, "password")     # campo de contraseña
    _LOGIN_BUTTON = (By.NAME, "login-button")   # botón de inicio de sesión

    def __init__(self, driver):
        # WebDriver provisto por el fixture de pytest
        self.driver = driver

    def open(self):
        """Navega a la URL base definida en `utils.helpers`.

        Se asume que `URL` apunta a la página de login (ej: https://www.saucedemo.com).
        """
        self.driver.get(URL)

    def login(self, username=USERNAME, password=PASSWORD):
        """Rellena los campos de usuario y contraseña y hace click en Login.

        Args:
            username (str): nombre de usuario a utilizar. Por defecto viene de `utils.helpers`.
            password (str): contraseña a utilizar. Por defecto viene de `utils.helpers`.

        Comportamiento:
        - Espera hasta que cada elemento sea clickable antes de interactuar, para
          evitar errores por elementos no renderizados aún.
        - Envía el texto a los inputs y finalmente hace click en el botón de login.
        """
        # Espera y escribe el nombre de usuario
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self._INPUT_NAME)
        ).send_keys(username)

        # Espera y escribe la contraseña
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self._INPUT_PASSWORD)
        ).send_keys(password)

        # Espera y hace click en el botón de login
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self._LOGIN_BUTTON)
        ).click()
