API Documentation
Índice
Registrar Transação
Cancelar Transação
Gerar Relatório
Registrar Transação
Endpoint
bash
Copy
POST /api/transactions
Descrição
Este endpoint é utilizado para registrar uma nova transação. A transação pode ser de débito ou crédito, associada a uma categoria e com um valor informado pelo usuário.

Parâmetros de Requisição
Parâmetro	Tipo	Descrição
user_id	string	Identificador único do usuário.
category_id	string	Identificador da categoria da transação.
transaction_type	string	Tipo da transação: credit ou debit.
amount	float	Valor da transação (ex: 100.50).
transaction_date	string	Data da transação (formato YYYY-MM-DD).
Resposta de Sucesso
Código: 201 Created

json
Copy
{
  "message": "Transação registrada com sucesso",
  "transaction_id": "123456",
  "status": "success"
}
Resposta de Erro
Código: 400 Bad Request

json
Copy
{
  "message": "Erro ao registrar transação. Verifique os dados informados.",
  "status": "error"
}
Cancelar Transação
Endpoint
bash
Copy
POST /api/transactions/cancel
Descrição
Este endpoint é utilizado para cancelar uma transação previamente registrada. O cancelamento é realizado utilizando o identificador da transação original.

Parâmetros de Requisição
Parâmetro	Tipo	Descrição
user_id	string	Identificador único do usuário.
transaction_ids	array	Lista de IDs de transações a serem canceladas.
cancel_reason	string	Motivo do cancelamento.
Resposta de Sucesso
Código: 200 OK

json
Copy
{
  "message": "Transações canceladas com sucesso",
  "status": "success",
  "cancelled_transactions": [
    {
      "transaction_id": "123456",
      "status": "cancelled"
    }
  ]
}
Resposta de Erro
Código: 400 Bad Request

json
Copy
{
  "message": "Erro ao cancelar transação. Verifique os dados informados.",
  "status": "error"
}
Gerar Relatório
Endpoint
bash
Copy
POST /api/reports/generate
Descrição
Este endpoint é utilizado para gerar um relatório financeiro com base em um intervalo de datas. O relatório pode ser gerado em diversos formatos, como PDF ou Excel.

Parâmetros de Requisição
Parâmetro	Tipo	Descrição
user_id	string	Identificador único do usuário.
start_date	string	Data de início do intervalo (formato YYYY-MM-DD).
end_date	string	Data de término do intervalo (formato YYYY-MM-DD).
format	string	Formato do relatório: pdf ou excel.
Resposta de Sucesso
Código: 202 Accepted

json
Copy
{
  "message": "Relatório em processo de geração.",
  "status": "processing",
  "report_link": null
}
Resposta quando o relatório estiver pronto
Código: 200 OK

json
Copy
{
  "message": "Relatório gerado com sucesso.",
  "status": "completed",
  "report_link": "https://s3.amazonaws.com/relatorios/relatorio_123456.pdf"
}
Resposta de Erro
Código: 400 Bad Request

json
Copy
{
  "message": "Erro ao gerar relatório. Verifique os dados informados.",
  "status": "error"
}
Fluxo de Trabalho
Registrar uma Transação
O usuário envia uma solicitação POST /api/transactions com os parâmetros necessários (ID do usuário, categoria, tipo de transação, valor e data).
O sistema valida os dados e registra a transação no banco de dados.
O sistema retorna uma mensagem de sucesso ou erro, conforme a validação.
Cancelar uma Transação
O usuário envia uma solicitação POST /api/transactions/cancel com a lista de IDs de transações a serem canceladas e o motivo.
O sistema valida a solicitação e realiza o cancelamento das transações no banco de dados, criando registros de cancelamento.
O sistema retorna uma mensagem de sucesso ou erro, conforme a validação.
Gerar um Relatório
O usuário envia uma solicitação POST /api/reports/generate com o intervalo de datas e formato do relatório.
O sistema processa a solicitação e começa a gerar o relatório. Inicialmente, retorna um status de "processamento".
Quando o relatório é gerado com sucesso, o sistema retorna o link para download do arquivo. Caso contrário, um erro é retornado.
