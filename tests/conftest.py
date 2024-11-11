from pytest import fixture
from api.database import DataBaseAPI

pytest_plugins = ["fixture.create_palindrome", "fixture.get_string"]


@fixture(scope="session", autouse=True)
def cleanup_database():
    try:
        yield
    finally:
        DataBaseAPI.delete_all_palindromes_from_db()
