import requests
import logging
import pathlib
from faker import Faker
from conftest import logger
import pytest
from datetime import datetime

logger.info("Configuracion del logger")
BASE_URL ="Http://Jsonplaceholder.typicode.com"
fake = Faker

path_dir = pathlib.Path('logs')
path_dir.mkdir(exist_ok=True)


logging.basicConfig(
    filename= path_dir/ "historial.log",
    level= logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s – %(message)s',
    datefmt='%H:%M:%S'
)

logger = logging.getLogger()

class TestJSONPlaceholder:

    logger.info("Pruebas para la API JSONPlaceholder")

    logger.info("TEST 1 - GET - Obtener todos los posts")
    def test_get_posts_success(self):
        logger.info("\n=== Test 1: GET Posts ===")
        
        
        logger.info("Peticion GET")

        response = requests.get(f"{BASE_URL}/posts")
        
        
        logger.info("Validar código de estado")
        assert response.status_code == 200, f"Esperado 200, Obtenido {response.status_code}"
        print("✅ Código de estado 200 - OK")
        logger.info("✅ Código de estado 200 - OK")
        

        logger.info("Convertir a JSON")
        data  = response.json()

        logger.info("Validar estructura de datos")
        assert isinstance(data, list)

        assert len(data) > 0
        print(f"✅Estructura Json correcta")
        logger.info("Estructura Json correcta")

        logger.info("Validar estructura del primero post")
        first_post = data[0]
        required_fields = {"userId", "id", "title", "body"}
        for field in required_fields:
            assert field in first_post, f"Falta el campo {field} en el post"
        print("✅Estructura del primer post es correcta")
        logger.info("✅Estructura del primer post es correcta")

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
            logger.info("POST /posts - Crear un nuevo post exitosamente")
        print("\n=== Test 2: CREATE Post ===")
        
        logger.info("Datos para crear el post")
        post_data = {
            "title": fake.word(),
            "body": fake.text(),
            "userId": fake.random_int(1,6)
        }
        logger.info("\n=== Test 2: POST Create Post ===")
        
        logger.info("Petición POST")
        response = requests.post(f"{BASE_URL}/posts", json=post_data)
        
        logger.info("Validar código de estado")
        assert response.status_code == 201, f"Esperado 201, Obtenido {response.status_code}"
        print("✅ Código de estado 201 - Created")
        logger.info("✅ Código de estado 201 - Created")

        logger.info("Convertir a JSON")
        data = response.json()
        
        logger.info("Validar estructura de datos")
        required_fields = {"id", "title", "body", "userId"}
        for field in required_fields:
            assert field in data, f"Falta el campo {field} en la respuesta"
        print("✅ Estructura JSON correcta")
        logger.info("✅ Estructura JSON correcta")

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
            logger.info("PUT /posts/{id} - Actualizar un post existente exitosamente")
            print("\n=== Test 3: UPDATE Post ===")
        
        logger.info("ID del post a actualizar")
        post_id = 1
        
        logger.info("Datos para actualizar el post")
        update_data = {
            "title": fake.word(),
            "body": fake.text(),
            "userId": fake.random_int(1,6)
        }
        logger.info("\n=== Test 3: PUT Update Post ===")
        
        logger.info("Petición PUT")
        response = requests.put(f"{BASE_URL}/posts/{post_id}", json=update_data)
        
        logger.info("Validar código de estado")
        assert response.status_code == 200, f"Esperado 200, Obtenido {response.status_code}"
        print("✅ Código de estado 200 - OK")
        logger.info("✅ Código de estado 200 - OK")

        logger.info("Convertir a JSON")
        data = response.json()
        
        logger.info("Validar estructura de datos")
        required_fields = {"id", "title", "body", "userId"}
        for field in required_fields:
            assert field in data, f"Falta el campo {field} en la respuesta"
        print("✅ Estructura JSON correcta")
        logger.info("✅ Estructura JSON correcta")

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