# 📘 API Intuitive

Este projeto implementa uma API REST em Python utilizando Flask, conectando-se ao banco de dados MySQL, para consultar e retornar dados das operadoras de planos de saúde cadastradas na ANS.

---

## 🚀 Como Executar

### 1. 📁 Estrutura do Projeto

```
intuitive/
├── backend/
│   ├── app/
│   │   ├── api.py
│   │   ├── config.py
│   │   └── db.py
│   ├── docs/
│   │   └── intuitiveCare.postman_collection.json
│   ├── utils/
│   │   └── preprocessamento.py
│   ├── requirements.txt
│   └── .env
├── db/
│    ├── consulta_ano.sql
│    ├── consulta_trimestre.sql
│    ├── consultas.sql
│    ├── import_postgres.sql
│    └── schema.sql
```

---

### 2. ⚙️ Configuração Inicial

**Passo 1:** Crie um ambiente virtual Python

```bash
python -m venv .venv
```

Ative o ambiente virtual:

```bash
# Windows
.venv\Scripts\activate

# Linux ou Mac
source .venv/bin/activate
```

**Passo 2:** Instale as dependências necessárias

```bash
pip install -r backend/requirements.txt
```

**Passo 3:** Configure as variáveis de ambiente (`.env`):

1. Renomeie o arquivo `example.env` para `.env`
2. Altere as configurações do `.env`

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=sua_senha
DB_DATABASE=db_intuitive
```

---

### 3. 🛠️ Executar a API

```bash
cd backend/app
python api.py
```

A API estará disponível em `http://localhost:5000`

---

## 🔗 Rotas Disponíveis

### 🔹 **Busca textual de Operadoras**

**GET** `/api/busca_operadoras`

**Parâmetros opcionais:**
- `q` = termo de busca (nome, razão social ou CNPJ)
- `uf` = estado (ex: SP)
- `cidade` = nome da cidade (ex: Campinas)

**Exemplos:**
```http
GET /api/busca_operadoras?q=amil
GET /api/busca_operadoras?q=amil&uf=SP
GET /api/busca_operadoras?q=12345678000100&cidade=São Paulo&uf=SP
```

---

### 🔹 **Top 10 Operadoras (Despesas)**

**GET** `/api/top_operadoras?periodo={ano|trimestre}&ano={ano}&trimestre={trimestre}&uf={uf}`

**Parâmetros obrigatórios:**
- `periodo` = "ano" ou "trimestre"
- `ano` = ano da análise (ex: 2024)

**Parâmetros opcionais:**
- `trimestre` = trimestre (ex: 4T)
- `uf` = estado (ex: SP)

**Exemplos:**
```http
GET /api/top_operadoras?periodo=ano&ano=2024
GET /api/top_operadoras?periodo=trimestre&ano=2024&trimestre=4T
GET /api/top_operadoras?periodo=ano&ano=2024&uf=SP
```

---

## 📌 Exemplos de Retorno

### ✅ **Busca Textual**

```json
[
  {
    "registro_ans": "123456",
    "razao_social": "AMIL ASSISTÊNCIA MÉDICA INTERNACIONAL S.A.",
    "nome_fantasia": "Amil",
    "cnpj": "00.000.000/0001-00",
    "uf": "SP",
    "cidade": "São Paulo"
  }
]
```

### ✅ **Top 10 Operadoras**

```json
[
  {
    "registro_ans": "123456",
    "razao_social": "AMIL ASSISTÊNCIA MÉDICA INTERNACIONAL S.A.",
    "nome_fantasia": "Amil",
    "cnpj": "00.000.000/0001-00",
    "uf": "SP",
    "total_despesa": 15000000.00
  }
]
```

---

## 📦 Coleção Postman

A coleção Postman foi atualizada e contempla os parâmetros `uf` e `cidade` nos endpoints de busca e de top operadoras:

📄 `backend/docs/intuitiveCare.postman_collection.json`

---

## 🛠️ Tecnologias utilizadas

- **Python**
- **Flask**
- **MySQL**
- **Postman**
- **dotenv**
- **CORS**
- **JSON + Decimal encoding**