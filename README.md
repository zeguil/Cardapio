# Cardapio

Projeto INOVATEC 2022

### 🎲 Rodando a API

```bash
# Clone este repositório
$ git clone <https://github.com/Cardapio>

# Acesse a pasta do projeto no terminal/cmd
$ cd Cardapio

# Instale o virtualenv
$ pip install virtualenv 

# Crie um ambiente virtual
$ virtualenv venv (windows)
$ python3 -m venv venv (linux)

# Acesse o ambiente virtual
$ venv/Scripts/activate (windows)
$ source venv/bin/activate (linux)

#  Instale as bibliotecas necessarias 
$ pip install -r requirements.txt

# Execute a aplicação no terminal
$ python manage.py runserver

# O servidor inciará na porta:8000 - acesse <http://localhost:8000/api/v1/>
# Para ver a documentação e todos os endpoints disponiveis - acesse <http://localhost:8000/api/v1/swagger/>