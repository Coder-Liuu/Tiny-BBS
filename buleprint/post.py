import json

from flask import Blueprint, request, render_template, g, jsonify

from decorators import login_require
from exts import db
from models import PostModel, CommentModel

post_bp = Blueprint('post', __name__, url_prefix='/post')


@post_bp.route("/new_post", methods=["GET", "POST"])
@login_require
def new_post():
    if request.method == "GET":
        return render_template("post/new_post.html")
    elif request.method == "POST":
        data = json.loads(request.get_data())

        context = data["context"]
        post_name = data["title"]
        category = data["category"]

        post = PostModel(post_name=post_name, description=context,
                         category=category, author_id=g.user.id)
        db.session.add(post)
        db.session.commit()

        result = {
            "errno": 0,
        }
        return jsonify(result)


@post_bp.route("/detail/<id>", methods=["GET", "POST"])
def detail(id):
    if request.method == "GET":
        post = PostModel.query.filter_by(id=id).first()
        return render_template("post/detail_post.html", post=post)
    elif request.method == "POST":
        data = json.loads(request.get_data())

        content = data["content"]
        comment = CommentModel(content=content, post_id=id, author_id=g.user.id)
        if data["replied_id"] != "":
            comment.replied_id = data["replied_id"]
        db.session.add(comment)
        db.session.commit()
        result = {
            "errno": 0,
        }
        return jsonify(result)

@post_bp.route("/del_post", methods=["POST"])
@login_require
def del_post():
    if request.method == "POST":
        data = json.loads(request.get_data())
        post_id = data["post_id"]
        post = PostModel.query.filter_by(id=post_id).first()
        db.session.delete(post)
        db.session.commit()

        result = {
            "errno": 0,
        }
        return jsonify(result)