import allure
from pytest import mark
from data.enum_data import WrongData, WrongMethod

pytestmark = [allure.parent_suite("Тест создания и получения строки"),
              allure.suite("Создание строки"),
              allure.link("https://yangi.uz/#business"),
              mark.create_palindrome]


@allure.title("Создание палиндрома")
@mark.smoke
def test_create_palindrome(palindrome_api, palindrome_response_model):
    palindrome_api.create_palindrome_in_db()
    palindrome_api.check_response_status_code_equal(200)
    palindrome_api.validate_response_model(palindrome_response_model)


@allure.title("Создание случайной строки")
@mark.smoke
def test_create_random_string(palindrome_api, random_string_response_model):
    palindrome_api.create_random_string_in_db()
    palindrome_api.check_response_status_code_equal(200)
    palindrome_api.validate_response_model(random_string_response_model)


@allure.title("Запрос с не разрешенным методом: {method}")
@mark.parametrize("method", WrongMethod.list())
def test_send_method_not_allowed(method, palindrome_api):
    palindrome_api.send_method_not_allowed(method)
    palindrome_api.check_response_status_code_equal(405)


@allure.title("Запрос с пустым body")
def test_send_empty_body(palindrome_api):
    palindrome_api.send_empty_body()
    palindrome_api.check_response_status_code_equal(422)


@allure.title("Запрос с body.palindrome содержащим не булево значение: {value}")
@mark.parametrize("value", WrongData.list())
def test_send_non_boolean_body(value, palindrome_api):
    palindrome_api.send_non_boolean_value_in_body(value)
    palindrome_api.check_response_status_code_equal(422)
