from django.db import models
from django.utils.timezone import now

# Create your models here.
class adminUser (models.Model):
    TYPE = (
        ('A', '管理员'),
        ('B', '普通用户')
    )
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    creatDate = models.DateTimeField('创建时间', default=now)
    activation = models.BooleanField('是否激活', default=True)
    type = models.CharField('类型', max_length=1, choices=TYPE, default='B')

    def __str__(self):
        return self.name