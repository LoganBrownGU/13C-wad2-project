# Generated by Django 2.2.28 on 2023-03-17 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0011_remove_review_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
