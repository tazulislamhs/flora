# Generated by Django 3.2.9 on 2021-11-28 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_article_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(default=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.CharField(max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
