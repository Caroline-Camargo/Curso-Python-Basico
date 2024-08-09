'''O banco Banco Delas é um banco moderno e eficiente, com
vantagens exclusivas para clientes mulheres.
Modele um sistema orientado a objetos para representar contas
correntes do Banco Delas seguindo os requisitos abaixo.
● Cada conta corrente pode ter um ou mais clientes como
titular.
● O banco controla apenas o nome, o telefone e a renda
mensal de cada cliente.
● A conta corrente apresenta um saldo e uma lista de
operações de saques e depósitos.
● Quando a cliente fizer um saque, diminuiremos o saldo da
conta corrente. Quando ela fizer um depósito,
aumentaremos o saldo.
● Clientes mulheres possuem em suas contas um cheque
especial de valor igual à sua renda mensal, ou seja, elas
podem sacar valores que deixam a sua conta com valor
negativo até renda_mensal.
● Clientes homens por enquanto não têm direito a cheque
especial.
Para modelar seu sistema, utilize obrigatoriamente os conceitos
"classe", "herança", "propriedades", "encapsulamento" e "classe
abstrata'''

from abc import ABC, abstractmethod

class Cliente(ABC):
    def __init__(self, nome, telefone, rendaMensal):
        self.nome = nome
        self.__telefone = telefone
        self.__rendaMensal = rendaMensal
        self.__conta_corrente = None
    
    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone):
        if len(telefone) >= 11:
            self.__telefone = telefone
        else:
            raise ValueError('Telefone inválido, o telefone deve ter 11 dígitos: (xx) x xxxx-xxxx')
    
    @property
    def rendaMensal(self):
        return self.__rendaMensal
    
    @rendaMensal.setter
    def rendaMensal(self, rendaMensal):
        if isinstance(rendaMensal, (float, int)) and rendaMensal >= 0:
            self.__rendaMensal = rendaMensal
        else:
            raise ValueError('Renda mensal inválida, a renda mensal deve ser um número maior ou igual a 0')
        
    @property
    def conta_corrente(self):
        return self.__conta_corrente
    
    @conta_corrente.setter
    def conta_corrente(self, conta_corrente):
        if isinstance(conta_corrente, ContaCorrente):
            self.__conta_corrente = conta_corrente
        else:
            raise ValueError('Conta corrente inválida, não foi possível adicionar a conta corrente')
    
    def adicionar_conta_corrente_existente(self, conta):
        conta.titulares_conta = self
        self.conta_corrente = conta
        return conta
    
    @abstractmethod
    def criar_conta_corrente(self, saldo):
        pass
        
    def __str__(self) -> str:
        string = (f'Nome: {self.nome}\n'
                f'Telefone: {self.telefone}\n'
                f'Renda Mensal: R$ {self.rendaMensal}\n')
        
        if self.__conta_corrente == None:
            string += 'Não há conta corrente vinculada a este cliente\n'
        else:
            string += f'Conta Corrente: {self.conta_corrente}\n'
        return string


class ClienteMulher(Cliente):
    def __init__(self, nome, telefone, rendaMensal):
        super().__init__(nome, telefone, rendaMensal)
    
    def criar_conta_corrente(self, saldo):
        conta = ContaCorrente(saldo, self.rendaMensal)
        conta.titulares_conta = self
        self.conta_corrente = conta
        return conta

class ClienteHomen(Cliente):
    def __init__(self, nome, telefone, rendaMensal):
        super().__init__(nome, telefone, rendaMensal)
    
    def criar_conta_corrente(self, saldo):
        conta = ContaCorrente(saldo, 0.0)
        conta.titulares_conta = self
        self.conta_corrente = conta
        return conta


class ContaCorrente():
    def __init__(self, saldo, cheque_especial):
        self.__saldo = saldo
        self.__cheque_especial = cheque_especial
        self.__titulares_conta = []
        self._lista_operacoes = []
        self._lista_operacoes.append(f'Conta Criada! Saldo inicial de R$ {saldo}')
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo):
        if isinstance(saldo, (float, int)):
            self.__saldo = saldo
        else:
            raise ValueError('Saldo inválido, o saldo deve ser um número')
    
    @property
    def titulares_conta(self):
        return self.__titulares_conta
    
    @titulares_conta.setter
    def titulares_conta(self, titular):
        if isinstance(titular, Cliente):
            self.__titulares_conta.append(titular)
        else:
            raise ValueError('Titular inválido, não foi possível adicionar o titular')

    def depositar_dinheiro(self, valor_deposito):
        if isinstance(valor_deposito, (float, int)) and valor_deposito > 0:    
            self.saldo += valor_deposito
            self._lista_operacoes.append(f'Depósito de R$ {valor_deposito}')
        else:
            raise ValueError('Valor de depósito inválido, o valor de depósito deve ser um número')
    
    def sacar_dinheiro(self, valor_saque):
        if not isinstance(valor_saque, (float, int)):
            raise ValueError('Valor de saque inválido, o valor de saque deve ser um número')
        
        if valor_saque <= 0:
            raise ValueError('Valor de saque inválido, o valor de saque deve ser maior que 0')
        
        if valor_saque <= self.saldo:
            self.saldo -= valor_saque
            self._lista_operacoes.append(f'Saque de R$ {valor_saque}')
        else:
            if valor_saque <= self.saldo + self.__cheque_especial:
                self.__cheque_especial -= valor_saque - self.saldo
                self.saldo = 0
                self._lista_operacoes.append(f'Saque de R$ {valor_saque}')
                self._lista_operacoes.append(f'Cheque Especial de R$ {self.__cheque_especial}')
            else:
                print('Saldo insuficiente, não foi possível realizar o saque')	
                self._lista_operacoes.append(f'Não foi possível realizar o saque R$ {valor_saque}, saldo insuficiente')
    
    def adicionar_titular(self, titular):
        if isinstance(titular, Cliente):
            self.titulares_conta = titular
        else:
            raise ValueError('Titular inválido, não foi possível adicionar o titular')

    def imprimir_extrato(self):
        print(f'Saldo Atual: R$ {self.saldo}')
        print(f'\nHistórico: ')
        for operacao in self._lista_operacoes:
            print(operacao)
        print('\n')

    def __str__(self) -> str:
        titulares = ''
        for titular in self.titulares_conta:
            titulares += f'{titular.nome}, '

        return f'\n\tSaldo: R$ {self.saldo} \n\tCheque Especial: R$ {self.__cheque_especial} \n\tTitulares da conta: {titulares}'



cliente_caroline = ClienteMulher('Caroline', '11999999999', 2000)
print(cliente_caroline)
cliente_caroline.criar_conta_corrente(1000)
print(cliente_caroline)


cliente_caroline.conta_corrente.depositar_dinheiro(500)
cliente_caroline.conta_corrente.sacar_dinheiro(200)
cliente_caroline.conta_corrente.sacar_dinheiro(1500)
cliente_caroline.conta_corrente.imprimir_extrato()


cliente_joao = ClienteHomen('João', '11888888888', 1000)
cliente_joao.adicionar_conta_corrente_existente(cliente_caroline.conta_corrente)
print(cliente_joao) 
cliente_joao.conta_corrente.depositar_dinheiro(1000)
cliente_joao.conta_corrente.sacar_dinheiro(3000)
cliente_joao.conta_corrente.imprimir_extrato()




