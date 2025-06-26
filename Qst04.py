# 6. Eliminação de Duplicatas
# Objetivo: Dada uma lista de emails, remover todos os duplicados.

from typing import List

lista: List[str] = [ 
                    "crystyanjlc@gmail.com" , 
                    "thiago.crystyan@grupoargo.tech", 
                    "thiago.crystyan@grupoargo.tech" , 
                    "governanca@parcelamostudo.com.br"
                    ]

lista02: List[str] = []

for i in lista:
    if i in lista02:
        print(f"Item duplicado - {i}")
    else:
        lista02.append(i)

print(lista)
print(lista02)

lista03 = set(lista)

print(lista03)

