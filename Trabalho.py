class Projeto():
    nome = None
    descricao = None
    def __init__(self, nome = None, descricao = None):
        self.nome = nome
        self.descricao = descricao

class Pessoa():
    nome = ''
    data_nascimento =''

    def __init__(self, nome = None, data_nascimento = None):
        self.nome = nome
        self.data_nascimento = data_nascimento

class PessoaFisica(Pessoa):
    cpf = None
    def __init__(self, cpf = None, nome = None, data_nascimento = None):
        Pessoa.__init__(self, nome, data_nascimento)
        self.cpf = cpf

class PessoaJuridica(Pessoa):
    cnpj = None
    def __init__(self, cnpj = None, nome = None, data_nascimento = None):
        Pessoa.__init__(self, nome, data_nascimento)
        self.cnpj = cnpj
        
class Tarefa():
    descricao = None
    data_inicio = None
    data_fim = None
    prioridade = None
    def __init__(self, descricao = None, data_inicio = None, data_fim = None, prioridade = None):
        self.descricao = descricao
        self.data_inicio = data_inicio
        seff.data_fim = data_fim
        self.prioridade = proridade
        self.projeto = Projeto()
        self.solicitacao = PessoaJuridica()
        self.atendimento = Pessoa Fisica()
