# utils.py

def add(a, b):
    """Soma dois números."""
    return a + b

def subtract(a, b):
    """Subtrai o segundo número do primeiro."""
    return a - b

def is_palindrome(s: str) -> bool:
    """Verifica se uma string é um palíndromo, ignorando espaços e maiúsculas/minúsculas."""
    # Limpa a string: remove não alfanuméricos e converte para minúsculas
    cleaned = ''.join(filter(str.isalnum, s)).lower()
    
    # Verifica se a string limpa é igual à sua inversa
    return cleaned == cleaned[::-1]