import boto3
import pika
from datetime import datetime
from models import db, Transacao

# Função para registrar a transação
def registrar_transacao(usuario_id, categoria, tipo, valor):
    nova_transacao = Transacao(usuario_id=usuario_id, categoria=categoria, tipo=tipo, valor=valor)
    db.session.add(nova_transacao)
    db.session.commit()
    
    # Atualizar saldo (simplificação)
    saldo_atualizado = calcular_saldo(usuario_id)
    nova_transacao.saldo = saldo_atualizado
    db.session.commit()
    
    return nova_transacao

# Função para calcular o saldo
def calcular_saldo(usuario_id):
    transacoes = Transacao.query.filter_by(usuario_id=usuario_id).all()
    saldo = sum(t.valor if t.tipo == 'crédito' else -t.valor for t in transacoes)
    return saldo

# Função para cancelar transação
def cancelar_transacao(id_transacao):
    transacao = Transacao.query.get(id_transacao)
    if transacao:
        transacao.status = 'cancelada'
        db.session.commit()
        return transacao
    return None

# Função para gerar relatório
def gerar_relatorio(usuario_id, data_inicio, data_fim):
    # Consulta as transações entre o intervalo de datas
    transacoes = Transacao.query.filter(
        Transacao.usuario_id == usuario_id,
        Transacao.data_criacao.between(data_inicio, data_fim)
    ).all()
    
    # Gerar relatório (simplificado)
    relatorio = f'Relatório de Transações de {usuario_id} entre {data_inicio} e {data_fim}:\n'
    for t in transacoes:
        relatorio += f'{t.data_criacao} - {t.categoria} - {t.tipo} - {t.valor} - Status: {t.status}\n'
    
    # Enviar para S3
    s3 = boto3.client('s3')
    s3.put_object(Bucket='meu-bucket', Key=f'relatorio_{usuario_id}.txt', Body=relatorio)
    
    return f'https://meu-bucket.s3.amazonaws.com/relatorio_{usuario_id}.txt'

# Função para simular interação com NATS 
def enviar_para_nats(mensagem):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='relatorios')
    channel.basic_publish(exchange='', routing_key='relatorios', body=mensagem)
    connection.close()
