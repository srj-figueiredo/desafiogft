# Fluxos de Processos

## Fluxo de Registrar uma Transação

1. O usuário se loga no sistema.
2. O sistema consulta o perfil do usuário.
3. O usuário escolhe a categoria, tipo e valor da transação.
4. O sistema registra a transação no banco e atualiza o saldo.

## Fluxo de Cancelar uma Transação

1. O supervisor se loga no sistema.
2. O supervisor filtra as transações a serem canceladas.
3. O sistema registra a transação como "cancelada" e atualiza o saldo.

## Fluxo de Gerar Relatório

1. O usuário solicita a geração do relatório.
2. O sistema consulta as transações no banco e gera o relatório.
3. O relatório é armazenado no S3 e o link é disponibilizado para o usuário.
