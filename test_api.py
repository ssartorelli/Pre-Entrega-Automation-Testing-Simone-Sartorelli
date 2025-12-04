import requests
import logging
import pathlib
from faker import Faker
from conftest import logger
import pytest
from datetime import datetime


# -----------------------------
# Configuración y constantes
# -----------------------------

# Mensaje inicial en el logger importado desde `conftest.py`
logger.info("Configuracion del logger")

# URL base de la API bajo prueba. No modifiqué el valor original.
BASE_URL = "Http://Jsonplaceholder.typicode.com"

# Nota: `Faker` normalmente se instancia con `Faker()`.
# Aquí se mantiene `fake = Faker` para no modificar la lógica;
# si quieres que funcione como un generador de datos real, cambia a `Faker()`.
fake = Faker

# Directorio local para logs (se crea si no existe)
path_dir = pathlib.Path('logs')
path_dir.mkdir(exist_ok=True)



class TestJSONPlaceholder:

    # Mensajes de contexto para el registro
    logger.info("Pruebas para la API JSONPlaceholder")
    logger.info("TEST 1 - GET - Obtener todos los posts")

    def test_get_posts_success(self):
        """Test que valida la operación GET /posts.

        Pasos:
        - Realiza la petición GET a /posts
        - Verifica que el status code sea 200
        - Valida que la respuesta sea una lista no vacía
        - Comprueba que el primer elemento tenga los campos esperados
        - Verifica tipos de datos de los campos
        """
        logger.info("\n=== Test 1: GET Posts ===")

        # 1) Petición GET a la colección de posts
        logger.info("Peticion GET")
        response = requests.get(f"{BASE_URL}/posts")

        # 2) Validación del código de estado
        logger.info("Validar código de estado")
        assert response.status_code == 200, f"Esperado 200, Obtenido {response.status_code}"
        print("✅ Código de estado 200 - OK")
        logger.info("✅ Código de estado 200 - OK")

        # 3) Convertir la respuesta a JSON y validar estructura
        logger.info("Convertir a JSON")
        data = response.json()

        logger.info("Validar estructura de datos")
        assert isinstance(data, list)
        assert len(data) > 0
        print(f"✅Estructura Json correcta")
        logger.info("Estructura Json correcta")

        # 4) Validar campos del primer post
        logger.info("Validar estructura del primero post")
        first_post = data[0]
        required_fields = {"userId", "id", "title", "body"}
        for field in required_fields:
            assert field in first_post, f"Falta el campo {field} en el post"
        print("✅Estructura del primer post es correcta")
        logger.info("✅Estructura del primer post es correcta")

        # 5) Validar tipos de datos esperados
        logger.info("Validar tipos de datos")
        assert isinstance(first_post['userId'], int), "userId debe ser un entero"
        assert isinstance(first_post['id'], int), "id debe ser un entero"
        assert isinstance(first_post['title'], str), "title debe ser una cadena"
        assert isinstance(first_post['body'], str), "body debe ser una cadena"
        print("Tipos de datos del primer post son correctos")
        logger.info("✅Tipos de datos del primer post son correctos")

        print("🎉 Test GET Posts completado exitosamente!")
        logger.info("🎉 Test GET Posts completado exitosamente!")
        print("\n")

        logger.info("TEST 2 - POST - Crear un nuevo post")

    def test_create_post_success(self):
        """Test que valida la operación POST /posts.

        Pasos:
        - Genera datos de ejemplo para un nuevo post
        - Envía POST a /posts con payload JSON
        - Verifica que el status code sea 201
        - Valida estructura y valores devueltos
        """
        logger.info("POST /posts - Crear un nuevo post exitosamente")
        print("\n=== Test 2: CREATE Post ===")

        # Datos para crear el post (aquí se usa `fake`, ver nota arriba)
        logger.info("Datos para crear el post")
        post_data = {
            "title": fake.word(),
            "body": fake.text(),
            "userId": fake.random_int(1,6)
        }
        logger.info("\n=== Test 2: POST Create Post ===")

        # Petición POST con JSON
        logger.info("Petición POST")
        response = requests.post(f"{BASE_URL}/posts", json=post_data)

        # Validar código 201 (Created)
        logger.info("Validar código de estado")
        assert response.status_code == 201, f"Esperado 201, Obtenido {response.status_code}"
        print("✅ Código de estado 201 - Created")
        logger.info("✅ Código de estado 201 - Created")

        # Convertir respuesta a JSON y validar contenido
        logger.info("Convertir a JSON")
        data = response.json()

        logger.info("Validar estructura de datos")
        required_fields = {"id", "title", "body", "userId"}
        for field in required_fields:
            assert field in data, f"Falta el campo {field} en la respuesta"
        print("✅ Estructura JSON correcta")
        logger.info("✅ Estructura JSON correcta")

        # Validar que los valores devueltos coincidan con los enviados
        logger.info("Validar valores devueltos")
        assert data["title"] == post_data["title"], "El título no coincide"
        assert data["body"] == post_data["body"], "El cuerpo no coincide"
        assert data["userId"] == post_data["userId"], "El userId no coincide"
        print("✅ Valores devueltos son correctos")
        logger.info("✅ Valores devueltos son correctos")
        print("🎉 Test CREATE Post completado exitosamente!")
        logger.info("🎉 Test CREATE Post completado exitosamente!")
        print("\n")

        logger.info("TEST 3 - PUT - Actualizar un post existente")

    def test_update_post_success(self):
        """Test que valida la operación PUT /posts/{id}.

        Pasos:
        - Define `post_id` a actualizar
        - Prepara nuevos datos y envía PUT
        - Verifica status 200 y la estructura/valores de la respuesta
        """
        logger.info("PUT /posts/{id} - Actualizar un post existente exitosamente")
        print("\n=== Test 3: UPDATE Post ===")

        # ID del post a actualizar (ejemplo fijo)
        logger.info("ID del post a actualizar")
        post_id = 1

        # Datos a enviar en la actualización
        logger.info("Datos para actualizar el post")
        update_data = {
            "title": fake.word(),
            "body": fake.text(),
            "userId": fake.random_int(1,6)
        }
        logger.info("\n=== Test 3: PUT Update Post ===")

        # Petición PUT
        logger.info("Petición PUT")
        response = requests.put(f"{BASE_URL}/posts/{post_id}", json=update_data)

        # Validación del status code
        logger.info("Validar código de estado")
        assert response.status_code == 200, f"Esperado 200, Obtenido {response.status_code}"
        print("✅ Código de estado 200 - OK")
        logger.info("✅ Código de estado 200 - OK")

        # Convertir a JSON y validar estructura
        logger.info("Convertir a JSON")
        data = response.json()

        logger.info("Validar estructura de datos")
        required_fields = {"id", "title", "body", "userId"}
        for field in required_fields:
            assert field in data, f"Falta el campo {field} en la respuesta"
        print("✅ Estructura JSON correcta")
        logger.info("✅ Estructura JSON correcta")

        # Validar que los valores actualizados coincidan
        logger.info("Validar valores devueltos")
        assert data["title"] == update_data["title"], "El título no coincide"
        assert data["body"] == update_data["body"], "El cuerpo no coincide"
        assert data["userId"] == update_data["userId"], "El userId no coincide"
        assert data["id"] == post_id, "El ID del post no coincide"
        print("✅ Valores devueltos son correctos")
        logger.info("✅ Valores devueltos son correctos")
        print("🎉 Test UPDATE Post completado exitosamente!")
        logger.info("🎉 Test UPDATE Post completado exitosamente!")
        print("\n")