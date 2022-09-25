from flask import Flask

import decorators
from buleprint.api import api_bp
from exts import mail, migrate, db, moment, avator
from buleprint import auth_bp, post_bp, index_bp, user_bp

app = Flask(__name__)
# 加载数据库配置
app.config.from_object("config")
# 加载扩展
db.init_app(app)
migrate.init_app(app, db)
moment.init_app(app)
avator.init_app(app)

# 注册蓝图
app.register_blueprint(auth_bp)
app.register_blueprint(post_bp)
app.register_blueprint(index_bp)
app.register_blueprint(user_bp)
app.register_blueprint(api_bp)

# 装饰器
app.before_request(decorators.before_request)
app.context_processor(decorators.context_processor)

if __name__ == "__main__":
    app.run(debug=True)
