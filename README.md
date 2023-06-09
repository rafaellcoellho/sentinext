# Sentinext

Esse programa foi feito para a disciplina de Programação Paralela e Distribuida do curso de engenharia da computação no
IFCE do semestre 2023.1. O objetivo deste projeto consiste na construção de uma aplicação de chat entre
usuários, dotada de um sistema de monitoramento baseado em palavras-chave utilizando as tecnologias estudadas ao longo
do semestre, tais como MOM (Message-Oriented Middleware), RPC (Remote Procedure Call) e espaço de tuplas.

## Desenvolvimento

#### Configurando ambiente local

Instalar versão do python. Eu utilizo o [asdf](https://asdf-vm.com/), com o plugin
[asdf-python](https://github.com/asdf-community/asdf-python) para fazer isso:

```
$ asdf install python 3.10.4
```

O arquivo `.tool-versions` vai reconhecer que nessa pasta utilizamos a versão correta:

```
$ python --version
Python 3.10.4
```

Crio e iniciar o ambiente virtual:

```
$ virtualenv venv
[...]
$ . venv/bin/activate
```

Instalar as dependências de desenvolvimento:

```
$ pip install -r requirements.txt
```

Instalar a configuração do pre-commit:

```
$ pre-commit install
```

#### Compilando o binário

Instalar [PyInstaller] no ambiente virtual:

```
$ pip install pyinstaller
```

Agora basta usar a lib para criar o executável:

```
$ pyinstaller --name=sentinext --onefile src/main.py
```
