# Generated by Django 4.1.7 on 2023-02-21 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_ads_text_alter_ads_title_alter_reply_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='text',
            field=models.CharField(default='текст статьи от 2023-02-21 12:58:34.023559', max_length=512),
        ),
        migrations.AlterField(
            model_name='ads',
            name='title',
            field=models.CharField(default='заголовок статьи от 2023-02-21 12:58:34.023539', max_length=64),
        ),
        migrations.AlterField(
            model_name='reply',
            name='text',
            field=models.CharField(default='текст отклика от 2023-02-21 12:58:34.023790', max_length=256),
        ),
    ]
