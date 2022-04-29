from flask import Flask, render_template

app = Flask(__name__)

# criar a 1ª pagina do site
# route -> caminho depois do nome do seu domínio, link que vai abrir a página
# função -> o que você quer exibir naquela página

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/contatos')
def contatos():
    return render_template('contatos.html')

@app.route('/usuarios/<nome_usuario>')
def usuarios(nome_usuario):
    return render_template('usuarios.html', nome_usuario=nome_usuario)

# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)