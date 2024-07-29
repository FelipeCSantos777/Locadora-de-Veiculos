class Carro:
    def __init__(self, modelo, placa, ano, cor, quilometragem, valor_diario, observacao):
        self.modelo = modelo
        self.placa = placa
        self.ano = ano
        self.cor = cor
        self.quilometragem = quilometragem
        self.valor_diario = valor_diario
        self.observacao = observacao
        
class Esportivo(Carro):
    def __init__(self, modelo, placa, ano, cor, quilometragem, valor_diario, observacao, tempo, melhorias):
        super().__init__(modelo, placa, ano, cor, quilometragem, valor_diario, observacao)
        self.tempo = tempo
        self.tempo = melhorias

class Utilitario(Carro):
    def __init__(self, modelo, placa, ano, cor, quilometragem, valor_diario, observacao, quantidade_passageiros, tamanho_bagageiro, km_litro):
        super().__init__(modelo, placa, ano, cor, quilometragem, valor_diario, observacao)
        self.quantidade_passageiros = quantidade_passageiros
        self.tamanho_bagageiro = tamanho_bagageiro
        self.km_litro = km_litro
        
class Reserva:
    def __init__(self, cpf_cliente, status, dt_inicio, dt_fim):
        self.cpf_cliente = cpf_cliente
        self.status = status
        self.dt_inicio = dt_inicio
        self.dt_fim = dt_fim
        
class Pessoa:
    def __init__(self, nome, cpf, email, telefone, endereco):
        self.nome = nome
        self.cpf = cpf
        self.emal = email
        self.telefone = telefone
        self.endereco = endereco
        
class Funcionario(Pessoa):
    def __init__(self, nome, cpf, emal, telefone, endereco, idade, dt_contratacao, salario, qd_alugueis_mes = 0, status = False):
        super().__init__(nome, cpf, emal, telefone, endereco)
        self.idade = idade
        self.dt_contratacao = dt_contratacao
        self.salario = salario
        self.qd_alugueis_mes = qd_alugueis_mes
        self.status = status
        
class Cliente(Pessoa):
    def __init__(self, nome, cpf, emal, telefone, endereco, dt_nascimento, nu_carteira, foto_carteira, dt_vencimento_carteira):
        super().__init__(nome, cpf, emal, telefone, endereco)
        self.dt_nascimento = dt_nascimento
        self.nu_carteira = nu_carteira
        self.foto_carteira = foto_carteira
        self.dt_vencimento_carteira = dt_vencimento_carteira
        
class Promocao:
    def __init__(self, titulo, descricao, dt_validade):
        self.titulo = titulo
        self.descricao = descricao
        self.dt_validade = dt_validade