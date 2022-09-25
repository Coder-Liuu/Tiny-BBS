import random

from flask import Blueprint, request, render_template, flash
from exts import db
from models import PostModel

index_bp = Blueprint('index', __name__, url_prefix='/')


@index_bp.route("/", methods=["GET"])
def index():
    # 查询全部
    all_posts = PostModel.query.all()
    count = len(all_posts)
    sample_num = min(count, 5)
    random_posts = random.sample(all_posts, sample_num)

    # 分页操作
    Pagination = PostModel.query.order_by(db.text("-create_time")).paginate(
        page=int(request.args.get("page", 1)),
        per_page=int(request.args.get("size", 10)),
        error_out=False,
        max_per_page=50
    )
    return render_template("index.html", Pagination=Pagination, random_posts=random_posts)


@index_bp.route("/search/", methods=["GET"])
def search():
    wq = request.args.get("wq")
    posts = PostModel.query.filter(
        (PostModel.description + PostModel.post_name).contains(wq),
    ).order_by(db.text("-create_time"))
    flash(f"{wq} 的搜索结果", category="success")
    return render_template("index.html", posts=posts)
