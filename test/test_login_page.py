import pytest
from page.login_page import LoginPage
from data.data_login import CASOS_LOGIN
from utils.example_csv import get_login_csv, get_login_json
from utils.faker import get_login_faker


@pytest.mark.parametrize("username,password,login_bool", get_login_faker())
def test_login_page(driver, username, password, login_bool):
    """Prueba parametrizada de la página de login.

    - `get_login_faker()` provee tuplas (username, password, login_bool).
      `login_bool` indica si la combinación debe permitir el acceso.
    - Se utiliza el fixture `driver` para obtener el WebDriver.
    """

    # Crear objeto page y abrir la URL de login
    login_page = LoginPage(driver)
    login_page.open()

    # Intentar login con las credenciales parametrizadas
    login_page.login(username, password)

    # Verificar resultado: si login_bool es True, esperamos ir al inventario
    if login_bool:
        assert "inventory" in driver.current_url
    else:
        # Si login_bool es False, no deberíamos haber navegado al inventario
        assert "inventory" not in driver.current_url

    # Guardar captura para facilitar debugging en caso de fallo
    driver.save_screenshot("login_page.png")

