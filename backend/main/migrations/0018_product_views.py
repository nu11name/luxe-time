# Generated by Django 3.2.8 on 2022-04-20 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20220420_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='views',
            field=models.PositiveIntegerField(default=0, editable=False, verbose_name='Views'),
        ),
    ]
