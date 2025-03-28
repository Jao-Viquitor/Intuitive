# 🌐 Frontend Intuitive

Este é o frontend do sistema **Intuitive**, uma aplicação web construída com **Vue.js 3 + Vite + Tailwind CSS**, responsável por consultar e exibir dados públicos de operadoras de planos de saúde cadastradas na **ANS**, consumindo os dados expostos pela [API Intuitive](../backend/README.md).

---

## 🚀 Como Executar

### 1. 📁 Estrutura do Projeto

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

### 2. ⚙️ Instalação e Execução

#### **Passo 1:** Acesse o diretório do frontend

```bash
cd frontend
```

#### **Passo 2:** Instale as dependências

```bash
npm install
```

#### **Passo 3:** Execute Frontend + Backend juntos

```bash
npm run dev
```

Esse comando utiliza `concurrently` para:
- Iniciar o backend Flask (`localhost:5000`)
- Iniciar o frontend Vue (`localhost:5173`)

---

## 🧩 Funcionalidades

### 🔎 **Busca de Operadoras**

- Campo de busca textual com autocomplete
- Filtro opcional por estado (UF)
- Cards reutilizáveis com razão social, nome fantasia, CNPJ e localização

### 📊 **Top 10 Operadoras por Despesa**

- Filtros por **ano**, **trimestre** e **UF**
- Resultados em ordem decrescente de despesas
- Apresentação em cards com destaque para valores

---

## 💅 Design e Experiência

- Componentização com **Vue 3 (SFC)**
- Estilo moderno e responsivo com **Tailwind CSS**
- Componentes reutilizáveis para inputs, botões e cards
- Layout global com `Header` e `Footer` consistentes

---

## 🧪 Tecnologias Utilizadas

- [Vue.js 3 + Vite](https://vitejs.dev/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Axios](https://axios-http.com/)
- [Vue Router](https://router.vuejs.org/)
- [Node.js](https://nodejs.org/)
- [Vite SVG Loader](https://www.npmjs.com/package/vite-svg-loader)

---

## 📦 Comandos Disponíveis

| Comando         | Descrição                              |
|-----------------|------------------------------------------|
| `npm install`   | Instala todas as dependências             |
| `npm run dev`   | Inicia frontend e backend juntos          |
| `npm run build` | Gera a versão de produção do frontend     |

---

## 🔗 Backend

Certifique-se de que o backend esteja disponível e corretamente configurado.  
Para mais detalhes, consulte o [README do Backend](../backend/README.md).