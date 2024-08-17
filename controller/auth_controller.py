from flask import Blueprint, request

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/')
@auth.route('/login',methods=['POST'])
def login():
    return "login"

@auth.route('/logout',methods=['POST'])
def logout():
    return "logout"