import sqlite3
import uuid
from uuid import UUID

import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from utils import generate_palindrome_string, generate_random_string

app = FastAPI()

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE palindromes (id TEXT, result_string TEXT, is_palindrome INTEGER)""")


class Palindrome(BaseModel):
    """
    Модель запроса для создания строки

    - palindrome: флаг для создания строки
    True: запрос на генерацию строки-палиндрома
    False: запрос на генерацию случайной строки, не палиндрома
    """
    palindrome: bool


@app.post("/palindromes/")
async def create_palindrome(palindrome: Palindrome):
    string_id = uuid.uuid4()
    result = generate_palindrome_string() if palindrome.palindrome else generate_random_string()
    is_palindrome = palindrome.palindrome

    data = (str(string_id), result, is_palindrome)

    cursor.execute("INSERT INTO palindromes VALUES (?, ?, ?)", data)
    conn.commit()

    return {
        'id': string_id,
        'result': result
    }


@app.get("/palindromes/{string_id}")
async def read_item(string_id: UUID):
    cursor.execute("SELECT * FROM palindromes WHERE id=?", (str(string_id),))
    result = cursor.fetchone()

    if not result:
        raise HTTPException(status_code=404, detail="String not found!")

    return {"result": {
        "id": result[0],
        "result_string": result[1],
        "is_palindrome": result[2]
    }}


if __name__ == '__main__':
    uvicorn.run("server:app", reload=True)
