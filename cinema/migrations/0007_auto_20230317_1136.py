# Generated by Django 2.2.28 on 2023-03-17 11:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cinema', '0006_auto_20230310_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='likes',
        ),
        migrations.AddField(
            model_name='review',
            name='likes',
            field=models.ManyToManyField(related_name='review_like', to=settings.AUTH_USER_MODEL),
        ),
    ]