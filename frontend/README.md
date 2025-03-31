# 🌐 Frontend Intuitive

Este é o frontend do sistema **Intuitive**, uma aplicação web construída com **Vue.js 3 + Vite + Tailwind CSS**, responsável por consultar e exibir dados públicos de operadoras de planos de saúde cadastradas na **ANS**, consumindo os dados expostos pela [API Intuitive](../backend/README.md).

🟢 **Acesse em produção**:  
🔗 https://intuitive-eta.vercel.app/

---

## 🚀 Como Executar Localmente

### 📁 Estrutura do Projeto

```
frontend/
├── public/
│   └── favicon.svg
├── src/
│   ├── assets/
│   │   ├── logo.svg
│   │   └── tailwind.css
│   ├── components/
│   │   ├── cards/OperadoraCard.vue
│   │   ├── inputs/InputText.vue
│   │   ├── inputs/InputSelectUF.vue
│   │   ├── layout/Header.vue
│   │   └── layout/Footer.vue
│   ├── pages/
│   │   ├── Home.vue
│   │   ├── TopOperadoras.vue
│   │   └── BuscaOperadoras.vue
│   ├── services/
│   │   └── api.js
│   ├── router/
│   │   └── index.js
│   ├── App.vue
│   └── main.js
├── index.html
├── package.json
├── postcss.config.cjs
└── tailwind.config.js
```

---

### ⚙️ Instalação e Execução

#### Passo 1: Acesse a pasta

```bash
cd frontend
```

#### Passo 2: Instale as dependências

```bash
npm install
```

#### Passo 3: Execute a aplicação (frontend + backend)

```bash
npm run dev
```

Este comando executa simultaneamente:

- ✅ Backend Flask (`http://localhost:5000`)
- ✅ Frontend Vue com Vite (`http://localhost:5173`)

---

## 🧩 Funcionalidades

### 🔍 Busca de Operadoras

- Busca por nome, razão social ou CNPJ
- Filtro opcional por estado (UF)
- Resultados exibidos em **cards reutilizáveis**

### 📊 Top 10 Operadoras por Despesa

- Filtros por **ano**, **trimestre** e **UF**
- Dados classificados por valor de despesa assistencial
- Apresentação visual com destaque para os valores

---

## 💅 Interface e Design

- Estilização com **Tailwind CSS**
- Layout com **Header** e **Footer** global
- Componentes reutilizáveis:
    - Inputs (`InputText.vue`, `InputSelectUF.vue`)
    - Botões (`ButtonPrimary`)
    - Cards (`OperadoraCard.vue`)
- Responsivo e acessível

---

## 🧪 Tecnologias Utilizadas

- [Vue 3 + Vite](https://vitejs.dev/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Axios](https://axios-http.com/)
- [Vue Router](https://router.vuejs.org/)
- [Vite SVG Loader](https://www.npmjs.com/package/vite-svg-loader)
- [Vercel (Deploy)](https://vercel.com)

---

## 📦 Comandos Disponíveis

| Comando         | Descrição                                   |
|-----------------|----------------------------------------------|
| `npm install`   | Instala as dependências do projeto           |
| `npm run dev`   | Executa o frontend e o backend juntos        |
| `npm run build` | Gera os arquivos otimizados para produção    |

---

## 🔗 Integração com o Backend

A aplicação consome a [API Intuitive](../backend/README.md), que deve estar disponível na URL:

```
https://intuitive-backend.onrender.com
```

A comunicação é feita com `axios`, através da instância centralizada no arquivo `src/services/api.js`.