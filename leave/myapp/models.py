from django.db import models

# Create your models here.

class UserModel(models.Model):
    uname=models.CharField(max_length=32,null=True,verbose_name='用户名称')
    upwd=models.CharField(max_length=64,null=True,verbose_name='密码')
    choice={
        (1,'学生'),
        (2,'老师')
    }
    role=models.IntegerField(choices=choice,verbose_name='角色')


class LevelModel(models.Model):
    tname=models.CharField(max_length=32,null=True)

class MouldModel(models.Model):
    stu_name=models.CharField(max_length=32,null=True,verbose_name='学生名称')
    choice = {
        (0, '待审核'),
        (1, '通过'),
        (2,'未通过')
    }
    status=models.IntegerField(choices=choice,verbose_name='状态')
    createtime=models.DateTimeField(null=True,verbose_name='创建时间')
    context=models.TextField(verbose_name='事由',max_length=200)
    tid=models.ForeignKey(to='LevelModel',on_delete=models.DO_NOTHING,verbose_name='外键')
