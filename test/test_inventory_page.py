from page.login_page import LoginPage
from page.inventory_page import InventoryPage
import time


def test_inventory(driver):
    """Test de la página de inventario.

    Flujo:
    1. Crear objetos page para Login e Inventory.
    2. Abrir la página de login y realizar login con credenciales por defecto.
    3. Esperar unos segundos para que la página cargue (se puede reemplazar
       por esperas explícitas más específicas si se desea).
    4. Verificar que estamos en la página de inventario y luego hacer logout.
    5. Comprobar que la URL final corresponde a la página principal (logout correcto)
    6. Guardar una captura para debugging.
    """

    # Crear page objects
    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    # Abrir la página de login y realizar el login con credenciales por defecto
    login.open()
    login.login()

    # Pequeña espera para evitar flakiness; idealmente usar esperas explícitas
    time.sleep(5)

    # Comprobar que la página de inventario está cargada
    inventory.is_at_page()

    # Cerrar sesión usando el menú de la página de inventario
    inventory.logout()

    # Verificar que tras el logout volvemos a la URL base de saucedemo
    assert "https://www.saucedemo.com/" in driver.current_url

    # Espera final y captura de pantalla para debugging/manual review
    time.sleep(5)
    driver.save_screenshot("inventory_page.png")