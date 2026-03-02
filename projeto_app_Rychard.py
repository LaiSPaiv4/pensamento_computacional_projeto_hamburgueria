'''
CRUD

    Hamburgueria

Este sistema irá  criar um menu para a Hamburgueria
Rychard
Rychard
'''
while True:

    print("\n== Sistema da Hamburgueria ===")
    print("1. Cadastro") #Para o cliete criar a conta, irá precisar colocar o, Email, Numero de telefone, CPF
    print("2. Esqueceu a senha") #Enviar um codigo de 6 digitos para o email cadastrado, Criar nova senha
    print("3. Menu 1") #Combos e opções
    print("4. Carrinho") #Adicionar os combos ou opções no carrinho
    print("5. Opções") #Retirar algum ingrediente
    print("6. Finalizar pedido") # O cliente precisará colocar o, CEP, Endereço, Numero da casa, Ponto de referencia, Forma de pagamento para calcular a entrega
    print("7. Cupom") #Cada compra, o cliente ira acumular 5% para a o proximo pedido que o cliente fizer
    print("8. Chat da loja") #Pontos que podem ser melhorados na loja
    print("9. Feedback") #O cliente dar uma avaliação de 0-5 para a loja
    print("0. Sair") #Sair do atendimento


    escolha = input("\nEscolha uma opção:")

    if escolha == '1':
        print("\n--- Novo Cadastro ---")
        nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        cpf = input("CPF: ")
        senha = input("Senha: ")
        
        cliente = {
            "nome": nome,
            "email": email,
            "telefone": telefone,
            "cpf": cpf,
            "senha": senha
        }


    elif escolha == '2':
        print("Esqueceu a senha")


    elif escolha == '3':
        print("\n--- Cardápio ---")
        print("1. X-Bacon - 25,00R$")
        print("2. X-Tudo - 30,00R$")
        item = input("escolha o numero do lanche para continuar: ")





    elif escolha == '4':
        print("Aqui fica registrado os pedido")


    elif escolha == '5':
        print("Retirar algo")


    elif escolha == '6':
        print("Finalizar pedido")


    elif escolha == '7':
        print("Nossos cupons!") 


    elif escolha == '8':
        print("Entre em contato")


    elif escolha == '9':
        print("Nos diga oque achou")



    elif escolha == '0':
        print("Saindo do sistema. Até logo")
        break



else:
    print("Opção inválida, Por favor, Tente novamente")    