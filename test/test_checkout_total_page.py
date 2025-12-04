import pytest
from page.login_page import LoginPage
from page.inventory_page import InventoryPage
from page.cart_page import CartPage
from page.checkout_page import CheckoutPage
from page.checkout_total_page import CheckoutCompletePage
import time


def test_complete_purchase_flow(driver):
    """Test del flujo completo de compra (simplificado).

    Flujo cubierto:
    1. Login con usuario estándar.
    2. Añadir un producto al carrito y navegar al carrito.
    3. Ir al proceso de checkout, rellenar datos y continuar.
    4. Comprobar la pantalla de 'checkout complete' (aquí simulada usando
       `driver.get` para evitar dependencia del paso overview).
    5. Verificar mensajes/elementos de éxito y volver al inventario.

    Nota: El test simula la navegación final a `checkout-complete.html` con
    `driver.get` porque la página de overview y el botón final no están
    automatizados en este ejemplo. En una suite real, reemplazar por el
    flujo real desde overview -> finish.
    """

    # Inicializar page objects
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)
    complete = CheckoutCompletePage(driver)

    # 1) Login
    login.open()
    login.login("standard_user", "secret_sauce")

    # Espera corta para asegurar que la UI responde (mejor usar waits explícitos)
    time.sleep(4)

    # 2) Agregar producto al carrito y navegar al carrito
    inventory.add_product_to_cart(0)
    inventory.go_to_cart()

    # 3) Ir a checkout desde el carrito
    cart.go_to_checkout()

    # 4) Rellenar información del cliente y continuar
    checkout.fill_customer_info("John", "Doe", "12345")
    checkout.continue_to_overview()

    # 5) Simular finalización de la compra: navegar a la página de checkout completo
    # (se usa driver.get aquí por simplicidad en el ejemplo)
    driver.get("https://www.saucedemo.com/checkout-complete.html")

    # Verificaciones de la página de completado
    assert complete.is_at_page()
    assert "Thank you for your order!" in complete.get_success_message()
    assert complete.is_success_image_displayed()

    # Volver a la página principal/inventario y comprobar estado
    complete.back_to_home()
    assert inventory.is_at_page()

    # Captura para debugging/manual review
    driver.save_screenshot("checkout_complete_page.png")