from flask import Flask
import sys

app = Flask(__name__)

@app.route('/')
def hello_world():
    # print(f"Rodando na porta {port}")
    return f'Hello, World! Porta: {port}'

@app.route('/qualquercoisa')
def qualquercoisa():
    return "Você acessou outra rota"

if __name__ == "__main__":
    port = 5000  # Valor padrão da porta
    if len(sys.argv) > 1:
        port = int(sys.argv[1])  # Pega a porta passada como argumento

    print(f"Rodando na porta {port}")
    app.run(host='0.0.0.0', port=port)
