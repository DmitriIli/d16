# Generated by Django 4.1.7 on 2023-02-17 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='text',
            field=models.CharField(default='текст статьи от 2023-02-17 02:09:22.490529', max_length=512),
        ),
        migrations.AlterField(
            model_name='ads',
            name='title',
            field=models.CharField(default='заголовок статьи от 2023-02-17 02:09:22.490510', max_length=64),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='text',
            field=models.CharField(default='текст отклика от 2023-02-17 02:09:22.490735', max_length=256),
        ),
    ]
