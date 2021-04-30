# Generated by Django 3.2 on 2021-04-22 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogproject',
            name='image',
        ),
        migrations.RemoveField(
            model_name='blogproject',
            name='url',
        ),
        migrations.AddField(
            model_name='blogproject',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='blogproject',
            name='description',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='blogproject',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]