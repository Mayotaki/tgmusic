from flask import request, jsonify
from .models import User, Post

@app.route('/create_post', methods=['POST'])
def create_post():
    data = request.json
    new_post = Post(user_id=data['user_id'], content=data['content'])
    db.session.add(new_post)
    db.session.commit()
    return jsonify({"message": "Post created!"}), 201
