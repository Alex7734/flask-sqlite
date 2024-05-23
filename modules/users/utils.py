from flask import session, redirect, url_for

def log_user_in(account):
    session['loggedin'] = True
    session['id'] = account[0]
    session['username'] = account[1]

def log_user_out():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    session['logged_out'] = True
