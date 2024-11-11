from enum import Enum


class BaseEnum(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda d: d.value, cls))


class WrongData(BaseEnum, Enum):
    STRING = 'qwerty'
    INTEGER = 42


class WrongMethod(BaseEnum, Enum):
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"
