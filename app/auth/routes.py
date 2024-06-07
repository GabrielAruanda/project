from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'  # Defina uma chave secreta para o Flask

# Configuração para renderizar templates a partir de um diretório específico
app.template_folder = 'templates'

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
