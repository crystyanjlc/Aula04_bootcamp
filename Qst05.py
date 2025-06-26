# 7. Filtragem de Dados
# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

from typing import List 

idades: List[int] = [ 6, 50 , 8 , 13 , 30 , 45 , 58]

De_maior: List[int] = [ i for i in idades if i >= 18 ]

print(De_maior)   