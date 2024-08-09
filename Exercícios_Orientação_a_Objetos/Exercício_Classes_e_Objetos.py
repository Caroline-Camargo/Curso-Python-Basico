'''1. Crie uma classe que modele o objeto "carro".
2. Um carro tem os seguintes atributos: ligado, cor, modelo,
velocidade.
3. Um carro tem os seguintes comportamentos: liga, desliga, acelera,
desacelera.
4. Crie uma instância da classe carro.
5. Faça o carro "andar" utilizando os métodos da sua classe.
6. Faça o carro "parar" utilizando os métodos da sua classe.'''

class Carro:
    def __init__(self, ligado: bool, cor: str, modelo: str, velocidade: float) -> None:
        self.ligado = ligado
        self.cor = cor
        self.modelo = modelo
        self.velocidade = velocidade
    
    def __str__(self) -> str:
        string = (f'Carro: {"Ligado" if self.ligado else "Desligado"}\n'
                f'Cor: {self.cor}\n'
                f'Velocidade: {self.velocidade} km/h\n'
                f'Ligado: {self.ligado}\n\n')
        return string

    
    def ligar(self):
        if self.ligado:
            print('\nO carro já está ligado')
        else:
            self.ligado = True
            print('\nO carro foi ligado')

    def desligar(self):
        if self.ligado:
            self.ligado = False
            self.velocidade = 0
            print('\nO carro foi desligado')
        else:
            print('\nO carro já está desligado')
    
    def acelerar(self):
        if self.ligado:
            self.velocidade += 1
            print(f'\nVelocidade: {self.velocidade} km/h')
        else:
            print('\nO carro precisa estar ligado para acelerar')

    def desacelerar(self):
        if self.ligado:
            if self.velocidade == 0:
                print('\nO carro está parado')
            else:
                self.velocidade -= 1
            print(f'\nVelocidade: {self.velocidade} km/h')
        else:
            print('\nO carro precisa estar ligado para desacelerar')

    def parar(self):
        if self.ligado:
            print('\nParando o carro... Freada brus')
            self.velocidade = 0
            print('O carro parou')
        else:
            print('\nO carro precisa estar ligado para parar')


meu_carro = Carro(False, 'Vermelho', 'BMW', 0)
print(meu_carro)

meu_carro.ligar()

for _ in range(10):
    meu_carro.acelerar()

print('Sinal Vermelho')

for _ in range(3):
    meu_carro.desacelerar()

meu_carro.parar()
meu_carro.desligar()

