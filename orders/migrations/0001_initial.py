# Generated by Django 4.2.13 on 2024-06-09 21:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0008_alter_productchildish_color_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Is Paid?')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Phone Number')),
                ('address', models.CharField(max_length=700, verbose_name='Address')),
                ('order_notes', models.CharField(blank=True, max_length=700, verbose_name='Order Notes')),
                ('zarinpal_authority', models.CharField(blank=True, max_length=255)),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('datetime_modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('price', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='products.productoffice')),
            ],
        ),
    ]
