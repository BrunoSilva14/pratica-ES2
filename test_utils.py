# test_utils.py
from utils import add, subtract, is_palindrome

# Teste 1
def test_add_positive():
    assert add(5, 10) == 15

# Teste 2
def test_add_negative():
    assert add(-1, -1) == -2

# Teste 3
def test_subtract():
    assert subtract(10, 5) == 5

# Teste 4: Palíndromo simples
def test_is_palindrome_simple():
    assert is_palindrome("radar") == True

# Teste 5: Palíndromo complexo (com espaços e maiúsculas)
def test_is_palindrome_complex():
    assert is_palindrome("A man, a plan, a canal: Panama") == True

# Teste 6 (Extra): Não palíndromo
def test_is_not_palindrome():
    assert is_palindrome("python") == False