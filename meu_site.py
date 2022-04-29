from flask import Flask

app = Flask(__name__)

# criar a 1ª pagina do site
# route -> caminho depois do nome do seu domínio, link que vai abrir a página
# função -> o que você quer exibir naquela página

@app.route('/')
def home():
    return 'Meu 1º site usando Flask !!'

@app.route('/contatos')
def contatos():
    return '<p>Email:</p> <p>blablabal@gmail.com</p> <p>Telefone:</p> <p>(00) 1234-5678</p>'

# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)