from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField('名字',max_length=32)
    stu_ID = models.IntegerField('学号')
    gender = models.CharField('性别',max_length=16)
    class_stu =models.CharField('班级',max_length=32)
    seat = models.IntegerField('座位')
    course = models.CharField('课程',max_length=32)
    score = models.CharField('成绩',max_length=32)
    status =models.CharField('状态',max_length=32)

    def __str__(self):
        return self.name

