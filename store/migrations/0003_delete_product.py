# Generated by Django 3.2 on 2021-04-06 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_products_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]
