from exts import db
from datetime import datetime


class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.INTEGER, primary_key=True, nullable=False, index=True, autoincrement=True)
    username = db.Column(db.String(40), nullable=False, index=True, unique=True, comment='user name')
    password = db.Column(db.String(200), comment='user password')
    email = db.Column(db.String(128), unique=True, nullable=False, comment='user register email')
    avatar = db.Column(db.String(100), comment='user avatar')


class PostModel(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 注意这里是utcnow，默认是世界时间，如果不用moment，建议替换成本地时间now
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    post_name = db.Column(db.String(50), nullable=False, unique=True)

    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text(), nullable=False)

    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('UserModel', backref="posts")

    def __repr__(self):
        return '<Post %r>' % self.post_name

class CommentModel(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 注意这里是utcnow，默认是世界时间，如果不用moment，建议替换成本地时间now
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    content = db.Column(db.Text(), nullable=False)

    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    post = db.relationship('PostModel', backref="comments")

    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('UserModel', backref="comments")

    replied_id = db.Column(db.Integer, db.ForeignKey('comment.id'))
    replies = db.relationship('CommentModel', back_populates='replied', cascade='all')
    replied = db.relationship('CommentModel', back_populates='replies', remote_side=[id])

    def __repr__(self):
        return '<CommentModel %r>' % self.content

# class CaptchaModel(db.Model):
#     __tablename__ = 'captcha'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     email = db.Column(db.String(50), nullable=False, unique=True)
#     code = db.Column(db.String(4), nullable=False)
#
#     def __repr__(self):
#         return '<Captcha %r>' % self.code

    # college_id = db.Column(db.INTEGER, db.ForeignKey('t_college.id'))
    # college = db.relationship('College', back_populates='user')