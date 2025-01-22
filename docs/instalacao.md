# Guia de Instalação

Aqui estão as etapas para rodar a aplicação localmente.

## Pré-requisitos

- **Python 3.x** instalado.
- **PostgreSQL** configurado.
- **Amazon S3** (opcional).

## Passos

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    cd nome-do-repositorio
    ```

2. Crie um ambiente virtual:
    ```bash
    python -m venv venv
    ```

3. Ative o ambiente virtual:
    - **Windows**:
      ```bash
      .\venv\Scripts\activate
      ```
    - **Linux/macOS**:
      ```bash
      source venv/bin/activate
      ```

4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

5. Configure o banco de dados PostgreSQL e o S3 (se necessário).
    
6. Execute a aplicação:
    ```bash
    python routes.py
    ```

A aplicação estará rodando em `http://localhost:5000`.
