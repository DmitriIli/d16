# Generated by Django 4.1.7 on 2023-02-19 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_ads_text_alter_ads_title_alter_feedback_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='text',
            field=models.CharField(default='текст статьи от 2023-02-19 14:04:13.723463', max_length=512),
        ),
        migrations.AlterField(
            model_name='ads',
            name='title',
            field=models.CharField(default='заголовок статьи от 2023-02-19 14:04:13.723444', max_length=64),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='text',
            field=models.CharField(default='текст отклика от 2023-02-19 14:04:13.723678', max_length=256),
        ),
    ]