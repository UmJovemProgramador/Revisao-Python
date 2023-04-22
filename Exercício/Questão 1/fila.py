fila = []
opcao = 0
tracos = ("-" * 46)

while opcao != 4:
    print ("-------------------- MENU --------------------")
    print("> Digite 1 para inserir um nome na fila.\n")
    print("> Digite 2 para remover o primeiro nome da fila.\n")
    print("> Digite 3 para mostrar a fila.\n")
    print("> Digite 4 para sair do programa.")
    print (tracos,"\n")

    opcao = int(input("Escolha uma das opções acima: \n"))

    if opcao == 1:
        print (tracos)
        nome = input("Digite o nome a ser inserido na fila: \n")
        fila.append(nome)
        print (tracos,"\n")
        print("O nome",nome,"foi inserido na fila.\n")
        print (tracos,"\n")
        input("Pressione <ENTER> para continuar.\n")

    elif opcao == 2:
        if len(fila) == 0:
            print (tracos,"\n")
            print("A fila está vazia no momento.\n")
            print (tracos,"\n")
            input("Pressione <ENTER> para continuar.\n")
        else:
            nome = fila.pop(0)
            print (tracos,"\n")
            print("O primeiro nome (",nome,") foi removido da fila.\n")
            print (tracos,"\n")
            input("Pressione <ENTER> para continuar.\n")

    elif opcao == 3:
        if len(fila) == 0:
            print (tracos,"\n")
            print("A fila está vazia no momento.\n")
            print (tracos,"\n")
            input("Pressione <ENTER> para continuar.\n")
        else:
            print (tracos,"\n")
            print("Aqui está a fila atual:", fila,"\n")
            print (tracos,"\n")
            input("Pressione <ENTER> para continuar.\n")


    elif opcao == 4:
        print (tracos,"\n")
        print ("Finalizando programa... 👋\n")
        break

    else:
        print (tracos,"\n")
        print("Opção inválida 🚫. Tente novamente com uma opção válida entre 1 e 4.\n")
        print (tracos,"\n")
        input("Pressione <ENTER> para continuar.\n")