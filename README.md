# desafiogft
Projeto para avaliação de conhecimentos técnicos no processo seletivo da GFT

Esta aplicação é responsável pelo registro, cancelamento e geração de relatórios de transações. 
Ela foi desenvolvida utilizando Python, com o framework Flask para o back-end, SQLAlchemy para interação com o banco de dados PostgreSQL, e Boto3 para integração com o Amazon S3.

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
git clone https://github.com/srj-figueiredo/desafiogft.git
cd nome-do-repositorio

2. Criando um Ambiente Virtual
Crie um ambiente virtual para isolar as dependências do projeto. Caso não tenha o virtualenv instalado, você pode instalar usando o comando:

bash
Copy
pip install virtualenv

Agora, crie o ambiente virtual:

bash
Copy
python -m venv venv
Ative o ambiente virtual:

No Windows:

bash
Copy
.\venv\Scripts\activate

No Linux/macOS:

bash
Copy
source venv/bin/activate


4. Configurando o Banco de Dados PostgreSQL
Certifique-se de ter o PostgreSQL instalado e configurado corretamente. Você pode usar o pgAdmin ou o psql para acessar o banco de dados.

Crie um banco de dados no PostgreSQL (por exemplo, transacoes_db).
Atualize o arquivo de configuração routes.py com a URL de conexão do banco de dados:
python
Copy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://usuario:senha@localhost:5432/transacoes_db'
Substitua usuario, senha, e localhost pelas configurações do seu ambiente.

5. Configurando o Amazon S3
Se você deseja utilizar o Amazon S3 para o armazenamento dos relatórios gerados:

Crie uma conta na AWS.
Configure um bucket S3 para armazenar os relatórios.
Configure as credenciais da AWS no arquivo ~/.aws/credentials ou exporte as variáveis de ambiente:
bash
Copy
export AWS_ACCESS_KEY_ID='sua-chave-de-acesso'
export AWS_SECRET_ACCESS_KEY='sua-chave-secreta'

6. Inicializando o Banco de Dados
Após configurar o banco de dados, execute o seguinte comando para criar as tabelas necessárias:

bash
Copy
python
>>> from app import db
>>> db.create_all()
Isso criará as tabelas no banco de dados com base nos modelos definidos no arquivo models.py.
>>>

7. Rodando a Aplicação
Agora que tudo está configurado, você pode iniciar a aplicação localmente utilizando o seguinte comando:

bash
Copy
python routes.py
O Flask rodará a aplicação em http://localhost:5000.


8. Testando a API
Você pode usar ferramentas como o Postman ou cURL para testar as rotas da API.

Registrar uma Transação:
bash
Copy
curl -X POST http://localhost:5000/registrar -H "Content-Type: application/json" -d '{"usuario_id": "123", "categoria": "compras", "tipo": "débito", "valor": 100.0}'

Cancelar uma Transação:
curl -X POST http://localhost:5000/cancelar -H "Content-Type: application/json" -d '{"transacao_id": 1}'

9. Parando a Aplicação
Para parar a aplicação, pressione Ctrl+C no terminal onde o Flask está rodando.

Estrutura do Repositório
perl
Copy
nome-do-repositorio/
├── .github/
│   └── workflows/
│       └── ci.yml                # Workflow de CI (Integração Contínua)
├── docs/                          # Diretório para toda a documentação
│   ├── images/                    # Pasta para armazenar imagens utilizadas na documentação
│   ├── index.md                   # Página inicial da documentação
│   ├── instalação.md              # Guia de instalação e configuração
│   ├── funcionalidades.md         # Detalhamento das funcionalidades
│   ├── fluxos.md                  # Descrição dos fluxos de processos
│   ├── casostestes.md             # Casos de teste unitários e integrados
│   ├── api.md                     # Documentação das APIs
│   └── contribuição.md            # Instruções para contribuição no projeto
├── src/                           # Código-fonte da aplicação
│   ├── app/
│   ├── models.py
│   ├── routes.py
│   └── services.py
├── README.md                      # Resumo do projeto, instruções rápidas de uso
├── requirements.txt               # Dependências do projeto
├── LICENSE                        # Licença do projeto
└── .gitignore                     # Arquivos a serem ignorados pelo Git

11. Testes e Validações
Os casos de teste para garantir o correto funcionamento da aplicação podem ser executados usando o pytest ou outro framework de testes que preferir. O código para testes não está incluso neste repositório, mas você pode escrever testes unitários e de integração conforme discutido anteriormente.

