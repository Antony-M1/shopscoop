# Generated by Django 4.2.7 on 2023-11-03 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_productdetails'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductDetails',
        ),
    ]