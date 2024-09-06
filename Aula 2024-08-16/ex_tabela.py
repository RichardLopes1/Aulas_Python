registros = {}
def mostrar_menu():
   print("\nMenu:")
   print("0 - Sair")
   print("1 - Consultar")
   print("2 - Listar registros")
   print("3 - Cadastrar")
   print("4 - Editar")
   print("5 - Excluir")
def consultar(cpf):
   return registros.get(cpf)
def listar_registros():
   for cpf, dados in registros.items():
       print(f"CPF: {cpf}, Dados: {dados}")
def cadastrar(cpf, dados):
   if cpf in registros:
       print("Já existe um registro com esse CPF.")
   else:
       registros[cpf] = dados
       print("Registro cadastrado com sucesso.")
def editar(cpf, novos_dados):
   if cpf in registros:
       registros[cpf] = novos_dados
       print("Registro editado com sucesso.")
   else:
       print("CPF não encontrado.")
def excluir(cpf):
   if cpf in registros:
       del registros[cpf]
       print("Registro excluído com sucesso.")
   else:
       print("CPF não encontrado.")
while True:
   mostrar_menu()
   opcao = int(input("\nEscolha uma opção: "))
   if opcao == 0:
       break
   elif opcao == 1:
       cpf = input("Digite o CPF para consultar: ")
       resultado = consultar(cpf)
       if resultado:
           print(f"Registro encontrado: {resultado}")
       else:
           print("Registro não encontrado.")
   elif opcao == 2:
       listar_registros()
   elif opcao == 3:
       cpf = input("Digite o CPF: ")
       dados = input("Digite os dados do registro: ")
       cadastrar(cpf, dados)
   elif opcao == 4:
       cpf = input("Digite o CPF para editar: ")
       novos_dados = input("Digite os novos dados: ")
       editar(cpf, novos_dados)
   elif opcao == 5:
       cpf = input("Digite o CPF para excluir: ")
       excluir(cpf)
   else:
       print("Opção inválida.")


