# Generated by Django 4.2.13 on 2024-05-30 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_productchildish_productcooking_productfeminine_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='productWashing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='products.productwashing'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='productchildish',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='products.productchildish'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='productcooking',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='products.productcooking'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='productfeminine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='products.productfeminine'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='productheadphone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='products.productheadphone'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='productlaptop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='products.productlaptop'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='productlist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='products.productlist'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='productmen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='products.productmen'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='productoffice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='products.productoffice'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='productrefrigerator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='products.productrefrigerator'),
        ),
    ]
