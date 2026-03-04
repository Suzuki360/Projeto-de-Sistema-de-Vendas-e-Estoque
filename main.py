from classes import *
from datetime import datetime
import os
import json
import random
import uuid

def LimparTela():
    if os.name == "nt":
        os.system(f"cls")
    else:
        os.system(f"clear")

def pausar():
    input(" \n Pressione ENTER para continuar...")

funcionarios = {}
funcionario = Funcionario("Admin", "123", "123", "algum lugar", "admin@gmail", "Senha", 1 )
v1 = Funcionario("Vendedor", "456", "456", "Seila", "vendedor@gmail.com", "Codigo", 2)
funcionarios["123"] = funcionario
funcionarios["456"] = v1
clientes = {}
produtos = {}
vendas = {}
verificar = 0

#lendoarquivosjson
if os.path.exists("funcionarios.json"):
    with open("funcionarios.json", "r") as arquivo:
        dados = json.load(arquivo)
    for cpf_fun, info in dados.items():
        funcionario_obj = Funcionario.from_dict_vendedor(info)
        funcionarios[cpf_fun] = funcionario_obj

if os.path.exists("clientes.json"):
    with open("clientes.json", "r") as arquivo:
        dados = json.load(arquivo)
    for cpf_cli, info in dados.items():
        cliente_obj = Cliente.from_dict(info)
        clientes[cpf_cli] = cliente_obj

if os.path.exists("produtos.json"):
    with open("produtos.json", "r") as arquivo:
        dados = json.load(arquivo)
    #transformando Lista em Json para Objeto
    for id_pro, info in dados.items():
        prod_obj = Produto.from_dict_produto(info)
        produtos[id_pro] = prod_obj

if os.path.exists("vendas.json"):
    with open("vendas.json", "r") as arquivo:
        dados = json.load(arquivo)
    for id_venda, info in dados.items():
        venda_obj = Venda.from_dict_venda(info)
        vendas[id_venda] = venda_obj

def Verificarfunc(verificar):
    if verificar in funcionarios:
        return True
    else:
        return False

    pausar()

def verificarclientes(verificar):
    if verificar in clientes:
        return True
    else:
        return False

def salvarprodutos(lista):
    prod_temp = {id_venda: v.to_dict() for id_venda, v in produtos.items()}
    with open("produtos.json", "w") as arquivo:
        json.dump(prod_temp, arquivo, indent=4)

def salvarvendas(lista):
    vendas_temp = {id_venda: v.to_dict() for id_venda, v in vendas.items()}
    with open("vendas.json", "w") as arquivo:
        json.dump(vendas_temp, arquivo, indent=4)

def Encontrarproduto(_ID):
    if _ID in produtos:
        return True
    else:
        False

def CadastrarProdutos():
    LimparTela()
    opcao = input("Voce deseja (Cadastrar produtos - 1) ou (Excluir Produto - 2)? ")
    if(opcao == "1"):
        nome_pro = input("Digite o Nome do Produto: ")
        _ID = input("Digite o ID do Produto: ").strip()
        marca = input("Marca: ")
        quantidade = input("Quantidade: ")
        preco_venda = input("Preço Vendido: ")
        preco_custo = input("Preço de Compra: ")
    elif opcao=="2":
        _ID = input("Digite o ID do Produto que deseja apagar: ").strip()
        encontrado = Encontrarproduto(_ID)
        if encontrado:
            print(f"Produto {produtos[_ID].nome_pro} removido com sucesso! ")
            del produtos[_ID]
            produtos.remove(produto)
        if not encontrado:
            print("\n[!] ID não encontrado.")

    produto = Produto(nome_pro, _ID, marca, quantidade,preco_venda, preco_custo)
    produtos[_ID] = produto
    salvarprodutos(produtos)
    pausar()

def AtualizarEstoque(cpf):
    LimparTela()
    _ID = input("Digite o ID do Produto que deseja atualizar: ").strip()
    encontrado = Encontrarproduto(_ID)
    if encontrado:
        print(f"Atualizando dados do Produto {produtos[_ID].nome_pro}: ")
        if(funcionarios[cpf].cargo == 1):
            produtos[_ID].nome_pro = input("Novo nome: ")
            produtos[_ID].marca = input("Nova marca: ")
        produtos[_ID].quantidade = input("Quantidade do Produto em Estoque: ")
    if not encontrado:
        print("\n Produto não Encontrado!!")
    salvarprodutos(produtos)
    pausar()

