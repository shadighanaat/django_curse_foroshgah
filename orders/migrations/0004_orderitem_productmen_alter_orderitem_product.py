# Generated by Django 4.2.13 on 2024-06-22 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_remove_productchildish_color_and_more'),
        ('orders', '0003_alter_orderitem_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='productmen',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='order_items_men', to='products.productmen'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='products.product'),
        ),
    ]
