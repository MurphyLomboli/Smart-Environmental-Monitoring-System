from app import app, db
from app.models import User, Post
from flask import jsonify, request


@app.route("/")
def index():
    return "Hello World"


@app.route('/api/users')
def all_users():
    users = User.query.all()

    users_data = [user.to_dict() for user in users]

    return jsonify(users_data)

@app.route('api/users/<int:id>')
def user(id):

    user = User.query.get(id)

    return jsonify(user.to_dict())

@app.route('/api/users', methods=['POST'])
def create_user():

    data = request.get_json

    #Data storage
    user == User()

    user.from_dict(data)

    db.session.add(user)
    db.session.coomit()

    response = jsonify(user.to_dict())
    response.status_code = 201

    return response
