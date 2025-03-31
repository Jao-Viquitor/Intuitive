# 📘 API Intuitive

Este projeto implementa uma **API REST** em **Python + Flask**, conectando-se a um banco de dados **PostgreSQL** (compatível com MySQL), para consulta e análise de dados de operadoras de planos de saúde fornecidos pela **ANS** (Agência Nacional de Saúde Suplementar).

A API está publicada em:

🔗 **https://intuitive-backend.onrender.com**

---

## 1. 📁 Estrutura do Projeto

```
intuitive/
├── backend/
│   ├── app/
│   │   ├── api.py
│   │   ├── config.py
│   │   └── db.py
│   ├── utils/
│   │   └── preprocessamento.py
│   ├── docs/
│   │   └── intuitiveCare.postman_collection.json
│   ├── requirements.txt
│   └── .env
├── db/
│   ├── schema.sql
│   ├── import_postgres.sql
│   ├── consulta_ano.sql
│   ├── consulta_trimestre.sql
```

---

## 2. ⚙️ Configuração Inicial

### 2.1 Ambiente virtual

```bash
python -m venv .venv
```

Ative o ambiente:

```bash
# Windows
.venv\Scripts\activate

# Unix/Mac
source .venv/bin/activate
```

### 2.2 Instalação de dependências

```bash
pip install -r backend/requirements.txt
```

### 2.3 Configuração do `.env`

Renomeie `example.env` para `.env` e configure com os dados do banco PostgreSQL:

```env
DB_HOST=localhost
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_DATABASE=db_intuitive
```

---

## 3. ▶️ Execução da API

No diretório `backend/app`, execute:

```bash
python api.py
```

A aplicação estará disponível localmente em:

```
http://localhost:5000
```

Ou no ambiente de produção (Render):

```
https://intuitive-backend.onrender.com
```

---

## 4. 🔗 Endpoints da API

Todos os endpoints abaixo funcionam com a base:

```
https://intuitive-backend.onrender.com/api/
```

### 4.1 GET `/busca_operadoras`

Busca textual de operadoras.

**Parâmetros opcionais:**

- `q`: termo (nome, razão social, CNPJ)
- `uf`: estado (ex: `SP`)
- `cidade`: cidade (ex: `Campinas`)

**Exemplos:**

```
GET /api/busca_operadoras?q=amil
GET /api/busca_operadoras?q=amil&uf=SP
GET /api/busca_operadoras?q=12345678000100&cidade=São Paulo&uf=SP
```

---

### 4.2 GET `/top_operadoras`

Retorna as 10 operadoras com maiores despesas assistenciais.

**Parâmetros obrigatórios:**

- `periodo`: `ano` ou `trimestre`
- `ano`: ex: `2024`

**Parâmetros opcionais:**

- `trimestre`: ex: `4T`
- `uf`: ex: `SP`

**Exemplos:**

```
GET /api/top_operadoras?periodo=ano&ano=2024
GET /api/top_operadoras?periodo=trimestre&ano=2024&trimestre=4T
GET /api/top_operadoras?periodo=ano&ano=2024&uf=SP
```

---

## 5. ✅ Exemplos de Retorno

### 5.1 Busca de operadoras

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

### 5.2 Top 10 operadoras

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

## 6. 🧪 Testes com Postman

Utilize a coleção pronta:

📄 `backend/docs/intuitiveCare.postman_collection.json`

Ela já inclui todos os endpoints e parâmetros.

---

## 7. 🛠️ Tecnologias Utilizadas

- **Python + Flask**
- **PostgreSQL (Render)**
- **dotenv**
- **Pandas**
- **Flask-CORS**
- **psycopg2**
- **Postman**