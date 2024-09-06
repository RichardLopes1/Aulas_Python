def lista_tabela(t: list) -> None:
 for i in range(0, len(tabela), 1):
  print(f"Registro: {i + 1}")
  print(f"nome:{t[i] ['nome']}")
  print(f"nome:{t[i] ['idade']}\n")

import os 
os.system ('clear')

tabela = list()
agenda = {
    'nome': 'Richard',
    'idade': 18
}

tabela.append(agenda.copy())

agenda['nome'] = input("Nome:")
agenda['idade'] = input("Idade:")
tabela.append(agenda.copy())


agenda['nome'] = input("Nome:")
agenda['idade'] = input("Idade:")
tabela.append(agenda.copy())

lista_tabela(tabela)