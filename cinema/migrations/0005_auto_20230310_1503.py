# Generated by Django 2.1.5 on 2023-03-10 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0004_auto_20230309_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
