# Generated by Django 5.1 on 2024-08-26 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_product_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='detail',
            field=models.TextField(blank=True, null=True),
        ),
    ]
