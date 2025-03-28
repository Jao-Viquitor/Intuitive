# 🩺 Intuitive Care — Análise de Operadoras de Saúde (ANS)

O **Intuitive Care** é uma plataforma completa de análise e visualização de dados públicos de operadoras de planos de saúde registrados na **ANS** (Agência Nacional de Saúde Suplementar). A aplicação é composta por:

- 🔹 **Backend (API REST)** em **Flask + MySQL**
- 🔹 **Frontend SPA** em **Vue 3 + Tailwind + Vite**
- 🔹 Processamento de dados a partir de arquivos públicos fornecidos pela ANS

---

## 📂 Estrutura do Projeto

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
│   ├── package.json
│   └── tailwind.config.js
├── dados/
│   ├── demonstracoes_contabeis/
│   └── operadoras_ativas/
├── db/
│   ├── schema.sql
│   ├── import.sql
│   ├── consulta_ano.sql
│   └── consulta_trimestre.sql
```

---

## 📥 Preparação de Dados (Obrigatório)

Antes de rodar o sistema, baixe os dados públicos da ANS:

### 1. 📊 Demonstrativos Contábeis

Baixe os arquivos `.csv` dos últimos 2 anos (1T a 4T) em:

🔗 [https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/](https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/)

Coloque em:

```
dados/demonstracoes_contabeis/
```

### 2. 🏢 Cadastro das Operadoras Ativas

Baixe o `Relatorio_cadop.csv` em:

🔗 [https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/](https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/)

Coloque em:

```
dados/operadoras_ativas/
```

### 3. 🧹 Executar Pré-processamento

Execute o script para preparar os dados para importação:

```bash
python backend/utils/preprocessamento.py
```

---

## 🚀 Executando o Projeto

### ✅ Backend

1. Ative o ambiente virtual:

```bash
python -m venv .venv
.venv\Scripts\activate
```

2. Instale as dependências:

```bash
pip install -r backend/requirements.txt
```

3. Configure o `.env` (copie de `example.env` e ajuste):

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=sua_senha
DB_DATABASE=db_intuitive
```

4. Execute os scripts SQL no seu MySQL:

```sql
SOURCE db/schema.sql;
SOURCE db/import.sql;
```

---

### ✅ Frontend + Backend (simultâneo)

1. Entre na pasta `frontend` e instale as dependências:

```bash
cd frontend
npm install
```

2. Rode tudo com:

```bash
npm run dev
```

Esse comando executa:
- O **servidor Flask** (`http://localhost:5000`)
- O **frontend Vue** (`http://localhost:5173`)

---

## 🧩 Funcionalidades

### 🔎 Busca por Operadora
- Busca por razão social, nome fantasia ou CNPJ
- Filtro adicional por estado (UF)
- Lista com cartões personalizados e responsivos

### 📊 Top 10 Operadoras por Despesa
- Consulta por ano ou trimestre
- Filtro por estado (UF)
- Valores formatados, layout limpo e responsivo

---

## 📦 Tecnologias Utilizadas

| Camada     | Tecnologias                                     |
|------------|-------------------------------------------------|
| Backend    | Python, Flask, MySQL, python-dotenv, CORS       |
| Frontend   | Vue 3, Vite, Tailwind CSS, Axios, Vue Router    |
| Dados      | CSVs da ANS, processamento com Pandas           |
| Utilitários| Postman, concurrently, dotenv, Vite plugins     |

---

## 📫 Testes via Postman

Uma coleção já pronta está disponível em:

```
backend/docs/intuitiveCare.postman_collection.json
```

Importe no Postman e teste todas as rotas da API rapidamente.