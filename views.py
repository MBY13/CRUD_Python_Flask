from flask import render_template, request, redirect, url_for
from models import User

def index():
    users = User.get_all()
    return render_template('index.html', users=users)

def create():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        user = User(name, email)
        user.save()
        return redirect(url_for('index'))
    return render_template('create.html')

def edit(user_id):
    user = User.get_by_id(user_id)
    if request.method == 'POST':
        user.name = request.form['name']
        user.email = request.form['email']
        user.update()
        return redirect(url_for('index'))
    return render_template('edit.html', user=user)

def delete(user_id):
    user = User.get_by_id(user_id)
    user.delete()
    return redirect(url_for('index'))