def ListarProdutos():
    LimparTela()
    print("Produtos em Estoque: ")
    for produto in produtos.values():
        print(f"\nProduto {produto.nome_pro}: ")
        print(f"ID: {produto._ID}")
        print(f"Marca: {produto.marca}")
        print(f"Quantidade em Estoque: {produto.quantidade}")
        print(f"Preco de venda: {produto.preco_venda}")
        print(f"Preco de compra: {produto.preco_custo}")

def AlterarPreco(cpf):
    LimparTela()
    _ID = input("Digite o ID do Produto que deseja Alterar preços: ").strip()
    encontrado = Encontrarproduto(cpf)
    if encontrado:
        print(f"Atualizando preços do Produto {produtos[_ID].nome_pro}: ")
        if(produtos[_ID].cargo==1):
            produtos[_ID].preco_custo = input("Novo preço de Custo: ")
        produtos[_ID].preco_venda = input("Preço de Venda: ")
    if not encontrado:
        print("\n Produto não Encontrado!!")
    salvarprodutos(produtos)
    pausar()

def Estoque(cpf):
    LimparTela()
    while True:
        print("Opções de Estoque: ")
        print("1 - Atualizar Estoque")
        print("2 - Listar Produtos")
        print("3 - Alterar Preço")
        if(funcionarios[cpf].cargo == 1):
            print("4 - Cadastrar ou Excluir Produtos")
        print("5 - Sair")

        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            AtualizarEstoque(cpf)
        elif escolha == "2":
            ListarProdutos(cpf)
        elif escolha == "3":
            AlterarPreco(cpf)
        if(funcionarios[cpf].cargo == 1):
            if escolha == "4":
                    CadastrarProdutos()
            else:
                print("Opção Digitada Invalida.")
        elif escolha == "5":
            print("Você escolheu sair!")
            break 
        else:
            print("Opção Digitada Invalida.")
    pass

def NovaVenda(cpf):
    LimparTela()
    cpf_cliente = input("Digite o CPF do cliente que deseja fazer a venda: ")
    encontrado = verificarclientes(cpf_cliente)
    if encontrado:
        print(f"Cliente : {clientes[cpf].nome}")
        produto_id = input("Digite o ID do produto que deseja vender: ").strip()
        buscado = Encontrarproduto(produto_id)
        if buscado:
            print(f"Produto {produtos[produto_id].nome_pro}:")
            print(f"Marca: {produtos[produto_id].marca}")
            print(f"Quantidade em Estoque: {produtos[produto_id].quantidade}")
            print(f"Preco de venda: {produtos[produto_id].preco_venda}")
            qua = int(input("\n Digite a quantidade de Produtos que deseja vender: "))
            compra = float(produtos[produto_id].preco_venda) * qua
            custo = produtos[produto_id].preco_custo * qua
            lucro = compra - custo
            print(f"\n O valor total da compra foi de :{compra:.2f}R$")
            confirmar = (input("Deseja realizar a Compra? (s/n)")).lower()
            if(confirmar=="s"):
                produtos[produto_id].quantidade = int(produtos[produto_id].quantidade) - qua
                clientes[cpf_cliente].valortotal += compra
                horaagr = datetime.now()
                hora = horaagr.timestamp()
                _ID_venda = str(uuid.uuid4()).split('-')[0].upper()
                venda = Venda(_ID_venda, produto_id, produtos[produto_id].nome_pro, funcionarios[cpf].nome, cpf, clientes[cpf_cliente].nome, cpf_cliente, 
                                      qua, produtos[produto_id].preco_venda, produtos[produto_id].preco_custo, compra, custo, lucro, hora)
                vendas[_ID_venda] = venda
                salvarprodutos(produtos)
                salvarvendas(vendas)
                pausar()
            else:
                 print("Compra cancelada")
                    
        if not buscado:
            print("Produto não Encontrado no sistema.")
            if(funcionarios[cpf].cargo == 1):
                ver = (input("Deseja Cadastrar o produto(s/n)? ")).lower()
                if(ver == "s"):
                    print("Levando a tela de Cadastro de Produtos")
                    pausar()
                    CadastrarProdutos()
    if not encontrado:
        print("Cliente não encontrado, Levando para tela de Cadastro de Clientes...")
        pausar()
        CadastroClientes()

