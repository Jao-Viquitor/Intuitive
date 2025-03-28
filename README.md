# 🩺 Intuitive Care — Análise de Operadoras de Saúde (ANS)

O projeto **Intuitive** é uma plataforma que integra uma API Flask com um frontend Vue.js para **consultar, visualizar e analisar dados de operadoras de planos de saúde registradas na ANS** (Agência Nacional de Saúde Suplementar).

Ela permite consultar as maiores operadoras em volume de despesas assistenciais, fazer buscas textuais por CNPJ ou nome e visualizar os dados de forma prática e organizada.

---

## 📂 Estrutura do Projeto

```
intuitive/
├── backend/
│   ├── app/
│   ├── utils/
│   │   └── preprocessamento.py
│   ├── docs/
│   └── requirements.txt
├── frontend/
│   └── ...
├── dados/
│   ├── demonstracoes_contabeis/   ← CSVs dos trimestres
│   └── operadoras_ativas/         ← Cadastro das operadoras
├── db/
│   ├── schema.sql
│   ├── import.sql
│   └── consultas.sql
```

---

## 📥 Preparação dos Dados (Obrigatório)

Antes de executar qualquer parte do sistema, é **necessário baixar e organizar os arquivos públicos da ANS**:

### 1. 📊 Demonstrativos Contábeis (últimos 2 anos)

Baixe os 8 arquivos `.csv` dos trimestres no seguinte link:

🔗 [https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/](https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/)

📂 Coloque-os em:

```
dados/demonstracoes_contabeis/
```

---

### 2. 🏢 Cadastro de Operadoras Ativas

Baixe o arquivo `Relatorio_cadop.csv`:

🔗 [https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/](https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/)

📂 Coloque-o em:

```
dados/operadoras_ativas/
```

---

### 3. 🧹 Processamento dos Dados

Após baixar os arquivos e colocá-los nas pastas corretas, execute o script que consolida os dados:

```bash
python backend/utils/preprocessamento.py
```

> Isso criará arquivos prontos para importação no MySQL (`demonstracoes_contabeis_completo.csv` e dados limpos das operadoras).

---

## 🚀 Executando a Aplicação

### 1. Backend

**Passo 1:** Crie e ative o ambiente virtual:

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Passo 2:** Instale as dependências:

```bash
pip install -r backend/requirements.txt
```

**Passo 3:** Configure o `.env` (conforme `example.env`)

**Passo 4:** Execute o script de schema e import no MySQL

```sql
SOURCE db/schema.sql;
SOURCE db/import.sql;
```

---

### 2. Frontend + Backend (rodando juntos)

Na pasta `frontend`, instale as dependências:

```bash
cd frontend
npm install
```

Agora rode tudo com um único comando:

```bash
npm run dev
```

Esse comando iniciará:

- ✅ A **API Flask** na porta `5000`
- ✅ O **Frontend Vue** na porta `5173`

---

## 📌 Funcionalidades

- 🔎 Busca textual por operadora
- 📈 Visualização das **10 operadoras com maiores despesas**
- 📊 Filtros por ano (2023 e 2024) e trimestre (1T, 2T, 3T, 4T)
- ⚡ Execução simultânea com `npm run dev`

---

## 📦 Tecnologias

- Python + Flask
- Vue 3 + Vite
- Tailwind CSS
- MySQL 8+
- Postman (coleção incluída)
- concurrently (para rodar frontend + backend juntos)