
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:

    URL_CURRENT = "/inventory.html"
    MENU_BUTTON= (By.ID, "react-burger-menu-btn")
    LINK_BUTTON = (By.ID, "logout_sidebar_link")
    ADD_TO_CART_BUTTONS = (By.XPATH, "//button[contains(text(), 'Add to cart')]")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver    

    def is_at_page(self):
        return self.URL_CURRENT in self.driver.current_url
    
    def logout(self):
        self.driver.find_element(*self.MENU_BUTTON).click()
        time.sleep(5)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.LINK_BUTTON))
    
    def add_product_to_cart(self, index=0):
        """Añade al carrito el producto por índice (0-based)."""
        # intentar obtener los botones de "Add to cart"
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
        if not buttons:
            # fallback: buscar botones dentro de items
            items = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
            if index < len(items):
                try:
                    btn = items[index].find_element(By.TAG_NAME, "button")
                    btn.click()
                except:
                    return
            return

        if index < len(buttons):
            buttons[index].click()

    def go_to_cart(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CART_LINK)).click()
        
