# Generated by Django 3.2.12 on 2022-04-30 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20220501_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Additionally',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Additionally'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Bezel_material',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Bezel material'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Box',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Box'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Bracelet_color',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Bracelet/strap color'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Bracelet_material',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Bracelet/strap material'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Bracelet_strap',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Bracelet/strap'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Caliber',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Caliber'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Case_diameter',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Case diameter'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Case_material',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Case material'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Case_size',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Case size'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Clasp_Fold_clasp',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Clasp Fold clasp'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Clasp_material',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Clasp material'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Clock_face',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Clock-face'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Comments_to_the_color',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Comments to the color'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Crystal',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Crystal'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Dial',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Dial'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Dial_blue',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Dial Blue'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Dial_colour',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Dial_colour'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Dial_numerals',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Dial numerals'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Features',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Features'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Functions',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Functions'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Gender',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Glass',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Glass'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Guarantee',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Guarantee'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Location',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Mechanism',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Mechanism'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Movement',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Movement'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Movement_Caliber',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Movement/Caliber'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Note',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Note'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Number_of_jewels',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Number of jewels'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Power_reserve',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Power reserve'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Ref',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ref'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Specifications',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Specifications'),
        ),
        migrations.AlterField(
            model_name='product',
            name='The_case_shape',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='The case shape'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Thickness',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Thickness'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Total_height',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Total height'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Water_resistance',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Water resistance'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Year_of_production',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Year of production'),
        ),
    ]
