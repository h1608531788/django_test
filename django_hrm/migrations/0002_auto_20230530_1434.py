# Generated by Django 3.0.14 on 2023-05-30 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_hrm', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='commodity',
            table='business_shop_commodity',
        ),
        migrations.AlterModelTable(
            name='shop',
            table='business_shop',
        ),
        migrations.AlterModelTable(
            name='shopstyle',
            table='business_shop_style',
        ),
        migrations.AlterModelTable(
            name='shoptostyle',
            table='business_shop_to_style',
        ),
    ]