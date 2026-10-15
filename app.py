from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"mensagem": "Bem vindo a API Fast Order!"})

@app.route('/api/status')
def status():
    return jsonify({"Status": "Operacional", "Servico": "FastOrder-Web"})

@app.route('/api/soma')
def soma():
    try:
        a = request.args.get('a')
        b = request.args.get('b')
        resultado = float(a) + float(b)
    except:
        resultado = "Erro na operação"  


    return jsonify({'resultado': str(resultado)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)