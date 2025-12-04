import pytest
from page.login_page import LoginPage
from page.inventory_page import InventoryPage
from page.cart_page import CartPage
from page.checkout_page import CheckoutPage
import time


def test_checkout_process(driver):
    """Verifica el proceso de checkout (flujo feliz) hasta el paso 2.

    Pasos:
    - Login con usuario estándar.
    - Añadir un producto al carrito y navegar al carrito.
    - Ir al checkout y comprobar que estamos en el primer paso.
    - Rellenar la información del cliente y continuar al overview (step two).
    - Verificar que la URL contiene `checkout-step-two`.
    """

    # Inicializar page objects
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    # Login
    login.open()
    login.login("standard_user", "secret_sauce")

    # Espera corta para que la UI cargue (mejor usar waits explícitos)
    time.sleep(4)

    # Agregar el primer producto y navegar al carrito
    inventory.add_product_to_cart(0)
    inventory.go_to_cart()
    time.sleep(4)

    # Ir al checkout
    cart.go_to_checkout()
    time.sleep(3)

    # Verificar que estamos en la página de checkout (step one)
    assert checkout.is_at_page()

    # Llenar información del cliente y continuar
    checkout.fill_customer_info("John", "Doe", "12345")
    checkout.continue_to_overview()

    # Comprobar que avanzamos al step two
    assert "checkout-step-two" in driver.current_url


def test_checkout_validation(driver):
    """Verifica validaciones del formulario de checkout (campos requeridos)."""

    # Inicializar page objects
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    # Login
    login.open()
    login.login("standard_user", "secret_sauce")

    time.sleep(4)

    # Añadir producto y navegar al checkout
    inventory.add_product_to_cart(0)
    inventory.go_to_cart()
    cart.go_to_checkout()

    # Intentar continuar sin completar la información del cliente
    checkout.continue_to_overview()

    # Comprobar que aparece el mensaje de error esperado
    error_message = checkout.get_error_message()
    assert "First Name is required" in error_message

    # Captura para debugging
    driver.save_screenshot("checkout_page.png")