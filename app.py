from flask import Flask, render_template, request
from db.init_db import UserDB


app = Flask(__name__)

user_db = UserDB()

'''Endpoit Index'''
@app.route('/')
def index_():
    return render_template('index.html')

'''Endpoint add usuario'''
@app.route('/add', methods=['POST'])
def add_user_():
    if request.method == 'POST':
        nome = request.form['name']
        email = request.form['email']
        user_db.add_user(nome, email)
        return render_template('index.html')

@app.route('/listar')
def listar_():
    users = user_db.list_users()
    return render_template('listar.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)


