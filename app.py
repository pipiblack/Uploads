from flask import Flask, render_template, request, redirect, url_for, flash
# from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])

def login():

    User_Name = request.form.get('User_Name')
    Password = request.form.get('Password')

    if User_Name == 'admin' and Password == 'admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('index'))
    
@app.route('/admin')

def admin():
    return render_template('admin.html')


if __name__ == '__main__':
    app.run(debug=True)

    
    


