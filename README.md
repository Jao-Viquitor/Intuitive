# 🩺 Intuitive Care — Análise de Operadoras de Saúde (ANS)

O **Intuitive Care** é uma plataforma fullstack para análise, consulta e visualização de dados públicos de operadoras de planos de saúde registradas na **ANS (Agência Nacional de Saúde Suplementar)**.

A aplicação é composta por:

- 🔹 **Backend**: API REST em **Flask** com conexão **PostgreSQL**
- 🔹 **Frontend**: SPA em **Vue.js 3 + Vite + Tailwind**
- 🔹 Pré-processamento de dados via **Pandas**
- 🔹 Integração com arquivos públicos da ANS

---

## 🌐 Acesso em Produção

- 🔸 Frontend: [https://intuitive-eta.vercel.app](https://intuitive-eta.vercel.app)
- 🔸 API Backend: [https://intuitive-backend.onrender.com](https://intuitive-backend.onrender.com)

---

## 📁 Estrutura do Projeto

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
├── frontend/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── router/
│   │   └── services/
│   ├── index.html
│   └── package.json
├── dados/
│   ├── demonstracoes_contabeis/
│   └── operadoras_ativas/
├── db/
│   ├── schema.sql
│   ├── import_postgres.sql
│   ├── consulta_ano.sql
│   └── consulta_trimestre.sql
```

---

## 📥 Preparação de Dados

### 1. 📊 Demonstrativos Contábeis

Baixe os arquivos `.csv` dos últimos 2 anos em:

🔗 https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/

Coloque os arquivos em:

```
dados/demonstracoes_contabeis/
```

---

### 2. 🏢 Operadoras Ativas

Baixe o arquivo `Relatorio_cadop.csv`:

🔗 https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/

E coloque em:

```
dados/operadoras_ativas/
```

---

### 3. 🧹 Pré-processamento

Execute o script para gerar os dados consolidados:

```bash
python backend/utils/preprocessamento.py
```

---

## 🚀 Execução Local

### Backend

1. Crie e ative o ambiente virtual:

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
```

2. Instale as dependências:

```bash
pip install -r backend/requirements.txt
```

3. Configure o arquivo `.env` com as credenciais do banco PostgreSQL:

```env
DB_HOST=localhost
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_DATABASE=db_intuitive
```

4. Execute os scripts SQL:

```sql
-- No PostgreSQL
\i db/schema.sql
\i db/import_postgres.sql
```

---

### Frontend + Backend

Na pasta do frontend:

```bash
cd frontend
npm install
npm run dev
```

Esse comando usa o `concurrently` para rodar o backend (Flask) e o frontend (Vite) juntos.

---

## 🔗 Funcionalidades

### 🔍 Busca de Operadoras

- Termo de busca: nome, razão social ou CNPJ
- Filtros opcionais: estado (UF), cidade
- Resultados exibidos em cards estilizados

### 📊 Top 10 Operadoras por Despesa

- Filtro por ano ou trimestre
- Filtro opcional por estado (UF)
- Apresentação em cards com destaque para os valores

---

## 📦 Tecnologias Utilizadas

| Camada      | Tecnologias                                 |
|-------------|---------------------------------------------|
| Backend     | Flask, PostgreSQL, psycopg2, dotenv, CORS   |
| Frontend    | Vue 3, Vite, Tailwind CSS, Axios, Vue Router|
| Processamento | Python, Pandas                           |
| Deploy      | Render (backend + banco), Vercel (frontend) |

---

## 🧪 Testes via Postman

Uma coleção pronta está disponível em:

```
backend/docs/intuitiveCare.postman_collection.json
```

Inclui exemplos com parâmetros `q`, `uf`, `cidade`, `ano`, `trimestre`.