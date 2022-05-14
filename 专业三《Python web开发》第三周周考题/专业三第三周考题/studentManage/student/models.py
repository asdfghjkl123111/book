from django.db import models

# Create your models here.

class StudentModel(models.Model):
    num=models.CharField(max_length=32,verbose_name='学号')
    name=models.CharField(max_length=32,verbose_name='姓名')
    chinese=models.IntegerField(verbose_name='语文')
    maths=models.IntegerField(verbose_name='数学')
    english=models.IntegerField(verbose_name='英语')
    cls=models.ForeignKey(to='ClassModel',on_delete=models.DO_NOTHING,verbose_name='班级')

class  EntryModel(models.Model):
    user=models.CharField(max_length=32,verbose_name='用户')
    password=models.CharField(max_length=64,verbose_name='密码')

class ClassModel(models.Model):
    cname=models.CharField(max_length=32,verbose_name='教室名称')
    script=models.CharField(max_length=64,verbose_name='备注')
    def __str__(self):
        return self.cname


