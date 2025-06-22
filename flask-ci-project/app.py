from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Docker!'

@app.route('/test')
def test():
    num = request.args.get('num')
    text = request.args.get('text')

    if not num or not text:
        return 'Erro: parâmetros "num" e "text" são obrigatórios.', 400

    return f'Recebido número: {num} e texto: "{text}"', 200

if __name__ == '__main__':
    app.run(debug=True)
