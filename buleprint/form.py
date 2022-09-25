import wtforms
from werkzeug.security import check_password_hash, generate_password_hash
from wtforms.validators import length, email, EqualTo
from models import UserModel


class LoginForm(wtforms.Form):
    email = wtforms.StringField(validators=[email()])
    password = wtforms.StringField(validators=[length(min=6,max=20)])

    def validate_password(self, field):
        password = field.data
        email = self.email.data
        user_model = UserModel.query.filter_by(email=email).first()
        # 查找不到用户
        if not user_model:
            raise wtforms.ValidationError("邮箱没有注册")
        # 密码不匹配
        pwhash = user_model.password
        self.user_id = user_model.id
        is_matched = check_password_hash(pwhash, password)
        if not is_matched:
            raise wtforms.ValidationError("密码不匹配")

class RegisterForm(wtforms.Form):
    username = wtforms.StringField(validators=[length(min=1,max=20,message="用户名至少1位,至多20位")])
    email = wtforms.StringField(validators=[email(message="邮箱不正确")])
    password = wtforms.StringField(validators=[length(min=6,max=20,message="密码必须至少六位")])
    password_confirm = wtforms.StringField(validators=[EqualTo("password")])
    # captcha = wtforms.StringField(validators=[length(min=4,max=4)])

    # def validate_captcha(self, field):
    #     captcha = field.data
    #     email = self.email.data
    #     captcha_model = CaptchaModel.query.filter_by(email=email).first()
    #     right_captcha = captcha_model.code
    #     if captcha != right_captcha:
    #         raise wtforms.ValidationError("验证码不正确")

    def validate_email(self, field):
        email = field.data
        usermodel = UserModel.query.filter_by(email=email).first()
        if usermodel:
            raise wtforms.ValidationError("邮箱已注册过")