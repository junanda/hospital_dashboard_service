from flask import Blueprint, Response, request
from ..entity.user import RequestLogin
from ..service.login_service import LoginService
import json

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/login', methods=['POST'])
def login():
    data = RequestLogin(**request.get_json())
    result, data, err = LoginService().login(data)
    if result:
        return Response(status=200, mimetype='application/json', response=json.dumps({'status':'success', 'message': 'login success', 'token': data}))
    return Response(status=401, mimetype='application/json', response=json.dumps({'status':'failed', 'message': 'Username or Password incorrect'}))

@auth.route('/logout',methods=['POST'])
def logout():
    return "logout"