from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_moment import Moment
from flask_avatars import Avatars

db = SQLAlchemy()
migrate = Migrate(db)
mail = Mail()
moment = Moment()
avator = Avatars()


