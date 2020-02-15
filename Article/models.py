from django.db import models

# Create your models here.
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32,verbose_name='作者姓名')
    gender = models.CharField(max_length=32,verbose_name='性别')
    age = models.IntegerField(verbose_name='年龄')
    email = models.EmailField(32)
    class Meta:
        db_table = 'Author'

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32,verbose_name='标题')
    date = models.DateTimeField(verbose_name='时间日期')
    content = models.TextField(verbose_name='文章内容')
    description = models.TextField(verbose_name='文章描述')
    Author = models.ForeignKey(to=Author,to_field='id',on_delete=models.CASCADE)
    class Meta:
        db_table = 'Article'

class Type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32,verbose_name='名字')
    description = models.TextField(verbose_name='描述')
    Article = models.ManyToManyField(to=Article)
    class Meta:
        db_table = 'Type'
        verbose_name = '类型'
        verbose_name_plural = '类型'

