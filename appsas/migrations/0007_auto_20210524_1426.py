# Generated by Django 3.2 on 2021-05-24 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appsas', '0006_postcomment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comment',
        ),
        migrations.DeleteModel(
            name='UserFollowing',
        ),
    ]
