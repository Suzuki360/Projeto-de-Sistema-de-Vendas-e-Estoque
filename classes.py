from datetime import datetime

class Pessoa:
    def __init__(self, nome, cpf, telefone,endereco, email):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        self.email = email

    def to_dict(self):
        return {
            "nome" : self.nome,
            "cpf": self.cpf,
            "telefone" : self.telefone,
            "endereco":self.endereco,
            "email":self.email
        }
    
    #função que trasnforma Lista de Dicionarios em Objeto
    @classmethod
    def from_dict(cls, dados):
        return cls(
            dados["nome"],
            dados["cpf"],
            dados["telefone"],
            dados["endereco"],
            dados["email"]
        )

class Funcionario(Pessoa):
    def __init__(self,nome, cpf, telefone,endereco, email, senha):
        # O super() manda os dados para o __init__ de Pessoa
        super().__init__(nome, cpf, telefone, endereco, email)
        self.senha = senha

    #função que trasnforma Objeto em Lista de Dicionarios
    def to_dict_vendedor(self):
        return {
            "nome" : self.nome,
            "cpf": self.cpf,
            "telefone" : self.telefone,
            "endereco":self.endereco,
            "email":self.email,
            "senha":self.senha
        }
    
    @classmethod
    def from_dict_vendedor(cls,dados):
        return cls(
            dados["nome"],
            dados["cpf"],
            dados["telefone"],
            dados["endereco"],
            dados["email"],
            dados["senha"]
        )

class Gerente(Funcionario):
    def __init__(self,nome, cpf, telefone,endereco, email, senha):
        super().__init__(nome, cpf, telefone, endereco, email,senha)

class Cliente(Pessoa): 
    def __init__(self, nome, cpf,telefone, endereco, email, valortotal):
        super().__init__(nome, cpf, telefone, endereco, email)
        self.valortotal = valortotal

class Produto:
    def __init__(self, nome_pro,_ID, marca, quantidade, preco_venda, preco_custo, quantidade_min = 5 ):
        self.nome_pro = nome_pro
        self._ID = _ID
        self.marca = marca
        self.quantidade = quantidade
        self.preco_venda = preco_venda
        self.preco_custo = preco_custo
        self.quantidade_min = quantidade_min

    def quantidadeMin(self):
        return self.quantidade<self.quantidade_min
    
    def to_dict_produto(self):
        return{
            "nome_pro": self.nome_pro,
            "_ID": self._ID,
            "marca": self.marca,
            "quantidade" : self.quantidade,
            "preco_venda": self.preco_venda,
            "preco_custo": self.preco_custo,
        }
    
    @classmethod
    def from_dict_produto(cls, dados):
        return cls(
            dados["nome_pro"],
            dados["_ID"],
            dados["marca"],
            dados["quantidade"],
            dados["preco_venda"],
            dados["preco_custo"]
        )

class Venda:
    def __init__(self, _ID_venda, _ID_produto, nome_produto, nome_vendedor, cpf_vendedor, nome_do_cliente,
                 cpf_cliente, qua, preco_venda, preco_custo, valortotal,custototal, lucrototal, data_hora):
        self._ID_venda = _ID_venda
        self._ID_produto = _ID_produto
        self.nome_produto = nome_produto
        self.nome_vendedor = nome_vendedor
        self.cpf_vendedor = cpf_vendedor
        self.nome_do_cliente =nome_do_cliente
        self.cpf_cliente = cpf_cliente
        self.qua = qua
        self.preco_venda = preco_venda
        self.preco_custo = preco_custo
        self.valortotal = valortotal
        self.custototal = custototal
        self.lucrototal = lucrototal
        self.data_hora = data_hora

    def to_dict_venda(self):
        return{
            "_ID_venda": self._ID_venda,
            "_ID_produto": self._ID_produto,
            "nome_produto": self.nome_produto,
            "nome_vendedor" : self.nome_vendedor,
            "cpf_vendedor": self.cpf_vendedor,
            "nome_do_cliente": self.nome_do_cliente,
            "cpf_cliente": self.cpf_cliente,
            "qua": self.qua,
            "preco_venda": self.preco_venda,
            "preco_custo" : self.preco_custo,
            "valortotal": self.valortotal,
            "custototal": self.custototal,
            "lucrototal" : self.lucrototal,
            "data_hora": self.data_hora,
        }
    
    @classmethod
    def from_dict_venda(cls, dados):
        return cls(
            dados["_ID_venda"],
            dados["_ID_produto"],
            dados["nome_produto"],
            dados["nome_vendedor"],
            dados["cpf_vendedor"],
            dados["nome_do_cliente"],
            dados["cpf_cliente"],
            dados["qua"],
            dados["preco_venda"],
            dados["preco_custo"],
            dados["valortotal"],
            dados["custototal"],
            dados["lucrototal"],
            dados["data_hora"],
        )
        

    def registroparahora(self):
        diahora = datetime.fromtimestamp(self.data_hora)
        return diahora