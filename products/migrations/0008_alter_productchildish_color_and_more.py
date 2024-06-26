# Generated by Django 4.2.13 on 2024-06-06 11:30

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_productchildish_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productchildish',
            name='color',
            field=colorfield.fields.ColorField(choices=[('#8b0000', 'red'), ('#ffff00', 'yellow'), ('#006400', 'green')], default='#FFFFFF', image_field=None, max_length=10, samples=None, verbose_name='what is your color?'),
        ),
        migrations.AlterField(
            model_name='productfeminine',
            name='color',
            field=colorfield.fields.ColorField(choices=[('#8b0000', 'red'), ('#ffff00', 'yellow'), ('#006400', 'green')], default='#FFFFFF', image_field=None, max_length=10, samples=None, verbose_name='what is your color?'),
        ),
        migrations.AlterField(
            model_name='productmen',
            name='color',
            field=colorfield.fields.ColorField(choices=[('#8b0000', 'red'), ('#ffff00', 'yellow'), ('#006400', 'green')], default='#FFFFFF', image_field=None, max_length=10, samples=None, verbose_name='what is your color?'),
        ),
    ]
