# Generated by Django 4.1.1 on 2022-09-17 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appProject', '0020_product_football_sneakers_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='social_media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website_url', models.CharField(blank=True, max_length=255, null=True)),
                ('facebook_url', models.CharField(blank=True, max_length=255, null=True)),
                ('instagram_url', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter_url', models.CharField(blank=True, max_length=255, null=True)),
                ('linkedin_url', models.CharField(blank=True, max_length=255, null=True)),
                ('github_url', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
