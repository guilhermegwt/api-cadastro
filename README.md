# API de Cadastro de Usuário

# Requisitos

  Python 3.10 ou superior  
  python3-pip  
  python3-virtualenv  

# Instalação

# Ubuntu, Mint e derivados

  git clone https://github.com/guilhermegwt/api-cadastro.git  
  cd api-cadastro/  
  chmod +x install.sh  
  ./install.sh  

# Windows

.  Acessar o diretório api-cadastro  
.  Configurar um ambiente virtual com Virtualenv  
.  Ativar ambiente virtual  
.  Instalar os seguintes pacotes utilizando o pip:  
    django  
    djangorestframework 3.14.0  
    djangorestframework-csv 2.1.1  
    drf-excel 2.2.0  
.  Iniciar e executar as configurações do Banco de Dados utilizando os seguintes comandos:  
    python manage.py makemigrations cadastro  
    python manage.py migrate  
.  Executar o API com o seguinte comando (O serviço será executado na porta 8000):  
    python manage.py runserver  
.  Acessar a API no pela url: http://localhost:8000/api/v1/cadastros  
  

  
