# Generated by Django 3.2.9 on 2021-12-06 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0004_article_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='dislike',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='soso',
            field=models.IntegerField(default=0),
        ),
    ]
