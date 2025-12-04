from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


"""Page object para la página del carrito.

Contiene los localizadores y acciones para interactuar con la página del
carrito (verificar presencia, navegar a checkout, continuar comprando,
contar items, eliminar items y leer el badge del carrito).
"""


class CartPage:
    # Ruta esperada para identificar que estamos en la página del carrito
    URL_CURRENT = '/cart.html'

    # Localizadores principales
    CHECKOUT_BUTTON = (By.ID, 'checkout')  # botón para iniciar el checkout
    CONTINUE_SHOPPING_BUTTON = (By.ID, 'continue-shopping')  # volver al inventario
    CART_ITEM = (By.CLASS_NAME, 'cart_item')  # elemento que representa un item en el carrito
    REMOVE_BUTTON = (By.XPATH, "//button[contains(text(), 'Remove')]")  # botón Remove junto a cada item
    CART_BADGE = (By.CLASS_NAME, 'shopping_cart_badge')  # badge con la cantidad de items en el header

    def __init__(self, driver):
        # WebDriver provisto por fixture
        self.driver = driver

    def is_at_page(self):
        """Devuelve True si la URL actual corresponde a la página del carrito."""
        return self.URL_CURRENT in self.driver.current_url

    def go_to_checkout(self):
        """Haz click en el botón de Checkout esperando que sea clickable."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        ).click()

    def continue_shopping(self):
        """Haz click en 'Continue Shopping' para volver al inventario."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CONTINUE_SHOPPING_BUTTON)
        ).click()

    def get_cart_items_count(self):
        """Devuelve el número de elementos actualmente listados en el carrito."""
        items = self.driver.find_elements(*self.CART_ITEM)
        return len(items)

    def remove_item(self, item_index=0):
        """Elimina un item del carrito por índice (0-based).

        Busca todos los botones 'Remove' y hace click en el que corresponde al
        índice solicitado si existe.
        """
        remove_buttons = self.driver.find_elements(*self.REMOVE_BUTTON)
        if remove_buttons and item_index < len(remove_buttons):
            remove_buttons[item_index].click()

    def get_cart_badge_count(self):
        """Lee el texto del badge del carrito y lo devuelve como int.

        Si no existe el badge (por ejemplo carrito vacío), devuelve 0.
        """
        try:
            badge = self.driver.find_element(*self.CART_BADGE)
            return int(badge.text)
        except Exception:
            return 0