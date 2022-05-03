# Generated by Django 3.2.12 on 2022-05-02 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_alter_productimage_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_en', models.CharField(blank=True, max_length=256, null=True, verbose_name='Title_en')),
                ('title_ge', models.CharField(blank=True, max_length=256, null=True, verbose_name='Title_ge')),
                ('title_ru', models.CharField(blank=True, max_length=256, null=True, verbose_name='Title_ru')),
                ('description_en', models.CharField(blank=True, max_length=256, null=True, verbose_name='Description_en')),
                ('description_ge', models.CharField(blank=True, max_length=256, null=True, verbose_name='Description_ge')),
                ('description_ru', models.CharField(blank=True, max_length=256, null=True, verbose_name='Description_ru')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
            ],
        ),
    ]