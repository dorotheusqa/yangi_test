from pytest import fixture

from api.get_string import GetStringAPI
from model.model import GetStringResponseModel


@fixture
def get_string_api() -> GetStringAPI:
    return GetStringAPI()


@fixture
def get_string_response_model():
    return GetStringResponseModel
