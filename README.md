<p align="center">
  <img alt="luizacode" title="banner-luizacode" src="https://user-images.githubusercontent.com/62856269/193715776-0a521946-b779-4b8e-a293-e772e835812a.png"/>
<!--Adicionar logo luizacode-opcional-->
</p>

<h1 align="center">
  Projeto Final - Luiza < Code > 
</h1>
  
<h2 align="center">
  Carrinho de compras
</h2>

<h2 align="center">
  Mercado 🛒 - Grupo 3
</h2>
  
<h3 align="center">
  API REST com FastAPI Framework e Python.
</h3>
  
<!--Opcional
<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/Bonizario/proffy?color=6842C2">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/bonizario/proffy?color=774DD6">

  <a href="https://github.com/Bonizario/proffy/blob/master/LICENSE">
    <img alt="License" src="https://img.shields.io/github/license/bonizario/proffy?color=04D361">
  </a>

  <a href="https://github.com/Bonizario/proffy/stargazers">
    <img alt="Stargazers" src="https://img.shields.io/github/stars/bonizario/proffy?style=social">
  </a>
</p>
<br />-->

## Índice

* [1. Sobre](#1-sobre)
* [2. Requisitos obrigatórios do desafio](#2-requisitos-obrigatórios-do-desafio)
* [3. Tecnologias utilizadas](#3-tecnologias-utilizadas)
* [4. Instalação da aplicação](#4-instalação-da-aplicação)
* [5. Bibliotecas Python](#5-bibliotecas-python)
* [6. Autoras](#6-autoras)
* [7. Contato](#7-contato)

***

## 1. Sobre
<!--Adicionar descrição do projeto-->
Uma API assíncrona com FastAPI e MongoDB, usando o pacote Motor para interagir com o MongoDB de forma assíncrona com deploy no Heroku. A aplicação foi desenvolvida visando atender os requisitos do projeto final do Luiza Code, com FastAPI, MongoDB e Python.
  
<!--Implementado com testes com TestClient e CI/CD no GitHub Actions com deploy no Heroku.-->
<br />
  
## 2. Requisitos obrigatórios do desafio
<!--Adicionar requisitos obrigatórios do porojeto-->
  -  
  - 
  - 
  -

## 3. Tecnologias utilizadas
<!--Adicionar tecnologias utilizadas-->
Para o desenvolvimento dessa aplicação foi utilizado o framework FastAPI para a criação da API, juntamente com o banco de dados MongoDB... 
- [FastAPI](https://fastapi.tiangolo.com/)
- [MongoDB](https://www.mongodb.com/)
- [Python](https://www.python.org/)

## 4. Instalação da aplicação

Para instalação é necessário ter o Python e o FastAPI instalados na máquina.
<!--Adicionar os passos para instalação, referência: https://www.alura.com.br/artigos/como-criar-apis-python-usando-fastapi-->

* Create venv
    ```
    $ python -m venv venv
    ```
* Ativando o ambiente virtual
   
    Para ativar o ambiente virtual no Linux:
    ```
    $ source venv/bin/activate
    ```
    Para ativar o ambiente virtual no Windows:
    ```
    $ .\venv\Scripts\activate
    ```
  Após o comando inserido, deve aparecer o nome do ambiente virtual
* Install requirements
    ```
    pip install -r requirements.txt
    ```
* Connect mongodb
    ```

    $ create a .env file with your mongoDB connect string according to .env.example file 
    ```

    | name_env | value |
    |------------|------------|
    |DATABASE_URI|connection string Atlas|
     
* Run
    ```
    uvicorn main:app --reload
    ```
* Como testar
    ```
  Abra os arquivos de teste de casos e teste as rotas
  Dica: você pode instalar a extensão "Rest Client" no Visual Studio Code para executar testes diretamente nos arquivos *.http
    ```

## 5. Bibliotecas instaladas
- [fastapi](https://fastapi.tiangolo.com/),
- [uvicorn](https://www.uvicorn.org/),
- [motor](https://motor.readthedocs.io/en/stable/).
  
## 6. Documentação Interativa da API

Documentação automática interativa da API (fornecida por [Swagger UI](https://github.com/swagger-api/swagger-ui)):
   ```
   http://127.0.0.1:8000/docs
   ```
  <!--print da documentação-->
  
## 7. Documentação Alternativa da API
Documentação automática alternativa (fornecida por [ReDoc](https://github.com/Redocly/redoc)):
   ```
   http://127.0.0.1:8000/redoc
   ```
  <!--print da documentação-->
  
## 8. Documentação do [Heroku](https://www.heroku.com/about):
```
```


<!--## 5. API Endpoints-->
<!--Adicionar os end points solicitados no projeto-->
  
<!--exemplos
- **endpoint:** `/users/register/`
- **method:** `POST`
- **params:** 

- **200 Response:**

#### Criando um produto

- **endpoint:** `/products/`
- **method:** `POST`
- **params:** Em Basic passar o username e password
- **200 Response:**

- **201 Response**

#### Listando Produtos

- **endpoint:** `/products/`
- **method:** `GET`


- **201 Response:**-->



<p align="center">
  <img alt="" title="" src="" />
<!--Adicionar imagem da documentação da API-opcional-->
</p>

## 8. Autoras

Projeto desenvolvido por: **Josiane Magalhães, Aline Marques, Nathália Rodrigues, Simone Lima, Vanessa Lima** 👋

## 9. Contato

**Linkedin**: 
- [Josiane Magalhães](https://www.linkedin.com/in/josianemagalhaes/)
- [Aline Marques](https://www.linkedin.com/in/aline-marques-16790115a/) 
- [Nathália Rodrigues](https://www.linkedin.com/in/naaahrodrigues/)
- [Simone Lima](https://www.linkedin.com/in/simone-lorenzini-lima-financeiro/)
- [Vanessa Lima](https://www.linkedin.com/in/vanessacristinadelima/)


<!--links úteis
FastAPI https://fastapi.tiangolo.com/
Python https://www.python.org/
MongoDB https://www.mongodb.com/docs/
https://www.alura.com.br/artigos/como-criar-apis-python-usando-fastapi
https://www.magazineluiza.com.br/mercado/l/me/-->

<!--
● Montar um arquivo README.md detalhando o projeto com informações tais como:
  ○ Tecnologia utilizada.
  ○ Bibliotecas do Python que estão no projeto.
  ○ Membros da equipe.
  ○ Como montar o ambiente para executar a aplicação.
  ○ Detalhes do desenvolvimento do trabalho, informando do que foi solicitado o que foi feito (o que não foi feito) e os extras que foram feitos.
  ○ Informações extras sobre o trabalho.-->
