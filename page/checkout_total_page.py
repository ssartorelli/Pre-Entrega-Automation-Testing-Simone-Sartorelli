from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


"""Page object para la pantalla final del checkout (Checkout Complete).

Expone métodos para verificar que estamos en la página correcta, leer los
mensajes de éxito, volver al home y comprobar si la imagen de confirmación
está visible.
"""


class CheckoutCompletePage:
    # URL que identifica la pantalla de checkout completado
    URL_CURRENT = '/checkout-complete.html'

    # Localizadores
    SUCCESS_MESSAGE = (By.CLASS_NAME, 'complete-header')  # encabezado de éxito
    SUCCESS_TEXT = (By.CLASS_NAME, 'complete-text')       # texto descriptivo de éxito
    BACK_HOME_BUTTON = (By.ID, 'back-to-products')        # botón para volver al inventario
    PONY_EXPRESS_IMAGE = (By.CLASS_NAME, 'pony_express')  # imagen decorativa de confirmación

    def __init__(self, driver):
        # WebDriver provisto por fixtures
        self.driver = driver

    def is_at_page(self):
        """Devuelve True si la URL actual corresponde a la página de checkout completo."""
        return self.URL_CURRENT in self.driver.current_url

    def get_success_message(self):
        """Devuelve el texto del encabezado de éxito si está presente, sino string vacío."""
        try:
            return self.driver.find_element(*self.SUCCESS_MESSAGE).text
        except Exception:
            return ""

    def get_success_text(self):
        """Devuelve el texto descriptivo de confirmación si está presente."""
        try:
            return self.driver.find_element(*self.SUCCESS_TEXT).text
        except Exception:
            return ""

    def back_to_home(self):
        """Hace click en el botón 'Back Home' esperando que sea clickable."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.BACK_HOME_BUTTON)
        ).click()

    def is_success_image_displayed(self):
        """Comprueba si la imagen de éxito está mostrada (devuelve bool)."""
        try:
            return self.driver.find_element(*self.PONY_EXPRESS_IMAGE).is_displayed()
        except Exception:
            return False