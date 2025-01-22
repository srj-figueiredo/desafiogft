# desafiogft
Projeto para avaliação de conhecimentos técnicos no processo seletivo da GFT

Esta aplicação é responsável pelo registro, cancelamento e geração de relatórios de transações. Ela foi desenvolvida utilizando Python, com o framework Flask para o back-end, SQLAlchemy para interação com o banco de dados PostgreSQL, e Boto3 para integração com o Amazon S3.

Funcionalidades
Registrar Transação: O usuário pode registrar transações (débito ou crédito).
Cancelar Transação: O usuário pode cancelar transações registradas.
Gerar Relatório: O sistema gera relatórios detalhados de transações dentro de um intervalo de datas especificado.
Requisitos
Para rodar a aplicação localmente, você precisará dos seguintes pré-requisitos:

Python 3.x (Recomendado: Python 3.7 ou superior)
PostgreSQL: Banco de dados para armazenar as transações
Amazon S3: Configuração de armazenamento para os relatórios gerados (opcional)
NATS : para cache da aplicação

Instruções para rodar a aplicação localmente
1. Clonando o Repositório
Clone este repositório para o seu ambiente local:

bash
Copy
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
