# O mesmo assunto visto do Python: tudo é objeto, e o Python cuida da memória.
import sys

print("== Tamanho dos objetos no Python ==")
print("int 0:", sys.getsizeof(0), "bytes")
print("int 2**100:", sys.getsizeof(2**100), "bytes")
print("lista vazia:", sys.getsizeof([]), "bytes")
print("lista com 4 números:", sys.getsizeof([10, 20, 30, 40]), "bytes")

print("\n== Sem limite de tamanho ==")
print("255 + 1 =", 255 + 1)
print("2 ** 100 =", 2**100)

print("\n== Duas variáveis, o mesmo objeto ==")
a = [1, 2, 3]
b = a  # b não é uma cópia: aponta para a mesma lista
b.append(4)
print("a =", a)
print("a is b:", a is b)
