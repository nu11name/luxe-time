# Generated by Django 3.2.12 on 2022-05-01 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Additionally_ge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ge-Additionally'),
        ),
        migrations.AddField(
            model_name='product',
            name='Additionally_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ru-Additionally'),
        ),
        migrations.AddField(
            model_name='product',
            name='Bezel_material_ge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ge-Bezel material'),
        ),
        migrations.AddField(
            model_name='product',
            name='Bezel_material_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ru-Bezel material'),
        ),
        migrations.AddField(
            model_name='product',
            name='Box_ge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ge-Box'),
        ),
        migrations.AddField(
            model_name='product',
            name='Box_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ru-Box'),
        ),
        migrations.AddField(
            model_name='product',
            name='Bracelet_color_ge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ge-Bracelet/strap color'),
        ),
        migrations.AddField(
            model_name='product',
            name='Bracelet_color_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ru-Bracelet/strap color'),
        ),
        migrations.AddField(
            model_name='product',
            name='Bracelet_material_ge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ge-Bracelet/strap material'),
        ),
        migrations.AddField(
            model_name='product',
            name='Bracelet_material_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ru-Bracelet/strap material'),
        ),
        migrations.AddField(
            model_name='product',
            name='Bracelet_strap_ge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ge-Bracelet/strap'),
        ),
        migrations.AddField(
            model_name='product',
            name='Bracelet_strap_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ru-Bracelet/strap'),
        ),
        migrations.AddField(
            model_name='product',
            name='Caliber_ge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ge-Caliber'),
        ),
        migrations.AddField(
            model_name='product',
            name='Caliber_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ru-Caliber'),
        ),
        migrations.AddField(
            model_name='product',
            name='Case_diameter_ge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ge-Case diameter'),
        ),
        migrations.AddField(
            model_name='product',
            name='Case_diameter_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ru-Case diameter'),
        ),
        migrations.AddField(
            model_name='product',
            name='Case_material_ge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ge-Case material'),
        ),
        migrations.AddField(
            model_name='product',
            name='Case_material_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ru-Case material'),
        ),
        migrations.AddField(
            model_name='product',
            name='Case_size_ge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ge-Case size'),
        ),
        migrations.AddField(
            model_name='product',
            name='Case_size_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ru-Case size'),
        ),
        migrations.AddField(
            model_name='product',
            name='Clasp_Fold_clasp_ge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ge-Clasp Fold clasp'),
        ),
        migrations.AddField(
            model_name='product',
            name='Clasp_Fold_clasp_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ru-Clasp Fold clasp'),
        ),
        migrations.AddField(
            model_name='product',
            name='Clasp_material_ge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ge-Clasp material'),
        ),
        migrations.AddField(
            model_name='product',
            name='Clasp_material_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ru-Clasp material'),
        ),
        migrations.AddField(
            model_name='product',
            name='Clock_face_ge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ge-Clock-face'),
        ),
        migrations.AddField(
            model_name='product',
            name='Clock_face_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ru-Clock-face'),
        ),
        migrations.AddField(
            model_name='product',
            name='Comments_to_the_color_ge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ge-Comments to the color'),
        ),
        migrations.AddField(
            model_name='product',
            name='Comments_to_the_color_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ru-Comments to the color'),
        ),
        migrations.AddField(
            model_name='product',
            name='Crystal_ge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ge-Crystal'),
        ),
        migrations.AddField(
            model_name='product',
            name='Crystal_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ru-Crystal'),
        ),
        migrations.AddField(
            model_name='product',
            name='Dial_blue_ge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ge-Dial Blue'),
        ),
        migrations.AddField(
            model_name='product',
            name='Dial_blue_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ru-Dial Blue'),
        ),
        migrations.AddField(
            model_name='product',
            name='Dial_colour_ge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ge-Dial_colour'),
        ),
        migrations.AddField(
            model_name='product',
            name='Dial_colour_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ru-Dial_colour'),
        ),
        migrations.AddField(
            model_name='product',
            name='Dial_ge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ge-Dial'),
        ),
        migrations.AddField(
            model_name='product',
            name='Dial_numerals_ge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ge-Dial numerals'),
        ),
        migrations.AddField(
            model_name='product',
            name='Dial_numerals_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ru-Dial numerals'),
        ),
        migrations.AddField(
            model_name='product',
            name='Dial_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ru-Dial'),
        ),
        migrations.AddField(
            model_name='product',
            name='Features_ge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ge-Features'),
        ),
        migrations.AddField(
            model_name='product',
            name='Features_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ru-Features'),
        ),
        migrations.AddField(
            model_name='product',
            name='Functions_ge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ge-Functions'),
        ),
        migrations.AddField(
            model_name='product',
            name='Functions_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ru-Functions'),
        ),
        migrations.AddField(
            model_name='product',
            name='Gender_ge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ge-Gender'),
        ),
        migrations.AddField(
            model_name='product',
            name='Gender_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ru-Gender'),
        ),
        migrations.AddField(
            model_name='product',
            name='Glass_ge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ge-Glass'),
        ),
        migrations.AddField(
            model_name='product',
            name='Glass_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ru-Glass'),
        ),
        migrations.AddField(
            model_name='product',
            name='Guarantee_ge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ge-Guarantee'),
        ),
        migrations.AddField(
            model_name='product',
            name='Guarantee_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ru-Guarantee'),
        ),
        migrations.AddField(
            model_name='product',
            name='Location_ge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ge-Location'),
        ),
        migrations.AddField(
            model_name='product',
            name='Location_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ru-Location'),
        ),
        migrations.AddField(
            model_name='product',
            name='Mechanism_ge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ge-Mechanism'),
        ),
        migrations.AddField(
            model_name='product',
            name='Mechanism_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ru-Mechanism'),
        ),
        migrations.AddField(
            model_name='product',
            name='Movement_Caliber_ge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ge-Movement/Caliber'),
        ),
        migrations.AddField(
            model_name='product',
            name='Movement_Caliber_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ru-Movement/Caliber'),
        ),
        migrations.AddField(
            model_name='product',
            name='Movement_ge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ge-Movement'),
        ),
        migrations.AddField(
            model_name='product',
            name='Movement_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ru-Movement'),
        ),
        migrations.AddField(
            model_name='product',
            name='Note_ge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ge-Note'),
        ),
        migrations.AddField(
            model_name='product',
            name='Note_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ru-Note'),
        ),
        migrations.AddField(
            model_name='product',
            name='Number_of_jewels_ge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ge-Number of jewels'),
        ),
        migrations.AddField(
            model_name='product',
            name='Number_of_jewels_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ru-Number of jewels'),
        ),
        migrations.AddField(
            model_name='product',
            name='Power_reserve_ge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ge-Power reserve'),
        ),
        migrations.AddField(
            model_name='product',
            name='Power_reserve_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ru-Power reserve'),
        ),
        migrations.AddField(
            model_name='product',
            name='Ref_ge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ge-Ref'),
        ),
        migrations.AddField(
            model_name='product',
            name='Ref_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ru-Ref'),
        ),
        migrations.AddField(
            model_name='product',
            name='Specifications_ge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ge-Specifications'),
        ),
        migrations.AddField(
            model_name='product',
            name='Specifications_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ru-Specifications'),
        ),
        migrations.AddField(
            model_name='product',
            name='The_case_shape_ge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ge-The case shape'),
        ),
        migrations.AddField(
            model_name='product',
            name='The_case_shape_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ru-The case shape'),
        ),
        migrations.AddField(
            model_name='product',
            name='Thickness_ge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ge-Thickness'),
        ),
        migrations.AddField(
            model_name='product',
            name='Thickness_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ru-Thickness'),
        ),
        migrations.AddField(
            model_name='product',
            name='Total_height_ge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ge-Total height'),
        ),
        migrations.AddField(
            model_name='product',
            name='Total_height_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ru-Total height'),
        ),
        migrations.AddField(
            model_name='product',
            name='Water_resistance_ge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ge-Water resistance'),
        ),
        migrations.AddField(
            model_name='product',
            name='Water_resistance_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ru-Water resistance'),
        ),
        migrations.AddField(
            model_name='product',
            name='Year_of_production_ge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ge-Year of production'),
        ),
        migrations.AddField(
            model_name='product',
            name='Year_of_production_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ru-Year of production'),
        ),
    ]
