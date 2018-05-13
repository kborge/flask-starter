from flask import Blueprint, request, make_response, jsonify
from flask_cors import CORS, cross_origin

api = Blueprint('api', __name__)
CORS(api)


@api.route('/', methods=['GET'])
@cross_origin()
def index():
    data = {'data': 'hello coder!'}
    return make_response(jsonify(data), 200)


@api.route('/login', methods=['POST'])
@cross_origin()
def login():
    # username = request.form.get('username')
    # password = request.form.get('password')
    return 'Welcome Back'


@api.route('/logout', methods=['GET'])
@cross_origin()
def logout():
    return 'See you again!'
