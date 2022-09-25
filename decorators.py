from functools import wraps

from flask import session, g, redirect, url_for
from models import UserModel


# request 之前
def before_request():
    user_id = session.get("user_id")
    if user_id:
        user = UserModel.query.filter_by(id=user_id).first()
        g.user = user


# 渲染html页面前
def context_processor():
    context = {}
    if hasattr(g, "user"):
        context["user"] = g.user
        return context
    else:
        return context

# 登录限制器
def login_require(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if not hasattr(g, "user"):
            return redirect(url_for('auth.login'))
        return func(*args, **kwargs)

    return inner
