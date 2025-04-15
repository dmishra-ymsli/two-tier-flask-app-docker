from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# In-memory "database" for demo
users = {
    1: {"id": 1, "name": "Alice", "email": "alice@example.com"},
    2: {"id": 2, "name": "Bob", "email": "bob@example.com"},
}

@app.route('/')
def home():
    return "Flask API is running!"

# GET a user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        abort(404, description="User not found")
    return jsonify(user)

# PUT (update) a user by ID
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        abort(404, description="User not found")

    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        abort(400, description="Missing name or email in request")

    users[user_id]['name'] = name
    users[user_id]['email'] = email
    
    print("test")
    return jsonify(users[user_id])

if __name__ == '__main__':
    app.run(debug=True)
