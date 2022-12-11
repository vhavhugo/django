# django
Curso de Django Treinaweb

# Ambiente Virtual
pip install virtualenv
source venv/bin/activate

# Django
pip install Django==2.1.3

# mysql
pip install mysqlclient

# criar novo projeto django
django-admin startproject tw_clientes

Projetos vs Apps
No Django, um projeto é composto por uma ou várias apps. Cada app possui sua arquitetura e arquivos de models, views e templates. Sendo assim, as apps podem representar aplicações isoladas, porém em um mesmo projeto.

Imagine que estamos criando uma aplicação para um blog. Normalmente, um blog possui uma aplicação de administração (para cadastro dos posts) e uma página web (para leitura dos posts). Estas duas aplicações podem estar em um mesmo projeto, porém de forma isoladas.

Na imagem abaixo podemos ver a arquitetura básica de várias apps em um mesmo projeto:

# Criar uma aplicação
keila@DESKTOP-GKBC5FE MINGW64 /c/projetos/django/fundamentos/tw_clientes
$ python manage.py startapp clientes

# Executando o projeto
keila@DESKTOP-GKBC5FE MINGW64 /c/projetos/django/fundamentos/tw_clientes (introducao)
$ python manage.py runserver


O padrão MTV – Model-Template-View
O Django segue o padrão arquitetural chamado MTV, que possuem três camadas (Model, Template e View). Esta arquitetura é bem similar ao MVC, utilizado na maioria dos frameworks web do mercado. Basicamente, suas responsabilidades são:

O Model segue ao pé da letra a função que possui no padrão MVC, sendo responsável pela gestão de dados e lógica de negócio da aplicação. Possuindo um mapeador objeto-relacional (ORM), que permite definir os modelos sem utilizar códigos SQL (algo que também é possível, se você quiser).
O Template é responsável pela criação das páginas HTML que exibem os dados para os usuários. É essa camada que faz a interação com o usuário.
A View é responsável pelo “trâmite” de informações entre o model e o template. É essa camada que vai determinar quais dados serão retornados para o template. Em suma, é o “cérebro” da aplicação.
Há também uma outra “camada” chamada de URLs. Basicamente, esta “camada” é responsável por direcionar para a view correta a depender da rota utilizada pelo usuário.
Um exemplo do funcionamento de uma aplicação Django pode ser vista abaixo:

O usuário, através do Browser, acessa uma rota para obter determinado recurso;
A URL invoca o método da view, que usa o model para obter os dados do banco de dados por meio do seu ORM;
O model retorna os dados para a view, que usa o template (ou não) para retornar as informações para o usuário.


Estrutura básica de um projeto
Um projeto no Django é constituído por uma ou mais aplicações. Cada aplicação visa resolver determinado problema, mas todas elas estão situadas em um mesmo projeto.

As aplicações possuem uma estrutura de pastas e arquivos pré-definida, como podemos ver na figura abaixo:


Os arquivos presentes no diretório “clientes” representam uma aplicação. Suas funções são:

Migrations: Este diretório é responsável por armazenar os arquivos de migração do projeto. São eles os responsáveis por criar a estrutura do banco de dados que utilizamos em nossas aplicações;
Admin.py: Arquivo para gerência do módulo administrativo do Django. Não o veremos neste curso, mas é por meio deste arquivo que ativamos o módulo de administração do Django e determinamos quais entidades este pode gerenciar;
Apps.py: Arquivo que contém as configurações da aplicação em questão;
Models.py: É neste arquivo que definimos os models (Entidades) da nossa aplicação. É a partir dele que criamos as tabelas e os arquivos de migração (armazenados no diretório migrations) do projeto;
Tests.py: Arquivo para desenvolvimento do módulo de testes do Django. Não entraremos em detalhes deste módulo neste curso;
Views.py: Arquivo em que desenvolvemos os métodos de view do nosso projeto. É basicamente aqui que o “cérebro da aplicação” é desenvolvido.

# Configurações
fundamentos\tw_clientes\tw_clientes\settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tw_django_fundamentos',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Iniciar migrações
python manage.py migrate

Conectando a outros bancos de dados
O Django possui suporte há vários tipos de bancos de dados. A conexão com todos eles podem ser vistos na própria documentação do Django: https://docs.djangoproject.com/en/2.1/ref/databases/#connecting-to-the-database

# Criando model

class Cliente(models.Model):
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções"),
    )
    nome = models.CharField(max_length=100, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    profissao = models.CharField(max_length=50, null=False, blank=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)

    def __str__(self):
        return self.nome

    # Configuração do models no settings.py
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'clientes'
]

keila@DESKTOP-GKBC5FE MINGW64 /c/projetos/django/fundamentos/tw_clientes (upload)
$ python manage.py makemigrations

Entendendo o parâmetro request
Quando uma requisição é enviada através do Django, a view recebe um objeto request. Este objeto é de grande importância pois é ele quem possui todos os metadados da requisição.

Estes metadados são dos mais variados, como:

HttpRequest.scheme: Representa o tipo de requisição (http ou https);
HttpRequest.path: Retorna o caminho completo da rota que foi executada anteriormente;
HttpRequest.method: Retorna o método utilizado na requisição (GET, POST, PUT, PATCH, DELETE);
HttpRequest.cookies: Um dicionário que contém todos os cookies da requisição.
Há diversos outros metadados que podem ser obtidos com o objeto request no Django. Todos eles podem ser vistos por meio da sua documentação oficial no seguinte link: https://docs.djangoproject.com/en/2.1/ref/request-response/#httprequest-objects

Entendendo o parâmetro response
Assim como toda view recebe um objeto do tipo request como parâmetro, ela é obrigada a retornar um objeto response. Diferente do request que é criado automaticamente pelo Django, o response é de responsabilidade do programador.

Basicamente sua função é retornar alguma informação para o usuário, seja uma lista de usuários cadastrados ou uma mensagem de erro. Qualquer informação que deva ser passada da view para o template utiliza o response.

Todos os recursos do objeto response podem ser vistos através da documentação do Django no seguinte link: https://docs.djangoproject.com/en/2.1/ref/request-response/#httpresponse-objects