# Importaciones necesarias
import pytest
import logging
import pathlib
import time
from selenium import webdriver
from pytest_html import extras


# -----------------------------
# Fixtures y utilidades comunes
# -----------------------------

@pytest.fixture
def api_url():
    # Fixture que devuelve la URL base para las pruebas de API
    return "http://jsonplaceholder.typicode.com"


def pytest_html_report_title(report):
    """Personaliza el título del reporte HTML generado por pytest-html.

    Se muestra en la pestaña del navegador cuando se abre el reporte.
    """
    report.title = "TalentoLab – Reporte de Testing"


# -----------------------------
# Configuración de logging
# -----------------------------

# Directorio donde se almacenarán los logs
path_dir = pathlib.Path('logs')
path_dir.mkdir(exist_ok=True)

logging.basicConfig(
    # Archivo de salida para el historial de logs
    filename= path_dir/ "historial.log",
    # Nivel mínimo de mensajes a guardar
    level= logging.INFO,
    # Formato con hora, nivel y mensaje
    format='%(asctime)s %(levelname)s %(name)s – %(message)s',
    datefmt='%H:%M:%S'
)


logger = logging.getLogger()


# -----------------------------
# Carpeta para screenshots
# -----------------------------
# Esta carpeta se usará para guardar capturas cuando fallen tests que usan el
# fixture `driver` (ver hook más abajo).
target = pathlib.Path('reports/screens')
target.mkdir(parents=True, exist_ok=True)


# -----------------------------
# Fixture `driver` para Selenium
# -----------------------------
@pytest.fixture
def driver():
    """Fixture que inicializa un navegador Chrome para pruebas UI.

    - Inicia `webdriver.Chrome()`
    - Abre `https://google.com` como página inicial de comprobación
    - Espera 2 segundos para que la página cargue (espera implícita/explicita
      más robusta es recomendable en tests reales)
    - Rinde el driver al test y lo cierra al finalizar
    """
    d = webdriver.Chrome()
    d.get("https://google.com")
    time.sleep(2)  # Espera simple para que cargue la página
    yield d
    # Cierra el navegador al terminar el test
    d.quit()


# -----------------------------
# Hook: captura screenshot al fallar
# -----------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook que se ejecuta tras cada fase del test y añade screenshots al
    reporte HTML si el test falla y utiliza el fixture `driver`.

    - `hookwrapper=True` permite ejecutar código antes/después del reporte.
    - Si el fallo ocurre en la fase 'call' y el test pidió el fixture `driver`,
      se captura una imagen y se añade a `report.extra` para que pytest-html
      la muestre en el reporte.
    """
    outcome = yield
    report = outcome.get_result()

    # Solo interesa la fase de ejecución (no setup/teardown) y si falló
    if report.when == 'call' and report.failed:
        # Comprobar si el test solicitó el fixture `driver`
        if 'driver' in item.fixturenames:
            driver = item.funcargs['driver']

            # Nombre de archivo basado en el nombre del test
            file_name = target / f"{item.name}.png"
            # Guardar captura
            driver.save_screenshot(str(file_name))

            # Asegurar que report.extra existe y añadir la imagen como extra
            report.extra = getattr(report, 'extra', [])
            report.extra.append(extras.png(str(file_name)))

