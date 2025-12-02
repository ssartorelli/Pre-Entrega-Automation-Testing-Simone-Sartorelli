import pytest
from page.login_page import LoginPage
from data.data_login import CASOS_LOGIN
from utils.example_csv import get_login_csv, get_login_json
from utils.faker import get_login_faker

@pytest.mark.parametrize("username,password,login_bool",get_login_faker())
def test_login_page(driver,username, password, login_bool):
    #crear objeto de la pagina de login
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)
    if login_bool:
        assert "inventory" in driver.current_url
    else:
        assert "inventory" not in driver.current_url 


