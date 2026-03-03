from classes import *
from datetime import datetime
import os
import json
import random

def LimparTela():
    if os.name == "nt":
        os.system(f"cls")
    else:
        os.system(f"clear")

def pausar():
    input(" \n Pressione ENTER para continuar...")

gerentes = []
adm = Gerente("Admin", "123", "123", "algum lugar", "admin@gmail", "Senha" )
gerentes = []
gerentes.append(adm)
clientes = []
vendedores = []
produtos = []
vendas = []
verificar = 0
acessonome = ""
acessocpf = ""

#lendo arquivo json
if os.path.exists("gerentes.json"):
    with open("gerentes.json", "r") as arquivo:
        dados = json.load(arquivo)
    #transformando Lista em Json para Objeto
    for d in dados:
            gerente = Gerente.from_dict_vendedor(d)
            gerentes.append(gerente)

if os.path.exists("vendedor.json"):
    with open("vendedores.json", "r") as arquivo:
        dados = json.load(arquivo)
    #transformando Lista em Json para Objeto
    for d in dados:
            vendedor = Funcionario.from_dict_vendedor(d)
            vendedores.append(vendedor)

if os.path.exists("produtos.json"):
    with open("produtos.json", "r") as arquivo:
        dados = json.load(arquivo)
    #transformando Lista em Json para Objeto
    for d in dados:
            produto = Produto.from_dict_produto(d)
            produtos.append(produto)

if os.path.exists("vendas.json"):
    with open("vendas.json", "r") as arquivo:
        dados = json.load(arquivo)
    #transformando Lista em Json para Objeto
    for d in dados:
            venda = Venda.from_dict_venda(d)
            vendas.append(venda)

def salvarprodutos(lista):
    dados_dict = [produto.to_dict_produto() for produto in lista]
    with open("produtos.json", "w") as arquivo:
        json.dump(dados_dict, arquivo, indent=4)

def salvarvendas(lista):
    dados_dict = [venda.to_dict_venda() for venda in lista]
    with open("vendas.json", "w") as arquivo:
        json.dump(dados_dict, arquivo, indent=4)

def CadastrarProdutos():
    LimparTela()
    opcao = input("Voce deseja (Cadastrar produtos - 1) ou (Excluir Produto - 2)? ")
    if(opcao == "1"):
        nome_pro = input("Digite o Nome do Produto: ")
        _ID = input("Digite o ID do Produto: ")
        marca = input("Marca: ")
        quantidade = input("Quantidade: ")
        preco_venda = input("Preço Vendido: ")
        preco_custo = input("Preço de Compra: ")
    elif opcao=="2":
        apagado = input("Digite o ID do Produto que deseja apagar: ")
        encontrado = False
        for produto in produtos:
             if(apagado==produto._ID):
                 produtos.remove(produto)
                 encontrado = True
                 print(f"\nCliente {produto.nome_pro} removido com sucesso!")
                 encontrado = True
                 break
        if not encontrado:
            print("\n[!] ID não encontrado.")

    produto = Produto(nome_pro, _ID, marca, quantidade,preco_venda, preco_custo)
    produtos.append(produto)
    salvarprodutos(produtos)
    pausar()

def AtualizarEstoque(cargo):
    LimparTela()
    _ID = input("Digite o ID do Produto que deseja atualizar: ")
    encontrado = False
    for produto in produtos:
        if(produto.id==_ID):
            print(f"Atualizando dados do Produto {produto.nome_pro}: ")
            if(cargo=="2"):
                produto.nome_pro = input("Novo nome: ")
                produto.marca = input("Nova marca: ")
            produto.quantidade = input("Quantidade do Produto em Estoque: ")
            break
        else:
            print("\n Produto não Encontrado!!")
    salvarprodutos(produtos)
    pausar()

def ListarProdutos():
    LimparTela()
    print("Produtos em Estoque: ")
    for produto in produtos:
        print(f"\nProduto {produto.nome_pro}: ")
        print(f"ID: {produto._ID}")
        print(f"Marca: {produto.marca}")
        print(f"Quantidade em Estoque: {produto.quantidade}")
        print(f"Preco de venda: {produto.preco_venda}")
        print(f"Preco de compra: {produto.preco_custo}")

