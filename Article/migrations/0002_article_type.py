# Generated by Django 2.2.1 on 2020-02-15 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('date', models.DateTimeField(verbose_name='时间日期')),
                ('content', models.TextField(verbose_name='文章内容')),
                ('description', models.TextField(verbose_name='文章描述')),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Article.Author')),
            ],
            options={
                'db_table': 'Article',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32, verbose_name='名字')),
                ('description', models.TextField(verbose_name='描述')),
                ('Article', models.ManyToManyField(to='Article.Article')),
            ],
            options={
                'verbose_name_plural': '类型',
                'verbose_name': '类型',
                'db_table': 'Type',
            },
        ),
    ]