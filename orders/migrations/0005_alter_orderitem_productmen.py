# Generated by Django 4.2.13 on 2024-06-23 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_remove_productchildish_color_and_more'),
        ('orders', '0004_orderitem_productmen_alter_orderitem_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='productmen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='products.productmen'),
        ),
    ]
