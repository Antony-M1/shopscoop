# Generated by Django 4.2.7 on 2023-11-03 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=500)),
                ('actual_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('offer_percentage', models.DecimalField(decimal_places=2, max_digits=4)),
                ('final_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Product Details',
                'db_table': 'tabProductDetails',
            },
        ),
    ]
