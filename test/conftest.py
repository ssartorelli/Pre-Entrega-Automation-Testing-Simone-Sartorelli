"""Configuración de fixtures para pytest.

Este archivo expone el fixture `driver` que proporciona un WebDriver
configurado usando la función `get_driver` definida en `utils.helpers`.

El fixture usa el patrón `yield` para ceder el driver al test y luego
ejecutar la limpieza (`driver.quit()`) al finalizar el test.
"""

import pytest
from utils.helpers import get_driver


@pytest.fixture
def driver():
    """Fixture que inicializa y entrega un WebDriver listo para usar.

    Uso:
        def test_something(driver):
            driver.get("https://www.saucedemo.com")

    Comportamiento:
    - Llama a `get_driver()` para construir/obtener la instancia.
    - `yield` devuelve el driver al test.
    - Después del test, se llama a `driver.quit()` para cerrar el navegador
      y liberar recursos.
    """
    # Obtener instancia de WebDriver desde helpers
    driver = get_driver()
    yield driver
    # Teardown: cerrar el navegador al finalizar el test
    driver.quit()


