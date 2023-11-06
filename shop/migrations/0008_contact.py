# Generated by Django 4.2.7 on 2023-11-04 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=156, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('message', models.TextField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Contact',
                'db_table': 'tabContact',
            },
        ),
    ]