def CadastroClientes():
    LimparTela()
    ver = (input("Deseja ver os clientes Cadastrados s/n?")).lower()
    if(ver=="s"):
        print("Os clientes cadastrados são: ")
        for cliente in clientes.values():
            print(f"Cliente: {cliente.nome} - CPF: {cliente.cpf}")
    cpf = input("Digite o CPF do Cliente que deseja Cadastrar/Atualizar Dados: ").strip()
    encontrado = verificarclientes(cpf)
    if encontrado:
        print(f"Atualizando dados do Cliente {clientes[cpf].nome} ")
        clientes[cpf].telefone = input("Novo Telefone: ")
        clientes[cpf].endereco = input("Novo Endereco: ")
        clientes[cpf].email = input("Novo Email: ")
    if not encontrado:
        print("Digite os dados do novo Cliente: ")
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        endereco = input("Endereco: ")
        email = input("Email: ")
        valortotal = 0
        cliente = Cliente(nome, cpf, telefone, endereco, email, valortotal)
        clientes[cpf] = cliente
    
    client_temp = {id_venda: v.to_dict() for id_venda, v in clientes.items()}
    with open("clientes.json", "w") as arquivo:
        json.dump(client_temp, arquivo, indent=4)
    pausar()

def CadastroFuncionario(cpf):
    LimparTela()
    ver = (input(f"Deseja ver os Funcionarios Cadastrados s/n? ")).lower()
    if(ver=="s"):
        print("Os Funcionários cadastrados são: ")
        print("Gerentes: ")
        for funcionario in [f for f in funcionarios.values() if f.cargo == 1]:
            print(f"Cliente: {funcionario.nome} - CPF: {funcionario.cpf}")
        print("Vendedores: ")   
        for funcionario in [f for f in funcionarios.values() if f.cargo == 2]:
            print(f"Cliente: {funcionario.nome} - CPF: {funcionario.cpf}") 
            pausar()
        cpfcadastro = ("Digite o CPF do Vendedor/Gerente que deseja Cadastrar/Atualizar Dados: ").strip()
        encontrado = Verificarfunc(cpfcadastro)

        if encontrado:
            print(f"Atualizando dados do Vendedor {funcionario[cpfcadastro].nome},(caso não queira atulizar, digite o valor antigo)")
            funcionario[cpfcadastro].telefone = input("Novo Telefone: ")
            funcionario[cpfcadastro].endereco = input("Novo Endereco: ")
            funcionario[cpfcadastro].email = input("Novo Email: ")
            funcionario[cpfcadastro].senha = input("Nova Senha: ")
            funcionario[cpfcadastro].cargo = int(input("Cargo do Funcionário, sendo 1 para Gerente e 2 para Vendedor: "))

    if not encontrado: 
        print("Digite os dados do Funcionário: ")
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        endereco = input("Endereco: ")
        email = input("Email: ")
        senha = input("Senha: ")
        cargo = int("Cargo do Funcionário, sendo 1 para Gerente e 2 para Vendedor: ")
        funcionario = Funcionario(nome, cpf, telefone, endereco, email, senha, cargo)
        funcionarios[cpfcadastro] = funcionario

    funcionario_temp = {id_venda: v.to_dict() for id_venda, v in funcionarios.items()}

    with open("funcionarios.json", "w") as arquivo:
        json.dump(funcionario_temp, arquivo, indent=4)

def FiltroHoras(cpf, status):
    z = (input("Deseja ver o Relatorio por Dia das compras(s/n)?")).lower()
    venda_to_filter = vendas.values()
    if z == "s":
        data_alvo_str_i = input("Digite a data do inicio do Período que deseja consultar (dd/mm/aaaa): ")
        data_alvo_str_f = input("Digite a data do Final do Período que deseja consultar (dd/mm/aaaa): ")
        data_alvo_i = datetime.strptime(data_alvo_str_i, "%d/%m/%Y")
        data_alvo_f = datetime.strptime(data_alvo_str_f, "%d/%m/%Y")
        venda_to_filter = [v for v in vendas.values() if data_alvo_i <= v.registroparahora() <= data_alvo_f]
        LimparTela()
        print(f"Vendas feitas no período de {data_alvo_str_i} há {data_alvo_str_f}")
    if(status == "1"):
        venda_to_filter = [v for v in venda_to_filter if v.cpf_vendedor== cpf]
        print(f" Vendas feitas pelo Vendedor/Funcionário {funcionarios[cpf].nome}:")
    elif(status== "2"):
        venda_to_filter = [v for v in venda_to_filter if v.cpf_cliente== cpf]
        print(f" Vendas feitas para o Cliente {clientes[cpf].nome}:")
    else:
        print("Todas as vendas feitas: ")

    ImprimirRelatorio(list(venda_to_filter))
    pausar()
            
