# Generated by Django 4.0.1 on 2022-01-12 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_group',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.productgroup'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.producttype'),
        ),
    ]
