from django.db import models

# Create your models here.
class User (models.Model):
    name = models.CharField('用户名', max_length=50)
    nickname = models.CharField('昵称', max_length=50)
    password = models.CharField('密码', max_length=20)
    province = models.CharField('省份', max_length=10)
    city = models.CharField('城市', max_length=10)
    openid = models.CharField('用户唯一标识', max_length=100)
    session_key = models.CharField('会话密钥', max_length=100)

    def __str__(self):
        return self.name