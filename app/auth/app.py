from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista temporária de usuários (simulação)
users = {'john': '123', 'emma': '456'}

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return redirect(url_for('success'))
        else:
            return render_template('login.html', error='Invalid username or password.')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username not in users:
            users[username] = password
            return redirect(url_for('login'))
        else:
            return render_template('signup.html', error='Username already exists.')
    return render_template('signup.html')

@app.route('/success')
def success():
    return 'Logged in successfully!'

if __name__ == '__main__':
    app.run(debug=True)
