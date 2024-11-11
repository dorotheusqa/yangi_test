from typing import Literal

from pydantic import BaseModel, field_validator
from pydantic.types import UUID4


class PalindromeResponse(BaseModel):
    id: UUID4
    result: str

    @field_validator("result")
    @classmethod
    def result_must_be_palindrome(cls, v: str) -> str:
        if v != v[::-1]:
            raise ValueError("result must be palindrome!")
        return v

    def __str__(self):
        return "Модель ответа PalindromeResponse"


class RandomStringResponse(BaseModel):
    id: UUID4
    result: str

    @field_validator("result")
    @classmethod
    def result_must_not_be_palindrome(cls, v: str) -> str:
        if v == v[::-1]:
            raise ValueError("result must not be palindrome!")
        return v

    def __str__(self):
        return "Модель ответа RandomStringResponse"


class ResultModel(BaseModel):
    id: UUID4
    result_string: str
    is_palindrome: Literal[1, 0]


class GetStringResponseModel(BaseModel):
    result: ResultModel
