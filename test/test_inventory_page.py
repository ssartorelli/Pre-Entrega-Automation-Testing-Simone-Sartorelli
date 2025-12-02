from page.login_page import LoginPage
from page.inventory_page import InventoryPage
import time

def test_inventory(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    login.open()
    login.login()
    time.sleep(5)
    inventory.is_at_page()
    inventory.logout()
    assert "https://www.saucedemo.com/" in driver.current_url
    time.sleep(5)