def ImprimirRelatorio(lista):
    LimparTela()
    somalucro = 0
    somacusto = 0
    somavenda= 0
    for venda in lista:
        data = venda.registroparahora()
        print(f"Venda de ID: {venda._ID_venda}, realizada no horario: {data}")
        print(f"Produto {venda.nome_produto}, de ID {venda._ID_produto}")
        print(f"Vendedor/Gerente que realizou a Compra: {venda.nome_vendedor}, de CPF: {venda.cpf_vendedor}")
        print(f"Cliente: {venda.nome_do_cliente}, de CPF {venda.cpf_cliente}")
        print(f"O preço da Venda de cada produto foi de {venda.preco_venda}R$, com custo de {venda.preco_custo:.2f}R$")
        print(f"Foram comprados: {venda.qua} produtos. Em um valor total de {venda.valortotal:.2f}R$")
        somavenda += venda.valortotal
        somacusto += venda.custototal
        somalucro += venda.lucrototal
        print(f"O lucro que foi obtido com esta compra foi de {venda.lucrototal:.2f}R$")

    print(f"O lucro total durante o periodo deste Relatorio foi de: {somalucro}R$, sendo {somavenda}R$ o Faturamento Bruto e {somacusto}R$ o Custos de Opereção.")
    print(f"\n ---------------------------------------------------------------------------------------------------------------------------------------------------------")

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
            cpf_func = input("Digite o CPF do Vendedor/Gerente: ")
            encontrado = Verificarfunc(cpf_func)
            if encontrado:
                FiltroHoras(cpf_func, status)
            if not encontrado:
                print("Vendedor/Gerente não Encontrado!")
                pausar()
        elif x == "2":
            LimparTela()
            status = "2"
            cpf_clie = input("Digite o CPF do Cliente: ")
            encontrado = verificarclientes(cpf_clie)
            if encontrado:
                FiltroHoras(cpf_clie, status)
            if not encontrado:
                print("Cliente não Encontrado!")
                pausar()
        elif x == "3":
            status = "3"
            ImprimirRelatorio(vendas)
            pausar()
        elif x == "4":
            print("Você escolheu sair.")
            pausar()
            break
        else:
            print("Opção Digitada Invalida!")
            pausar()

def Menu(cpf):
    LimparTela()
    while True:
        print("=======Menu da SGP=======")
        print("1 - Estoque")
        print("2 - Nova Venda")
        print("3 - Cadastro/Atulizar Clientes")
        if(funcionarios[cpf].cargo == 1):
            print("4 - Cadastar/Atualizar Funcionarios(Vendedores ou Gerentes)")
            print("5 - Relátorio Financeiro")
        print("9 - Sair")
        escolha = input("\n Escolha uma opção: ")
        if escolha == "1":
            Estoque(cpf)
        elif escolha == "2":
            NovaVenda(cpf)
        elif escolha == "3":
            CadastroClientes()
        if(funcionarios[cpf].cargo == 1):
            if escolha == "4":
                CadastroFuncionario(cpf)
            elif escolha == "5":
                Relatorio()
            elif escolha != ("1", "2", "3", "4", "5","9"):
                print("Opção Digitada Invalida!")
                pausar()
        elif escolha == "9":
            print("Você Escolheu sair.")
            break
        elif escolha != ("1", "2", "3", "4", "5","9"):
            print("Opção Digitada Invalida!")
            pausar()

while True:
    LimparTela()
    print("=======Acesso ao Menu da SGP: =======")
    cpf = input("Digite seu CPF: ").strip()
    ver = Verificarfunc(cpf)
    if ver:
        senha = input("Digite sua Senha: ")
        if senha == funcionarios[cpf].senha:
            print("Acesso Liberado!!")
            pausar()
            Menu(cpf)
            break
        else:
            print("Senha incorreta!!")
            break
    if not ver:
        print("\n CPF não encontrado, Procure um Gerente.")
        pausar()