def AlterarPreco(cargo):
    LimparTela()
    ID = input("Digite o ID do Produto que deseja Alterar preços: ")
    encontrado = False
    for produto in produtos:
        if(produto.id==ID):
            print(f"Atualizando preços do Produto {produto.nome_pro}: ")
            if(cargo=="2"):
                produto.preco_custo = input("Novo preço de Custo: ")
            produto.preco_venda = input("Preço de Venda: ")
            break
        else:
            print("\n Produto não Encontrado!!")
    salvarprodutos(produtos)
    pausar()

def Estoque(cargo):
    LimparTela()
    while True:
        print("Opções de Estoque: ")
        if(cargo=="2"):
            print("1 - Atualizar Estoque")
            print("2 - Listar Produtos")
            print("3 - Alterar Preço")
            print("4 - Sair")

            escolha = input("Escolha uma opção: ")
            if escolha == "1":
                AtualizarEstoque()
            elif escolha == "2":
                ListarProdutos(cargo)
            elif escolha == "3":
                AlterarPreco(cargo)
            elif escolha == "4":
                print("Você escolheu sair!")
                break
            else:
                print("Opção Digitada Invalida.")
        if(cargo=="1"):
            print("1 - Cadastrar ou Excluir Produtos")
            print("2 - Atualizar Estoque")
            print("3 - Listar Produtos")
            print("4 - Alterar Preço")
            print("5 - Sair")

            escolha = input("Escolha uma opção: ")
            if escolha == "1":
                CadastrarProdutos()
            elif escolha == "2":
                AtualizarEstoque(cargo)
            elif escolha == "3":
                ListarProdutos(cargo)
            elif escolha == "4":
                AlterarPreco(cargo)
            elif escolha == "5":
                print("Você escolheu sair!")
                break
            else:
                print("Opção Digitada Invalida.")

def NovaVenda(cargo):
    LimparTela()
    cpf_cliente = input("Digite o CPF do cliente que deseja fazer a venda: ")
    encontrado = False
    for cliente in clientes:
        if(cpf_cliente==cliente.cpf):
            print(f"Cliente : {cliente.nome}")
            produto_id = input("Digite o ID do produto que deseja vender: ")
            buscado = False
            for produto in produtos:
                if(produto_id==produtos):
                    print(f"Produto {produto.nome_pro}:")
                    print(f"Marca: {produto.marca}")
                    print(f"Quantidade em Estoque: {produto.quantidade}")
                    print(f"Preco de venda: {produto.preco_venda}")
                    print(F"Quantidade do Produto em Estoque: {produto.quantidade}")
                    qua = int(input("\n Digite a quantidade de Produtos que deseja vender: "))
                    compra = produto.preco_venda * qua
                    custo = produto.preco_custo * qua
                    lucro = compra - custo
                    print(f"\n O valor total da compra foi de :{compra:.2f}R$")
                    confirmar = (input("Deseja realizar a Compra? (s/n)")).lower
                    if(confirmar=="s"):
                        Venda.estoque()
                        cliente.valortotal += compra
                        horaagr = datetime.now()
                        hora = horaagr.timestamp()
                        _ID_venda = random.randit(10000,19999)
                        venda = Venda(_ID_venda, produto_id, produto.nome_pro, acessonome, acessocpf, cliente.nome, cpf_cliente, 
                                      qua, produto.preco_venda, produto.preco_custo, compra, custo, lucro, hora)
                        vendas.append(venda)
                        salvarprodutos(produtos)
                        salvarvendas(vendas)
                        pausar()
                        break
                    else:
                        print("Compra cancelada")
                    
            if not buscado:
                print("Produto não Encontrado no sistema.")
                if(cargo=="1"):
                    ver = (input("Deseja Cadastrar o produto(s/n)? ")).lower()
                    if(ver == "s"):
                        print("Levando a tela de Cadastro de Produtos")
                        pausar()
                        CadastrarProdutos()
                else:
                    break
            break
    if not encontrado:
        print("Cliente não encontrado, Levando para tela de Cadastro de Clientes...")
        pausar()
        CadastroClientes()

