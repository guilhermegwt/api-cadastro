# API de Cadastro de Usuário

## Requisitos

  Python 3.10 ou superior  
  python3-pip  
  python3-virtualenv  
  git  
  
## Instalação

### Ubuntu, Mint e derivados

- git clone https://github.com/guilhermegwt/api-cadastro.git  
- cd api-cadastro/  
- chmod +x install.sh  
- ./install.sh  
- Acessar a API no pela url: http://localhost:8000/api/v1/usuarios  

O serviço será executado automaticamente na porta 8000 (verifique se não há outro serviço em execução utilizando essa porta)  

### Windows

- Acessar o diretório api-cadastro  
- Configurar um ambiente virtual com Virtualenv  
- Ativar ambiente virtual  
- Instalar os seguintes pacotes utilizando o pip:  
  - django  
  - djangorestframework  
  - djangorestframework-csv  
  - drf-excel  
- Executar as configurações do Banco de Dados utilizando os seguintes comandos:  
  - python manage.py makemigrations cadastro  
  - python manage.py migrate  
- Executar o API com o comando:  
  - python manage.py runserver  
- Acessar a API no pela url: http://localhost:8000/api/v1/usuarios  

O serviço será executado na porta 8000, verifique se não há outro serviço em execução utilizando essa porta  

## Fazendo Requisições com a API

- GET / url: http://localhost:8000/api/v1/usuarios -> Acessa a API e retornar uma lista de usuários cadastrados  

- GET / url: http://localhost:8000/api/v1/usuarios.json -> Irá retornar uma lista em formato JSON com os usuários cadastrados  

- GET / url: http://localhost:8000/api/v1/usuarios.xlsx -> Irá retornar um arquivo em formato XLSX com os usuários cadastrados  

- GET / url: http://localhost:8000/api/v1/usuarios.csv -> Irá retornar um arquivo em formato CSV com os usuários cadastrados   

- POST / url: http://localhost:8000/api/v1/usuarios -> Preenchendo os campos login, senha e data_nascimento ou enviando {"login": "usuario123", "senha": "usuario12345", "data_nascimento": "1900-01-01"} irá gravar os dados no Banco de Dados. OBS.: O campo senha não é obrigatório, se não for preenchido, irá gerar automaticamente uma senha de 12 caracteres  

- PUT / url: http://localhost:8000/api/v1/usuarios/{id} -> Utilizando o método PUT e informando o **ID** de um usuário cadastrado, você pode atualizar o registro informando novos dados  

- DELETE / url: http://localhost:8000/api/v1/usuarios/{id} -> Utilizando o método DELETE e informando o **ID** de um usuário cadastrado, você efetuará a exclusão desse registro  

