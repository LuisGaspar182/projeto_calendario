# Meu Projeto

Este repositório contém um projeto com:

- **Back-end:** Django
- **Front-end:** Vue.js

## Estrutura do Projeto

meu-projeto/ ├── backend/ # Código do back-end ├── frontend/ # Código do front-end

## Como Configurar o Projeto

### 1. Configurar o Back-end (Django)

- Instale as dependências no ambiente virtual:
  ```bash
  cd calendario
  python -m venv venv
  source venv/bin/activate  # Windows: venv\Scripts\activate
  pip install -r requirements.txt
  python manage.py migrate
  python manage.py runserver
  ```

### 2. Configurar o Front-end (Vue.js)

- Instale as dependências e execute o servidor de desenvolvimento:
  ```bash
  cd frontend
  npm install
  npm run serve
  ```
