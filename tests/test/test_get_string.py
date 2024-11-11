import allure
from pytest import mark
from uuid import uuid4
from data.enum_data import WrongData

pytestmark = [allure.parent_suite("Тест создания и получения строки"),
              allure.suite("Получение строки"),
              allure.link("https://yangi.uz/#business"),
              mark.read_data]


@allure.title("Получение строки существующей в БД")
@mark.smoke
def test_get_exist_string(palindrome_api, get_string_api, get_string_response_model):
    string_id = palindrome_api.create_palindrome_in_db().get("id")
    get_string_api.get_string(string_id)
    get_string_api.check_response_status_code_equal(200)
    get_string_api.validate_response_model(get_string_response_model)


@allure.title("Получение не существующей в БД строки")
@mark.smoke
def test_get_non_exist_string(get_string_api):
    string_id = str(uuid4())
    get_string_api.get_string(string_id)
    get_string_api.check_response_status_code_equal(404)


@allure.title("Запрос с параметром string_id отличным от UUID")
@mark.parametrize("string_id", WrongData.list())
def test_get_non_exist_string(get_string_api, string_id):
    get_string_api.get_string(string_id)
    get_string_api.check_response_status_code_equal(422)
