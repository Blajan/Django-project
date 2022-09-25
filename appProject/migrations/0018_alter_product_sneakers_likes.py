# Generated by Django 4.1.1 on 2022-09-17 07:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appProject', '0017_product_sneakers_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_sneakers',
            name='likes',
            field=models.ManyToManyField(related_name='sneakers', to=settings.AUTH_USER_MODEL),
        ),
    ]
