# Generated by Django 4.2.13 on 2024-08-17 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_remove_orderitem_product_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='zarinpal_authority',
            new_name='authority',
        ),
    ]
