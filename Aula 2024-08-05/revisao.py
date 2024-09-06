# criando um dicionario vazio

lista = [] # ou list()
tupla = [] # ou tuple()
dicionario = {} # ou dict()



contato = {
    # "key" : value,
    "nome" : "Richard Lopes da Silva", 
    "idade" : 18,
    "namorando" : True,
    "altura" : 1.73,
}
#Execução bruta
print("Exibição bruta")
print(contato)

#Exibição manual
print("\nExibição manual")
print(f"Nome.................: {contato["nome"]}")

# Metodos que tratam dicionarios
print(f"Exibindo as keys: {contato.keys()}")

print(f"\nExibindo os valores: {contato.values()}")

print(f"Exibir os item: {contato.items()}")
os.system("clear")

# utilizando o del para remover um item
del contato["altura"]

# Inserindo uma key
contato["instagram"] = "@lopes_richard1"

# Exibição do dicionario através dos métodos

for k,v in contato.items():
    print(f"{k} => {v}")


