# Generated by Django 3.1.7 on 2021-04-27 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_product_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ingredients',
            field=models.TextField(default=''),
        ),
    ]
