# Generated by Django 4.2.7 on 2023-11-06 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_blog_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='description',
        ),
    ]
