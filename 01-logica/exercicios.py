# Lógica: variáveis, condicionais e laços


# 1. Par ou ímpar
def par_ou_impar(n):
    if n % 2 == 0:
        return "par"
    return "ímpar"


# 2. Maior de três números, sem usar max()
def maior_de_tres(a, b, c):
    maior = a
    if b > maior:
        maior = b
    if c > maior:
        maior = c
    return maior


# 3. Tabuada de um número
def tabuada(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


# 4. Soma dos números de 1 até n
def soma_ate(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


# 5. Número primo
def eh_primo(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


if __name__ == "__main__":
    print(par_ou_impar(7))
    print(maior_de_tres(4, 9, 2))
    tabuada(3)
    print(soma_ate(100))
    print([n for n in range(30) if eh_primo(n)])
