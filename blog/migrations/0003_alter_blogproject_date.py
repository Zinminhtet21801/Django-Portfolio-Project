# Generated by Django 3.2 on 2021-04-22 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210423_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogproject',
            name='date',
            field=models.DateField(),
        ),
    ]
