# Generated by Django 2.1 on 2018-09-30 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='pr_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
