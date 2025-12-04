import pytest
from page.login_page import LoginPage
from page.inventory_page import InventoryPage
from page.cart_page import CartPage
import time


"""Tests relacionados con operaciones del carrito.

Contienen dos casos:
- `test_cart_operations`: añade un producto al carrito, verifica su presencia
  y luego continúa comprando.
- `test_remove_from_cart`: añade un producto, va al carrito y elimina un item,
  verificando que el contador decrece.
"""


def test_cart_operations(driver):
    """Verifica agregar un producto y volver a seguir comprando desde el carrito."""
    # Inicializar page objects
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    # Login con usuario estándar
    login.open()
    login.login("standard_user", "secret_sauce")

    # Espera corta; idealmente usar waits explícitos
    time.sleep(3)

    # Agregar el primer producto (índice 0) y navegar al carrito
    inventory.add_product_to_cart(0)
    inventory.go_to_cart()

    # Verificar que estamos en la página del carrito y que hay 1 item
    assert cart.is_at_page()
    assert cart.get_cart_items_count() == 1

    # Continuar comprando y verificar que volvemos al inventario
    cart.continue_shopping()
    assert inventory.is_at_page()


def test_remove_from_cart(driver):
    """Verifica que eliminar un item decrementa el contador del carrito."""
    # Inicializar page objects
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    # Login
    login.open()
    login.login("standard_user", "secret_sauce")
    time.sleep(3)

    # Agregar producto y navegar al carrito
    inventory.add_product_to_cart(0)
    inventory.go_to_cart()

    # Contar, eliminar y verificar que el número decrece en 1
    initial_count = cart.get_cart_items_count()
    cart.remove_item(0)

    assert cart.get_cart_items_count() == initial_count - 1

    # Captura de pantalla para debugging/manual review
    driver.save_screenshot("cart_page.png")