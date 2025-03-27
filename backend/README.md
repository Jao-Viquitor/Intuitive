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
│    ├── import.sql
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

1. Renomeio o arquivo `example.env` para `.env`
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

**GET** `/api/busca_operadoras?q={termo}`

Exemplo de uso:
```http
GET http://localhost:5000/api/busca_operadoras?q=AMIL
```

### 🔹 **Top 10 Operadoras (Despesas)**

**GET** `/api/top_operadoras?periodo={ano|trimestre}&ano={ano}&trimestre={trimestre}`

Exemplos:

- **Por ano:**
```http
GET http://localhost:5000/api/top_operadoras?periodo=ano&ano=2024
```

- **Por trimestre:**
```http
GET http://localhost:5000/api/top_operadoras?periodo=trimestre&trimestre=4T&ano=2024
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
        "total_despesa": 15000000.00
    }
]
```

---

## 📦 Coleção Postman

Uma coleção no Postman está preparada com os exemplos acima para testar facilmente todas as rotas implementadas.

---

## 🛠️ Tecnologias utilizadas

- **Python**
- **Flask**
- **MySQL**
- **Postman**
