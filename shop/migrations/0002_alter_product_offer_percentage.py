# Generated by Django 4.2.7 on 2023-11-03 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='offer_percentage',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
