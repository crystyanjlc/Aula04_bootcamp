# 3. Informações de um livro
from typing import Union




lista: dict[str, Union[str, float, bool]] = {
 "Nome"  : "Do mil ao Milhão" ,
 "Valor" : 35.90 ,
 "Disponibilidade" : True
}

if lista["Disponibilidade"] == False:
    print("Livro em falta")
else:
    print("Livro disponível")

print(lista)