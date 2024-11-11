import random
import string


def generate_palindrome_string() -> str:
    k = random.randint(2, 10)
    letters = ''.join(random.choices(string.ascii_lowercase, k=k))
    return letters + letters[::-1]


def generate_random_string() -> str:
    k = random.randint(4, 10)
    letters = ''.join(random.choices(string.ascii_lowercase, k=k))
    return letters
