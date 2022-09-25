from flask import Blueprint, request, render_template, session, redirect, flash, url_for
from werkzeug.security import generate_password_hash

from buleprint.form import LoginForm, RegisterForm
from exts import db
from models import UserModel

auth_bp = Blueprint('auth',__name__,url_prefix='/auth')


@auth_bp.route("/login/",methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("auth/login.html")
    elif request.method == "POST":
        # 接收POST请求
        form = LoginForm(request.form)
        if form.validate():
            # 登录成功
            session["user_id"] = form.user_id
            flash("登录成功", category='success')
            return redirect(url_for('index.index'))
        else:
            # 登录失败
            for key, err in form.errors.items():
                if err != "":
                    flash(err, category='error')
            return render_template("auth/login.html")

@auth_bp.route("/register/",methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("auth/register.html")
    elif request.method == "POST":
        # 接收POST请求
        form = RegisterForm(request.form)
        if form.validate():
            # 存储数据
            hash_password = generate_password_hash(form.password.data)
            user_model = UserModel(username=form.username.data, email=form.email.data, password=hash_password)
            db.session.add(user_model)
            db.session.commit()
            flash("注册成功", category='success')
            return redirect(url_for("auth.login"))
        else:
            for key, err in form.errors.items():
                if err != "":
                    flash(err, category='error')
            # 报告哪里出现了问题
            return render_template("auth/register.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('auth.login'))