# Generated by Django 2.2.28 on 2023-03-17 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0007_auto_20230317_1136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='likes',
        ),
        migrations.AddField(
            model_name='review',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]