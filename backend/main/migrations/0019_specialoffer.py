# Generated by Django 3.2.8 on 2022-04-20 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_product_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('slug', models.SlugField(unique=True, verbose_name='Public Url')),
                ('products', models.ManyToManyField(to='main.Product')),
            ],
        ),
    ]
