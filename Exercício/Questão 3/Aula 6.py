opcao =0

while opcao!=3:
    print("1 - Cadastrar \n")
    print("2 - Consultar \n")
    print("3 - Sair \n")
    print("4 - Alterar \n")
    print("5 - Remover \n")

    opcao = int(input("Digite a opção \n"))
    if opcao == 1:
        arquivo = open('Produtos.txt','a')
        arquivo.write(input("Digite o nome do Produto:\n"))
        arquivo.write("\n")
        arquivo.write(input("Digite o preço do Produto:\n"))
        arquivo.write("\n")
        print("Cadastrado com sucesso \n")
        input("Aperte ENTER para continuar")
    elif opcao ==2:
        arquivo = open('Produtos.txt','r')
        cadastro = []
        cadastro = arquivo.readlines()
        num = len(cadastro)
        cont = 0
        while cont < num:
            print("NomeProduto: ",cadastro[cont]," PrecoProduto: ",cadastro[(cont+1)])
            cont = cont + 2
        input("Aperte ENTER para continuar\n")
    elif opcao ==3:
        print("Muito Obrigado, tchau \n")
    elif opcao ==4:
        arquivo = open("Produtos.txt", 'r')
        cadastro = []
        cadastro = arquivo.readlines()
        print(cadastro)
        cad = [s.strip() for s in cadastro]
        cont = 0
        num = len(cad)
        busca = False
        mat = input("Digite o nome do Produto:\n")
        while cont < num:
            if mat == cad[cont]:
                cad[cont] =input("Novo produto \n")
                cad[cont+1]=input("Novo preco\n")
                busca = True
                break
            cont = cont + 2
        if busca == False:
            print("Produto não encontrado \n")
        else:
            arquivo = open("Produtos.txt", 'w')
            cont = 0
            num = len(cad)
            while cont < num:
                arquivo.write(cad[cont])
                arquivo.write("\n")
                cont = cont + 1
            input("Digite ENTER para continuar\n")
    elif opcao  ==5:
        arquivo = open("Produtos.txt", 'r')
        cadastro = []
        cadastro = arquivo.readlines()
        cad = [s.strip() for s in cadastro]
        busca = False
        cont = 0
        num = len(cad)
        mat = input("Digite nome do produto: \n")
        while cont < num:
            if mat == cad[cont]:
                cad.pop(cont)
                cad.pop(cont)
                busca = True
                break
            cont = cont + 2
        if busca == False:
            print("Produto não encontrado")
        else:
            arquivo = open("Produtos.txt", 'w')
            cont = 0
            num = len(cad)
            while cont < num:
                arquivo.write(cad[cont])
                arquivo.write("\n")
                cont = cont + 1
                input("Digite ENTER para continuar")
    else:
        print("Opçao Inválida \n")
        input("Aperte ENTER para continuar\n")