def CadastroClientes():
    LimparTela()
    ver = (input("Deseja ver os clientes Cadastrados s/n?")).lower()
    if(ver=="s"):
        print("Os clientes cadastrados são: ")
        for cliente in clientes:
            print(f"Cliente: {cliente.nome} - CPF: {cliente.cpf}")
    cpf = input("Digite o CPF do Cliente que deseja Cadastrar/Atualizar Dados: ")
    encontrado = False
    for cliente in clientes:
        if(cpf==cliente.cpf):
            print(f"Atualizando dados do Cliente {cliente.nome} ")
            cliente.telefone = input("Novo Telefone: ")
            cliente.endereco = input("Novo Endereco: ")
            cliente.email = input("Novo Email: ")
            encontrado = True
    if(encontrado == False):
        print("Digite os dados do novo Cliente: ")
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        endereco = input("Endereco: ")
        email = input("Email: ")
        valortotal = 0
        cliente = Cliente(nome, cpf, telefone, endereco, email, valortotal)
        clientes.append(cliente)
    
    dados_dict = [cliente.to_dict() for cliente in clientes]
    with open("clientes.json", "w") as arquivo:
        json.dump(dados_dict, arquivo, indent=4)
    pausar()

def CadastroVendedores():
    LimparTela()
    ver = (input("Deseja ver os vendedores Cadastrados s/n? ")).lower()
    if(ver=="s"):
        print("Os vendedores cadastrados são: ")
        for vendedor in vendedores:
            print(f"Cliente: {vendedor.nome} - CPF: {vendedor.cpf}")
    cpf = input("Digite o CPF do Vendedor que deseja Cadastrar/Atualizar Dados: ")
    encontrado = False
    for vendedor in vendedores:
        if(cpf==vendedor.cpf):
            print(f"Atualizando dados do Vendedor {vendedor.nome} ")
            vendedor.telefone = input("Novo Telefone: ")
            vendedor.endereco = input("Novo Endereco: ")
            vendedor.email = input("Novo Email: ")
            vendedor.senha = input("Nova Senha: ")
            encontrado = True
    if(encontrado == False):
        print("Digite os dados do novo Vendedor: ")
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        endereco = input("Endereco: ")
        email = input("Email: ")
        senha = input("Senha: ")
        vendedor = Funcionario(nome, cpf, telefone, endereco, email, senha)
        vendedores.append(vendedor)

    dados_dict = [vendedor.to_dict_vendedor() for vendedor in vendedores]
    with open("vendedor.json", "w") as arquivo:
        json.dump(dados_dict, arquivo, indent=4)
    pausar()

def CadastroGerentes():
    LimparTela()
    ver = (input("Deseja ver os vendedores Gerentes s/n?")).lower()
    if(ver=="s"):
        print("Os gerentes cadastrados são: ")
        for gerente in gerentes:
            print(f"Cliente: {gerente.nome} - CPF: {gerente.cpf}")
    cpf = input("Digite o CPF do Cliente que deseja Cadastrar/Atualizar Dados: ")
    encontrado = False
    for gerente in gerentes:
        if(cpf==gerente.cpf):
            print(f"Atualizando dados do Vendedor {gerente.nome} ")
            gerente.telefone = input("Novo Telefone: ")
            gerente.endereco = input("Novo Endereco: ")
            gerente.email = input("Novo Email: ")
            gerente.senha = input("Nova Senha: ")
            encontrado = True
    if(encontrado == False):
        print("Digite os dados do novo Vendedor: ")
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        endereco = input("Endereco: ")
        email = input("Email: ")
        senha = input("Senha: ")
        gerente = Cliente(nome, cpf, telefone, endereco, email, senha)
        gerentes.append(gerente)

    dados_dict = [gerente.to_dict_vendedor() for gerente in gerentes]
    with open("gerentes.json", "w") as arquivo:
        json.dump(dados_dict, arquivo, indent=4)
    pausar()

