from pytest import fixture

from api.palindrome import PalindromeAPI
from model.model import PalindromeResponse, RandomStringResponse


@fixture
def palindrome_api() -> PalindromeAPI:
    return PalindromeAPI()


@fixture
def palindrome_response_model():
    return PalindromeResponse


@fixture
def random_string_response_model():
    return RandomStringResponse
