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

