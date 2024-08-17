from flask import Blueprint, request

doctor = Blueprint('doctor', __name__, url_prefix='/doctors')

@doctor.route('/', methods=['GET'])
def index():
    return "welcome doctor"

@doctor.route('/', methods=['POST'])
def register():
    return "registrasi doctor"

@doctor.route('/<string:id>', methods=['GET'])
def get_by_id(id):
    return "detail doctor " + id

@doctor.route('/<string:id>', methods=['PUT'])
def update(id):
    return "update " + id

@doctor.route('/<string:id>', methods=['DELETE'])
def delete(id):
    return "delete " + id