def FiltroHoras(cpf, status):
    z = (input("Deseja ver o Relatorio por Dia das compras(s/n)?")).lower()
    if z == "s":
        data_alvo_str_i = input("Digite a data do inicio do Período que deseja consultar (dd/mm/aaaa): ")
        data_alvo_str_f = input("Digite a data do Final do Período que deseja consultar (dd/mm/aaaa): ")
        data_alvo_i = datetime.strptime(data_alvo_str_i, "%d/%m/%y")
        data_alvo_f = datetime.strptime(data_alvo_str_f, "%d/%m/%y")
        encontrou = False
        lista = []
        for venda in vendas:
            datadia = venda.registroparahora()
            if data_alvo_i <= datadia <= data_alvo_f:
                lista.append(venda)

        if(status == "1"):
            lista_v = []
            for venda in lista:
                if(cpf==venda.cpf_vendedor):
                    lista_v.append(venda)
            LimparTela()
            print(f"Vendas feita pelo Vendedor/Gerente de CPF: {cpf}, no período de {data_alvo_str_i} a {data_alvo_str_f}: ")
            ImprimirRelatorio(lista_v)
            pausar()

        elif(status== "2"):
            lista_c = []
            for venda in lista:
                if(cpf==venda.cpf_cliente):
                    lista_c.append(venda)
            LimparTela()
            print(f"Vendas feitas ao Cliente de CPF: {cpf}, no no período de {data_alvo_str_i} a {data_alvo_str_f}:  ")
            ImprimirRelatorio(lista_c)
            pausar()
    else: 
        if(status == "1"):
            lista_v = []
            for venda in lista:
                if(cpf==venda.cpf_vendedor):
                    lista_v.append(venda)
            LimparTela()
            print(f"Vendas feita pelo Vendedor/Gerente de CPF: {cpf}: ")
            ImprimirRelatorio(lista_v)
            pausar()
        elif(status== "2"):
            lista_c = []
            for venda in lista:
                if(cpf==venda.cpf_cliente):
                    lista_c.append(venda)
            LimparTela()
            print(f"Vendas feitas ao Cliente de CPF: {cpf}:  ")
            ImprimirRelatorio(lista_c)
            pausar()
        elif(status == "3"):
            LimparTela()
            print("Todas as Vendas feitas: ")
            ImprimirRelatorio(vendas)
            pausar()
            
def ImprimirRelatorio(lista):
    somalucro = 0
    somacusto = 0
    somavenda= 0
    for venda in lista:
        data = venda.registroparahora()
        print(f"Venda de ID: {venda._ID_venda}, realizada no horario: {data}")
        print(f"Produto {venda.nome_produto}, de ID {venda._ID_produto}")
        print(f"Vendedor/Gerente que realizou a Compra: {venda.nome_vendedor}, de CPF: {venda.cpf_vendedor}")
        print(f"Cliente: {venda.nome_do_cliente}, de CPF {venda.cpf_cliente}")
        print(f"O preço da Venda de cada produto foi de {venda.preco_venda}R$, com custo de {venda.preco_custo}R$")
        print(f"Foram comprados: {venda.qua} produtos. Em um valor total de {venda.valortotal}R$")
        somavenda += venda.valortotal
        somacusto += venda.custototal
        somalucro += venda.lucrototal
        print(f"O lucro que foi obtido com esta compra foi de {venda.lucrototal}R$")

    print(f"O lucro total durante o periodo deste Relatorio foi de: {somalucro}R$, sendo {somavenda}R$ o Faturamento Bruto e {somacusto}R$ o Custos de Opereção.")

