from flask import Flask, request, jsonify
import json

app = Flask(__name__)

with open('trainer.json', 'r') as f:
    comandos_data = json.load(f)

@app.route('/comandos', methods=['POST'])
def get_comando():
    user_input = request.json.get('command')
    if user_input in comandos_data["comandos"]:
        return jsonify({"response": comandos_data["comandos"][user_input]})
    else:
        return jsonify({"response": "Desculpe, comando não encontrado."})

if __name__ == '__main__':
    app.run(debug=True)
