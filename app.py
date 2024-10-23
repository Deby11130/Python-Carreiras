from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

VAGAS = [{
    'id': 1,
    'titulo': 'Desenvolvedor Web',
    'empresa': 'Upwork',
    'local': 'Rio de Janeiro',
    'salario': 'R$ 4.000,00'
}, {
    'id': 2,
    'titulo': 'Desenvolvedor Web',
    'empresa': 'Totus',
    'local': 'São Paulo',
    'salario': 'R$ 5.000,00'
}, {
    'id': 3,
    'titulo': 'Analista de Dados',
    'empresa': 'vivo',
    'local': 'São Paulo',
    'salario': 'R$ 3.500,00'
}, {
    'id': 4,
    'titulo': 'Desenvolvedor de IA',
    'empresa': 'Avanade',
    'local': 'São Paulo',
    'salario': 'R$ 6.500,00'
}, {
    'id': 5,
    'titulo': 'Desenvolvedor Backend',
    'empresa': 'Impacta',
    'local': 'Rio de Janeiro',
    'salario': 'R$ 5.000,00'
}]


@app.route('/')
def hello():
  return render_template("home.html", vagas=VAGAS)

@app.route('/vagas')
def lista_vagas():
  return jsonify(VAGAS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
