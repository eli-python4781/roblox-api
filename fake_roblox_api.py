from flask import Flask, jsonify

app = Flask(__name__)

# Fake user data
users = {
    1234: {
        "id": 1234,
        "username": "PlsDonateKing",
        "followers": 2750,
        "donated": 5000
    },
    5678: {
        "id": 5678,
        "username": "AFKChampion",
        "followers": 10000,
        "donated": 12000
    }
}

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
