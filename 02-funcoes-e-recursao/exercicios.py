# Funções e recursão


# 1. Fatorial, do jeito com laço e do jeito recursivo
def fatorial_laco(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


def fatorial(n):
    if n <= 1:  # caso base: sem ele a recursão nunca para
        return 1
    return n * fatorial(n - 1)  # caso recursivo: um problema menor


# 2. Soma dos dígitos: 1234 -> 1 + 2 + 3 + 4 = 10
def soma_digitos(n):
    if n < 10:
        return n
    return n % 10 + soma_digitos(n // 10)


# 3. Palíndromo: lê igual de trás para frente
def eh_palindromo(texto):
    if len(texto) <= 1:
        return True
    if texto[0] != texto[-1]:
        return False
    return eh_palindromo(texto[1:-1])


# 4. Fibonacci ingênuo, contando quantas vezes a função é chamada
chamadas = 0


def fibonacci(n):
    global chamadas
    chamadas += 1
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# 5. Fibonacci guardando o que já calculou (memoização)
def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n < 2:
        return n
    if n not in memo:
        memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


if __name__ == "__main__":
    print(fatorial(5), fatorial_laco(5))
    print(soma_digitos(1234))
    print(eh_palindromo("arara"), eh_palindromo("python"))

    for n in (10, 20, 25):
        chamadas = 0
        valor = fibonacci(n)
        print(f"fibonacci({n}) = {valor} com {chamadas} chamadas")

    print(fibonacci_memo(90))
