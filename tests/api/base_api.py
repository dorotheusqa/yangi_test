import allure
import requests
from pydantic import ValidationError
from settings import url_settings


class API:
    def __init__(self):
        self.base_url = url_settings.base_url.unicode_string()
        self.response = None

    def _request(self, url, method, body=None):
        with allure.step(f"Отправить {method} на {url}"):
            self.response = requests.request(url=url, method=method, json=body)

    def _create_body(self, palindrome_flag: bool | str = True, value=None):
        match palindrome_flag:
            case True:
                return {"palindrome": True}
            case False:
                return {"palindrome": False}
            case "Empty":
                return {}
            case "Non_boolean":
                return {"palindrome": value}

    # Assertions and checks

    @allure.step("ОР: Статус код равен {code}")
    def check_response_status_code_equal(self, code):
        assert self.response.status_code == code, (
            f"\nОР: Статус код равен '{code}'"
            f"\nФР: Статус код равен '{self.response.status_code}'"
        )

    @allure.step("ОР: Модель провалидирована {model}")
    def validate_response_model(self, model):
        try:
            model.model_validate(self.response.json())
        except ValidationError as e:
            errors = "".join([
                f"\nПоле '{error['loc'][0]}': {error['msg']}"
                f"\n(получено: {error.get('input', 'не указано')})"
                for error in e.errors()]
            )
            assert False, (f"\nОР: Модель провалидирована"
                           f"\nФР: Ошибка валидации модели:{errors}")
