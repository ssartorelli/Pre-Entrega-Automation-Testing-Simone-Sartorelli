from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


"""Page object para la página de Checkout (paso 1).

Provee métodos para rellenar la información del cliente, continuar al
overview, cancelar el checkout y leer mensajes de error.
"""


class CheckoutPage:
    # Localizadores para los campos del formulario y botones
    FIRST_NAME_INPUT = (By.ID, 'first-name')
    LAST_NAME_INPUT = (By.ID, 'last-name')
    POSTAL_CODE_INPUT = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')
    CANCEL_BUTTON = (By.ID, 'cancel')
    ERROR_MESSAGE = (By.CLASS_NAME, 'error-message-container')

    def __init__(self, driver):
        # WebDriver provisto por fixtures
        self.driver = driver

    def is_at_page(self):
        """Comprueba que la URL actual corresponde al primer paso del checkout."""
        return '/checkout-step-one.html' in self.driver.current_url

    def fill_customer_info(self, first_name, last_name, postal_code):
        """Rellena los campos de información del cliente.

        Espera explícitamente a que el primer campo sea clickable antes de
        interactuar para reducir flakiness en tests.
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FIRST_NAME_INPUT)
        ).send_keys(first_name)

        # Rellenar el resto de campos sin waits explícitos adicionales
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE_INPUT).send_keys(postal_code)

    def continue_to_overview(self):
        """Hace click en Continue para ir al checkout overview."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        ).click()

    def cancel_checkout(self):
        """Cancela el proceso de checkout y vuelve al paso anterior/página.
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CANCEL_BUTTON)
        ).click()

    def get_error_message(self):
        """Devuelve el texto del mensaje de error si está presente, sino string vacío."""
        try:
            error_element = self.driver.find_element(*self.ERROR_MESSAGE)
            return error_element.text
        except Exception:
            return ""