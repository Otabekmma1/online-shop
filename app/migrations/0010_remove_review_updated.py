# Generated by Django 5.0.3 on 2024-03-26 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_category_created_category_updated_customer_updated_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='updated',
        ),
    ]
