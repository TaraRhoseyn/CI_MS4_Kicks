# Generated by Django 4.0.1 on 2022-01-20 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_product_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.CharField(default='SOME STRING', max_length=40),
        ),
    ]
