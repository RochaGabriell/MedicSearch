
# Medic Search
_Este é um repositório dedicado ao treinamento de Django, e ao desenvolvimento de meus conhecimentos com o Django. Conteúdo aprendido no livro, [Django de A a Z - Crie Aplicações Web Rápidas, Seguras e Escaláveis com Python](https://www.linkedin.com/feed/update/urn:li:activity:7035781323155750912/)_

Aplicação web para consulta de médicos. Ela permitirá que usuários consultem os médicos, podendo filtrá-los por nome, especialidade, estado, cidade e bairro do médico. 

<img src="https://github.com/RochaGabriell/MedicSearch/blob/main/.github/home.png?raw=true" alt="Home Page"><br/>

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

## 📋 Pré-requisitos

```
Python 3.10.7
Django 4.1.5
```

## 🔧 Instalação

### 1 - Passo: Clone
Realize um clone do projeto em seu computador

```
https://github.com/RochaGabriell/MedicSearch.git
```

### 2 - Passo: Criação e Ativação do Ambiente Virtual
Crie um ambiente virtual na pasta raiz do projeto. No seu terminal use:

> Linux:

2.1 - Criação

```
python3 -m venv venv
```

2.2 - Ativação

```
source venv/bin/activate
```

> Para Windows ou Mac:

Consulte a documentação da linguagem [Python](https://docs.python.org/pt-br/3/library/venv.html)

### 3 - Passo: Instalação de depedências
É preciso instalar as depedências do projeto para o funcionamento correto. Com o seu ambiente virtual ativo use o comando no seu terminal:

```
pip install -r requirements.txt
```

### 4 - Configure os dados do arquivo [`.env`](https://django-environ.readthedocs.io/en/latest/)
Para a correta execução do projeto é necessário a configuração das variáveis de ambiente.

* Crie um arquivo `.env` na raiz do projeto

```
SECRET_KEY_DEVELOPMENT='Sua SECRET_KEY do ambiente de desenvolvimento'
SECRET_KEY_TESTING='Sua SECRET_KEY do ambiente de teste'
SECRET_KEY_PRODUCTION='Sua SECRET_KEY do ambiente de produção'

DATABASE_URL='URL que aponta para o banco de dados utilizado.'

SOCIAL_AUTH_FACEBOOK_KEY='id de autenticação para integração com a API do Facebook.'
SOCIAL_AUTH_FACEBOOK_SECRET='chaves de autenticação para integração com a API do Facebook.'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY='id de autenticação para integração com a API do Google.'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET='chaves de autenticação para integração com a API do Google.'

EMAIL_HOST_USER='usuário para autenticação em um servidor de e-mail.'
EMAIL_HOST_PASSWORD='senha para autenticação em um servidor de e-mail.'
DEFAULT_FROM_EMAIL='endereço de e-mail padrão utilizado.'
```

### 5 - Passo: Realize as migrações
Isso garante que o seu banco de dados esteja sincronizado com a estrutura do seu projeto.

```
python manage.py migrate
```

### 6 - Passo: Executar o projeto

```
python manage.py runserver
```
```
http://localhost:8000/
```
## 🔍 Funcionalidades

As principais funcionalidades da aplicação são:

* Login de usuário
* Logout de usuário
* Editar usuário
* Consultar médico
* Favoritar médico
* Comentar e avaliar médico
* Paginação na buscar dos médicos
* Autenticação de usuário por Facebook e Google
* Recuperação de senha via e-mail

## 🛠️ Construído com

* [Django Framework](https://www.djangoproject.com/) - O framework web usado na criação do projeto
* [PostgreSQL](https://www.postgresql.org/) - Banco de dados utilizado ao fazer deploy
* [Bootstrap](https://getbootstrap.com/) - Utilizado para estilização da página
* [HTML](https://developer.mozilla.org/pt-BR/docs/Web/HTML) - Estruturação da página
* [CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS) - Estilização da página
## 📄 Licença

#### Este projeto está sob a licença (MIT License) - veja o arquivo [LICENSE.md](https://github.com/RochaGabriell/MedicSearch/blob/main/LICENSE) para detalhes.
---