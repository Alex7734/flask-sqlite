from flask import Flask, render_template, request, Blueprint, redirect, url_for
from .repository import get_user_by_username_password, insert_user
from .utils import log_user_in, log_user_out

users = Blueprint('users', __name__)

@users.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        account = get_user_by_username_password(username, password)
        if account:
            log_user_in(account)
            return redirect(url_for('index'))
        else:
            return 'Login failed. Check your username and password!'
    return render_template('users/login.html')

@users.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirmPassword']
        if password != confirm_password:
            return 'Passwords do not match!'
        insert_user(username, password)
        return redirect(url_for('users.login'))
    return render_template('users/register.html')

@users.route('/logout')
def logout():
    log_user_out()
    return redirect(url_for('index'))

