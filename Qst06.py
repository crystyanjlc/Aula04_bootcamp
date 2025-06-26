# unir dicionários

dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"c": 3, "d": 4, "e" : 5}

print(f"Dicionário 01 - {dicionario1}")
print(f"Dicionário 02 - {dicionario2}")

dicionario_fundido = {**dicionario1, **dicionario2}

print(f"Dicionário 03 - {dicionario_fundido}")

#print(dicionario_fundido)