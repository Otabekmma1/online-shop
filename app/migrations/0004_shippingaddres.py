# Generated by Django 5.0.3 on 2024-03-26 20:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingAddres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addres', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=20)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.customer')),
            ],
        ),
    ]
