# 🌐 Frontend Intuitive

Este é o frontend do sistema **Intuitive**, uma aplicação web construída em **Vue.js 3 + Vite + Tailwind CSS**, 
responsável por exibir e interagir com os dados de operadoras de planos de saúde fornecidos pela [API Intuitive](../backend/README.md).

---

## 🚀 Como Executar

### 1. 📁 Estrutura do Projeto

```
frontend/
├── src/
│   ├── assets/
│   │   └── tailwind.css
│   ├── components/
│   │   ├── BuscaOperadoras.vue
│   │   └── TopOperadoras.vue
│   ├── App.vue
│   └── main.js
├── index.html
├── package.json
├── postcss.config.cjs
└── tailwind.config.js
```

---

### 2. ⚙️ Instalação e Setup

**Passo 1:** Navegue até a pasta `frontend`

```bash
cd frontend
```

**Passo 2:** Instale as dependências do projeto

```bash
npm install
```

**Passo 3:** xecutar Frontend + Backend juntos

Este projeto está configurado com `concurrently`, permitindo rodar o **frontend Vue.js** e o **backend Flask** com um único comando:

```bash
npm run dev
```

Esse comando:

- Ativa o servidor Flask (API)
- Inicia a aplicação Vue com Vite (`http://localhost:5173`)
- Faz a conexão entre frontend e backend automaticamente

---

## 🧩 Funcionalidades

### 🔎 **Busca de Operadoras**

- Campo de busca com retorno dinâmico de operadoras registradas na ANS
- Cards estilizados com informações como razão social, nome fantasia, CNPJ e localização

### 📊 **Top 10 Operadoras por Despesa**

- Consultas por **ano** ou **trimestre**
- Exibe as operadoras com maior gasto médico-hospitalar
- Valores formatados e layout responsivo

---

## 💅 Estilo e UX

- **Tailwind CSS** para estilo limpo, moderno e responsivo
- Tipografia legível e organização em cards

---

## 📦 Comandos Disponíveis

| Comando         | Descrição                         |
|-----------------|-----------------------------------|
| `npm install`   | Instala as dependências           |
| `npm run dev`   | Inicia o servidor de desenvolvimento |
| `npm run build` | Gera os arquivos para produção    |

---

## 📡 Integração com Backend

O frontend se comunica com a API Flask através de requisições HTTP via `axios`.  
Certifique-se de que a API esteja rodando em `http://localhost:5000`.

---

## 🛠️ Tecnologias Utilizadas

- [Vue 3 + Vite](https://vitejs.dev/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Axios](https://axios-http.com/)
- [Node.js](https://nodejs.org/)