# Generated by Django 4.1.1 on 2022-09-13 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appProject', '0009_alter_product_sneakers_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_football_sneaker',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_hat',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_pant',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_sneakers',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_t_shirt',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=0),
            preserve_default=False,
        ),
    ]
