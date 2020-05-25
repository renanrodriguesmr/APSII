# APSII

APSII é um pequeno projeto para responder 3 questões sobre o ensino fundamental brasileiro, para a avaliação na matéria Análise de Projetos e Sistemas II do IME.

As questões são:
- Quais as principais características que levam uma escola à ter um alto índice de reprovação, ou seja, por que uma escola reprova muito?
- Escolas particulares possuem um maior índice de reprovação do que as escolas públicas?
- A taxa de reprovação aumenta ao longo do ensino fundamental?

## Installation

O projeto possui um make file para prover a instalação. Então, basta realizar o seguinte comando:

```bash
make install
```

A instalação pode ser feita manualmente através do seguinte comando:

```bash
pip install -r requirements.txt
```

É recomendado a criação de um [virtual environment](https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais) antes da instalação.

## Data

É recomendado a criação de um diretório .data/ para armazenar os datasets que serão utilizados no projeto.

## Usage

```bash
make run
```

ou 

```bash
python3 main.py
```

## Running Tests

python -m tests

## License
[MIT](https://choosealicense.com/licenses/mit/)
