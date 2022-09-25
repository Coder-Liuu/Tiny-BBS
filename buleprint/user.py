from flask import request, render_template, Blueprint, g

from models import PostModel

user_bp = Blueprint('user',__name__,url_prefix='/user')

@user_bp.route("/index/",methods=["GET", "POST"])
def index():
    posts = PostModel.query.filter_by(author_id=g.user.id).all()

    if request.method == "GET":
        return render_template("user/index.html", posts=posts)