#Proposito del proyecto#
**Implementar un framework de pruebas automatizadas utilizando Python, Selenium WebDriver y Pytest para validar la funcionalidad principal del sitio web saucedemo.com. El proyecto tiene como finalidad demostrar la capacidad para automatizar flujos clave de navegación e interacción, aplicando buenas prácticas de organización de código, control de versiones y generación de reportes. Se busca asegurar la calidad del software, reducir el tiempo de ejecución de pruebas de regresión y entregar resultados claros y accionables.**
#Objetivos del Proyecto Final#
**El objetivo central de este proyecto es el desarrollo de un Framework de Automatización de Pruebas completo que demuestre la integración y aplicación de los conocimientos adquiridos durante el curso.**
**1. Desarrollo de un Framework Integral (Objetivo Principal)**
**Crear un framework de testing automatizado robusto y escalable utilizando Python como lenguaje principal y Pytest como framework de ejecución.**

**Integrar diversas herramientas para manejar diferentes tipos de pruebas dentro del mismo entorno.**

**2. Implementación de Pruebas de Calidad Dual (UI y API)**
**Automatizar Pruebas de Interfaz de Usuario (UI): Utilizar Selenium WebDriver para desarrollar casos de prueba que cubran flujos completos (ej. login, navegación, checkout) e incluir al menos un escenario negativo.**

**Automatizar Pruebas de API: Utilizar la biblioteca Requests para implementar casos de prueba en endpoints públicos, cubriendo métodos HTTP (GET, POST, DELETE) y validando códigos de estado y contenido de las respuestas JSON.**

**3. Aplicación de Estándares de Diseño y Buenas Prácticas**
Garantizar la Mantenibilidad: Implementar el patrón de diseño Page Object Model (POM) para las pruebas de UI, separando la lógica de las pruebas de la lógica de interacción con las páginas.**

**Estructurar el Código: Organizar el proyecto con una estructura de directorios clara (pages, tests, utils, etc.), aplicando buenas prácticas de programación, y utilizando una convención de nombres significativa.**

**Manejar Datos de Prueba: Implementar la parametrización de pruebas, utilizando fuentes externas (CSV, JSON, etc.) para la gestión de datos.**

**4. Generación de Reportes y Trazabilidad**
**Facilitar la Interpretación: Configurar Pytest para generar reportes HTML detallados que muestren el estado y la duración de los tests.**

**Mejorar la Depuración: Implementar un sistema de logging detallado para registrar los pasos clave de la ejecución.**

**Capturar Evidencia: Desarrollar una funcionalidad para la captura automática de screenshots al momento de una falla, incluyendo estas capturas en los reportes generados.**

**5. Control de Versiones y Documentación**
**Gestionar el Código: Utilizar Git para el control de versiones y GitHub como repositorio público, manteniendo un historial de commits claro.**

**Documentar el Proyecto: Crear un archivo README.md completo que explique el propósito, las tecnologías, la estructura, la instalación de dependencias, la ejecución de pruebas y la interpretación de los reportes.**



##Tecnologías Requeridas##

**Python como lenguaje principal**

**Pytest para estructura de testing**

**Selenium WebDriver para automatización**

**Git y GitHub para control de versiones**

**Biblioteca Requests para Testing de Api**

##Estructura del Proyecto##
**El código está organizado siguiendo el patrón Page Object Model (POM) y una estructura modular para mantener la lógica separada y el código limpio.**

**Framework_Automatizacion/**
├── pages/                  # Contiene las clases Page Object Model (POM) para la UI.
│   ├── login_page.py
│   └── product_page.py
├── tests/                  # Contiene los archivos de prueba que usan Pytest.
│   ├── test_ui_flows.py    # Pruebas de UI (Selenium)
│   └── test_api_calls.py   # Pruebas de API (Requests)
├── utils/                  # Módulos de utilidad y soporte.
│   ├── data_reader.py      # Lógica para leer archivos CSV/JSON.
│   └── logger_setup.py     # Configuración del sistema de logging.
├── data/                   # Archivos de datos externos (JSON, CSV).
│   └── test_users.csv
├── reports/                # Directorio donde se almacenan los reportes generados.
├── screenshots/            # Directorio para las capturas de pantalla de fallas.
├── conftest.py             # Hooks y fixtures de Pytest (ej. inicialización del driver).
├── requirements.txt        # Lista de dependencias del proyecto.
└── README.md


##Instruccion de instalacion de dependencias##

**Pip install selenium**


##Comandos para ejecucion de pruebas##
```bash
pytest -v --html=reports/reporte.html

pytest -v

pytest -v --html=reporte.html**

pytest install -r requiments.txt

pytest freeze > requirements.txt