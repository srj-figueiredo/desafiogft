from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Transacao(db.Model):
    __tablename__ = 'transacoes'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)  # 'débito' ou 'crédito'
    valor = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default='registrada')  # 'registrada' ou 'cancelada'
    saldo = db.Column(db.Float, nullable=True)
    data_criacao = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    def __init__(self, usuario_id, categoria, tipo, valor, saldo=None):
        self.usuario_id = usuario_id
        self.categoria = categoria
        self.tipo = tipo
        self.valor = valor
        self.saldo = saldo

    def __repr__(self):
        return f'<Transacao {self.id} - {self.categoria} - {self.tipo} - {self.valor}>'
