# Generated by Django 3.2.7 on 2021-09-23 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_alter_order_amount'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Coupon',
        ),
    ]