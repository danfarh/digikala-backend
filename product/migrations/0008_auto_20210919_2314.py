# Generated by Django 3.2.7 on 2021-09-19 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_brand_headline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='headline',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='name',
        ),
        migrations.AddField(
            model_name='brand',
            name='en_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='brand',
            name='fa_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='BrandMultiLanguage',
        ),
    ]