def Relatorio():
    LimparTela()
    while True:
        print("=====Relatorio de Vendas e Lucro=====")
        print("1 - CPF do Vendedor/Gerente que realizou a compra")
        print("2 - CPF do Cliente")
        print("3 - Sem Filtro")
        print("4 - Sair")
        x = input("Escolha uma opção de Filtro: ")
        if x == "1":
            LimparTela()
            status = 1
            y = input("Digite 1 para Gerente e 2 para Vendedor: ")
            if y == "1":
                cpf = input("Digite o CPF do Gerente: ")
                encontrado = False
                for gerente in gerentes:
                    if cpf == gerente.cpf:
                        FiltroHoras(cpf, status)
                        encontrado =  True
                if not encontrado:
                    print("Gerente não Encontrado!")
                pausar()
            elif y =="2":
                cpf = input("Digite o CPF do Vendedor: ")
                encontrado = False
                for vendedor in vendedores:
                    if cpf == vendedor.cpf:
                        FiltroHoras(cpf, status)
            if not encontrado:
                print("Vendedor não Encontrado!")
                pausar()
            else:
                print("Opção Digitada Inválida.")
        elif x == "2":
            LimparTela()
            status = "2"
            cpf = print("Digite o CPF do Cliente: ")
            encontrado =  False
            for cliente in clientes:
                if cpf == cliente.cpf:
                    FiltroHoras()
                    encontrado = True
            if not encontrado:
                print("Cliente não Encontrado!")
                pausar()
        elif x == "3":
            status = "3"
            LimparTela()
            ImprimirRelatorio()
            pausar
        elif x == "4":
            LimparTela()
            print("Você escolheu sair.")
            pausar()
            break
        else:
            LimparTela()
            print("Opção Digitada Invalida!")
            pausar()

def Menu(cargo):
    LimparTela()
    while True:
        print("=======Menu da SGP=======")
        if(cargo=="2"):
            print("1 - Estoque")
            print("2 - Nova Venda")
            print("3 - Cadastro/Atulizar Clientes")
            print("4 - Sair")

            escolha = input("\n Escolha uma opção: ")
            if escolha == "1":
                Estoque(cargo)
            elif escolha == "2":
                NovaVenda(cargo)
            elif escolha == "3":
                CadastroClientes()
            elif escolha == "4":
                print("Você Escolheu sair.")
                break
            else:
                print("Opção Digitada Invalida!")
        elif(cargo=="1"):
            print("1 - Estoque")
            print("2 - Nova Venda")
            print("3 - Cadastro/Atulizar Clientes")
            print("4 - Cadastar/Atualizar Vendedores")
            print("5 - Cadastar/Atualizar Gerentes")
            print("6 - Relátorio Financeiro")
            print("7 - Sair")

            escolha = input("\n Escolha uma opção: ")
            if escolha == "1":
                Estoque(cargo)
            elif escolha == "2":
                NovaVenda(cargo)
            elif escolha == "3":
                CadastroClientes()
            elif escolha == "4":
                CadastroVendedores()
            elif escolha == "5":
                CadastroGerentes()
            elif escolha == "6":
                Relatorio()
            elif escolha == "7":
                print("Você Escolheu sair.")
                break
            else:
                print("Opção Digitada Invalida!")

while True:
    LimparTela()
    print("=======Acesso ao Menu da SGP: =======")
    print("1 - Gerente ")
    print("2 - Vendedor")
    validador = input("Selecione seu cargo: ")
    if(validador=="1"):
        LimparTela()
        print("Opção Selecionada: Gerente")
        verificar = input("Digite seu CPF: ")
        encontrado = False

        for gerente in gerentes:
            if(verificar==gerente.cpf):
                senhat = input(f"Usuario {gerente.nome}, digite a Senha: ")
                if(gerente.senha==senhat):
                    print("Acesso Liberado!!")
                    encontrado = True
                    acessonome = gerente.nome
                    acessocpf = gerente.cpf
                    pausar()
                    Menu(validador)
                    break
                else:
                    print("Senha incorreta!!")
                    encontrado = True
                    break
        if not encontrado:
            print("\n Gerente não encontrado!")
        pausar()
    elif(validador=="2"):
        LimparTela()
        print("Opção Selecionada: Vendedor")
        verificar = input("Digite seu CPF: ")
        encontrado = False

        for vendedor in vendedores:
            if(verificar==vendedor.cpf):
                senhat = input(f"Usuario {vendedor.nome}, digite a Senha: ")
                if(vendedor.senha==senhat):
                    print("Acesso Liberado!!")
                    encontrado = True
                    acessonome = vendedor.nome
                    acessocpf = vendedor.cpf
                    pausar()
                    Menu(validador)
                    break
                else:
                    print("Senha incorreta!!")
                    encontrado = True
                    break
        if not encontrado:
            print("\n Vendedor não encontrado!")
        pausar()
    else:
        print("Opção Digitada Invalida.")
