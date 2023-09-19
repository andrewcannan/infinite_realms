# Generated by Django 3.2.21 on 2023-09-18 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_manufacturer'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub_category',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category'),
        ),
    ]