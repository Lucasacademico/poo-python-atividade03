class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def informacao(self):
        print(f'Marca: {self.marca}, Modelo: {self.modelo}')


class Carro(Veiculo):
    def __init__(self, marca, modelo, numero_portas):
        super().__init__(marca, modelo)
        self.numero_portas = numero_portas
    
    def informacao_completa(self):
        super().informacao()
        print(f'Numero de Portas: {self.numero_portas}')

def main():

    veiculo1 = Veiculo('Mitsubishi', 'Triton')
    veiculo1.informacao()
    carro1 = Carro('Fiat', 'Strada', 2)
    carro1.informacao_completa()

if __name__ == '__main__':
    main()
