# Integração ViaCEP com Python e PostgreSQL

## 📌 Sobre o Projeto

Este projeto é um mini exercício de integração entre uma API pública e um banco de dados relacional.

A aplicação realiza:

* Consulta de um CEP utilizando a API pública ViaCEP
* Tratamento de resposta HTTP
* Conversão do JSON retornado
* Persistência dos dados em banco PostgreSQL
* Controle de duplicidade utilizando `ON CONFLICT`

O objetivo é demonstrar conhecimentos básicos em:

* Consumo de API REST
* Manipulação de JSON
* Conexão com banco de dados PostgreSQL
* Estruturação de código em Python
* Versionamento com Git

---

## 🚀 Tecnologias Utilizadas

* Python 3.x
* requests
* psycopg2
* PostgreSQL

---

## ⚙️ Pré-requisitos

* Python instalado
* PostgreSQL instalado e rodando
* Banco de dados criado

Exemplo de criação do banco:

```sql
CREATE DATABASE enderecos;
```

Criação da tabela:

```sql
CREATE TABLE enderecos (
    cep VARCHAR(9) PRIMARY KEY,
    logradouro VARCHAR(255),
    complemento VARCHAR(255),
    bairro VARCHAR(255),
    localidade VARCHAR(255),
    uf VARCHAR(2)
);
```

---

## 📦 Instalação das Dependências

No terminal, execute:

```bash
pip install requests psycopg2
```

---

## 🏃 Como Executar

No diretório do projeto:

```bash
py consulta_cep.py
```

O sistema irá:

1. Consultar o CEP na API ViaCEP
2. Exibir os dados retornados
3. Inserir os dados no banco PostgreSQL (caso ainda não existam)

---

## 🔐 Configuração do Banco

No arquivo `consulta_cep.py`, configure o dicionário `DB_CONFIG` com os dados corretos de conexão:

```python
DB_CONFIG = {
    "host": "localhost",
    "database": "enderecos",
    "user": "seu_usuario",
    "password": "sua_senha",
    "port": 5432
}
```

---

## 🧠 Estrutura do Código

* `consultar_cep()` → Responsável por consumir a API
* `salvar_no_banco()` → Responsável por persistir os dados
* `main()` → Orquestra a execução do fluxo

---

## 📈 Possíveis Melhorias Futuras

* Uso de variáveis de ambiente (.env)
* Implementação de logs estruturados
* Containerização com Docker
* Transformar o script em uma API REST
* Implementar testes automatizados

---

## 📄 Licença

Projeto desenvolvido para fins educacionais.
