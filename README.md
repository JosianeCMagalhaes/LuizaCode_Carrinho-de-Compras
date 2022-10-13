<!--<p align="center">
  <img alt="luizacode" title="banner-luizacode" src="https://user-images.githubusercontent.com/62856269/193715776-0a521946-b779-4b8e-a293-e772e835812a.png"/>-->
<!--Adicionar logo luizacode-opcional-->
<p align="center">
  <img alt="Fast-Mercado" title="banner-FastMercado" src="https://user-images.githubusercontent.com/62856269/195171619-4dedf943-90f0-4796-ad03-2b63c7c07bab.png"/>
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
* [2. O Projeto Carrinho de Compras](#2-o-projeto-carrinho-de-compras)
* [3. Implementações Futuras](#3-implementações-futuras)
* [4. Tecnologias utilizadas](#4-tecnologias-utilizadas)
* [5. Instalação da aplicação](#5-instalação-da-aplicação)
* [6. Bibliotecas instaladas](#6-bibliotecas-instaladas)
* [7. Documentação Interativa da API](#7-documentação-interativa-da-api)
* [8. Documentação do Heroku](#8-documentação-do-heroku)
* [9. Autoras](#9-autoras)
* [10. Contato](#10-contato)

***

## 1. Sobre
<!--Adicionar descrição do projeto-->
Uma API assíncrona com FastAPI e MongoDB, usando o pacote Motor para interagir com o MongoDB de forma assíncrona com deploy no Heroku. A aplicação foi desenvolvida visando atender os requisitos do projeto final do Luiza Code do Luizalabs, com FastAPI, MongoDB e Python.
  
<!--Implementado com testes com TestClient e CI/CD no GitHub Actions com deploy no Heroku.-->
<br />
  
## 2. O Projeto Carrinho de Compras
<!--Adicionar requisitos do porojeto-->
O Projeto Carrinho de Compras foi proposto como projeto final do curso, onde o objetivo é desenvolver um serviço de API Rest resolvendo a funcionalidade de Carrinho de Compra do cliente. Esse serviço deve atender os seguintes requisitos:

- Adicionar um produto ao carrinho do cliente;
- Remover um produto do carrinho do cliente;
- Consultar produtos do carrinho do cliente;

## 3. Implementações Futuras

- Performance (Volume de milhões de transações por dia);
- Testes automatizados e integração;
- Logs / Rastreabilidade;
- Tratamento de Exceção;
- Front-end da aplicação;
- Autenticação / Login da API;
- Alterar banco de dados;
- Implementar testes unitários.
 
## 4. Tecnologias utilizadas
<!--Adicionar tecnologias utilizadas-->
Para o desenvolvimento dessa aplicação foi utilizado o framework FastAPI para a criação da API, juntamente com o banco de dados MongoDB... 
- [FastAPI](https://fastapi.tiangolo.com/)
- [MongoDB](https://www.mongodb.com/)
- [Python](https://www.python.org/)

## 5. Instalação da aplicação

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

## 6. Bibliotecas instaladas
- [fastapi](https://fastapi.tiangolo.com/),
- [uvicorn](https://www.uvicorn.org/),
- [motor](https://motor.readthedocs.io/en/stable/).
  
## 7. Documentação Interativa da API

Documentação automática interativa da API (fornecida por [Swagger UI](https://github.com/swagger-api/swagger-ui)):
   ```
   http://127.0.0.1:8000/docs
   ```
  <!--print da documentação-->
  
Documentação automática alternativa (fornecida por [ReDoc](https://github.com/Redocly/redoc)):
   ```
   http://127.0.0.1:8000/redoc
   ```
  <!--print da documentação-->
  
## 8. Documentação do [Heroku](https://www.heroku.com/about):
```
```

## 9. Autoras

Projeto desenvolvido por: **Josiane Magalhães, Aline Marques, Nathália Rodrigues, Simone Lima, Vanessa Lima** 👋

## 10. Contato

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
