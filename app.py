from flask import Flask, redirect, render_template, flash, request

app = Flask(__name__)


users = []

user_id = 1

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/add', methods=['POST'])
def add_user():
    global user_id
    user = {}
    if request.method == 'POST':
        user['id'] = user_id
        user['nome'] = request.form['nome']
        user['email'] = request.form['email']
        users.append(user.copy())
        user_id += 1
    return render_template('index.html', users=users)

@app.route('/delete/<int:id>')
def remove_user(id):
    global users
    users = [u for u in users if u['id'] != id]
    return render_template('index.html', users=users)
    



if __name__ == "__main__":
    app.run(debug=True)


