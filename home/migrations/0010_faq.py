# Generated by Django 2.1 on 2018-08-20 10:39

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_blogpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=1024, null=True)),
                ('answer', tinymce.models.HTMLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]