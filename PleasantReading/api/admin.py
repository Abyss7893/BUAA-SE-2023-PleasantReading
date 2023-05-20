import jwt
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.utils.crypto import get_random_string


# Register your models here.

def validateAccessToken(accessToken):
    try:
        decoded_token = jwt.decode(accessToken, settings.SECRET_KEY, algorithms=['HS256'])
        # 在这里可以根据需要进行其他的验证，例如检查有效期等
        
        # 如果验证通过，返回解码后的 token 数据
        return decoded_token
    except jwt.ExpiredSignatureError:
        # 访问令牌已过期
        return None
    except jwt.InvalidTokenError:
        # 无效的访问令牌
        return None

def getUserFromToken(token):
    decodedToken = validateAccessToken(token)
    if decodedToken:
        User = get_user_model()
        try:
            user_id = decodedToken['user_id']
            user = User.objects.get(id=user_id)
            return user
        except:
            pass
    return None

def sendVerificationEmail(email):
    # 生成验证码
    verificationCode = get_random_string(length=6)

    # 构建邮件内容
    subject = '验证码邮件'
    message = f'欢迎您使用怡心阅读，您的验证码是：{verificationCode}'
    fromEmail = 'abyss7893@163.com'
    recipientList = [email]

    # 发送邮件
    send_mail(subject, message, fromEmail, recipientList)

    # 返回生成的验证码
    return verificationCode