# Exercício de Programação Orientada a Objetos: Veículo e Carro

Este projeto demonstra a criação de classes em Python usando o paradigma de Programação Orientada a Objetos (POO). Ele inclui uma classe base chamada `Veiculo` e uma classe derivada chamada `Carro`.

## Estrutura do Código

### Classes

1. **Classe `Veiculo`**
   - **Atributos**:
     - `marca`: A marca do veículo.
     - `modelo`: O modelo do veículo.
   - **Métodos**:
     - `__init__(self, marca, modelo)`: Construtor que inicializa os atributos `marca` e `modelo`.
     - `informacao(self)`: Método que imprime a marca e o modelo do veículo.

2. **Classe `Carro`**
   - Herda da classe `Veiculo`.
   - **Atributos**:
     - `numero_portas`: O número de portas do carro.
   - **Métodos**:
     - `__init__(self, marca, modelo, numero_portas)`: Construtor que chama o construtor da classe `Veiculo` e inicializa `numero_portas`.
     - `informacao_completa(self)`: Método que imprime todas as informações do carro, incluindo a marca, modelo e número de portas.

### Função Principal

- **`main()`**: 
  - Cria uma instância da classe `Veiculo` e chama o método `informacao()`.
  - Cria uma instância da classe `Carro` e chama o método `informacao_completa()`.

## Como Executar o Projeto

Para executar este projeto, siga os passos abaixo:

1. **Instale o Python**: Certifique-se de ter o Python instalado em sua máquina. Você pode baixar a versão mais recente em [python.org](https://www.python.org/downloads/).

2. **Clone o Repositório**:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DA_PASTA>
