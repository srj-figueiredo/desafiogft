from flask import Flask, request, jsonify
from services import registrar_transacao, cancelar_transacao, gerar_relatorio
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/dbname'
db.init_app(app)

@app.route('/registrar', methods=['POST'])
def registrar():
    data = request.json
    usuario_id = data.get('usuario_id')
    categoria = data.get('categoria')
    tipo = data.get('tipo')
    valor = data.get('valor')
    
    transacao = registrar_transacao(usuario_id, categoria, tipo, valor)
    return jsonify({
        'status': 'sucesso',
        'transacao_id': transacao.id,
        'saldo': transacao.saldo
    })

@app.route('/cancelar', methods=['POST'])
def cancelar():
    data = request.json
    transacao_id = data.get('transacao_id')
    
    transacao = cancelar_transacao(transacao_id)
    if transacao:
        return jsonify({'status': 'sucesso', 'transacao_id': transacao.id, 'status': transacao.status})
    return jsonify({'status': 'erro', 'mensagem': 'Transação não encontrada'}), 404

@app.route('/relatorio', methods=['POST'])
def relatorio():
    data = request.json
    usuario_id = data.get('usuario_id')
    data_inicio = data.get('data_inicio')
    data_fim = data.get('data_fim')
    
    link_relatorio = gerar_relatorio(usuario_id, data_inicio, data_fim)
    return jsonify({'status': 'sucesso', 'link': link_relatorio})

if __name__ == '__main__':
    app.run(debug=True)
