# Generated by Django 3.2 on 2021-05-19 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsas', '0002_alter_profilis_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comment',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
