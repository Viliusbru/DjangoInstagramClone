# Generated by Django 3.2 on 2021-05-19 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsas', '0003_alter_post_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilis',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]