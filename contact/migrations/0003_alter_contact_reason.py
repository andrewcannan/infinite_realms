# Generated by Django 3.2.21 on 2023-10-08 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20231008_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='reason',
            field=models.CharField(choices=[('', '--- Select Reason for Contact ---'), ('products', 'Inquiries about Products'), ('support', 'Customer Support or Technical Assistance'), ('feedback', 'Feedback or Suggestions'), ('wholesale', 'Wholesale or Bulk Orders'), ('privacy', 'Privacy Concerns or Data Requests'), ('marketing', 'Marketing or Advertising Inquiries'), ('orders', 'Recent Orders (Please include order number)'), ('general', 'General Questions or Comments')], max_length=100),
        ),
    ]
