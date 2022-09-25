import random

from faker import Faker
from werkzeug.security import generate_password_hash

from app import app
from exts import db
from models import UserModel, PostModel, CommentModel

fa = Faker(locale='zh-CN')

def generate_user():
    for i in range(10):
        hash_password = generate_password_hash("123455")
        user = UserModel(username=fa.user_name().strip().lower(), email=fa.email(), password=hash_password)
        db.session.add(user)
    db.session.commit()

def generate_post():
    for i in range(20):
        content = ''
        for text in fa.texts():
            content += text
        p = PostModel(post_name=fa.sentence(),  description=content, author_id=random.randint(1, 10), category=random.choice(["游戏区","唠嗑区","程序区"]))
        db.session.add(p)
        db.session.flush()
    db.session.commit()

def generate_comment():
    for i in range(50):
        comment = CommentModel(content=fa.sentence()+"\n", post_id=random.randint(15, 30), author_id=random.randint(1, 10))
        db.session.add(comment)
    db.session.commit()

with app.app_context():
    generate_comment()