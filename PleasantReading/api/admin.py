import jwt
from django.conf import settings
from django.contrib import admin

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