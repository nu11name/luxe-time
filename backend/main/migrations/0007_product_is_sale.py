# Generated by Django 3.2.8 on 2022-04-20 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_product_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_sale',
            field=models.BooleanField(blank=True, editable=False, null=True, verbose_name='Is sale'),
        ),
    ]
