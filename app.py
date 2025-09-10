from flask import Flask, render_template, request

app = Flask(__name__)

user_id = 1
usuarios = []
'''Endpoit Index'''
@app.route('/')
def index_():
    return render_template('index.html')

'''Endpoint add usuario'''
@app.route('/add', methods=['POST'])
def add_user_():
    global user_id
    user = {}
    if request.method == 'POST':
        user['id'] = user_id
        user['nome'] = request.form['name']
        user['email'] = request.form['email']
        usuarios.append(user.copy())
        user_id += 1
    return render_template('listar.html', usuarios=usuarios)

@app.route('/listar')
def listar_():
    return render_template('listar.html')

@app.route('/del')
def del_():
    return render_template('delete.html')

@app.route('/delete/<int:id>')
def delete_(id):
    global usuarios
    usuarios = [u for u in usuarios if u['id'] != id]
    return render_template('delete.html', usuarios=usuarios)

if __name__ == '__main__':
    app.run(debug=True)


