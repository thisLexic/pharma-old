# Generated by Django 3.0.6 on 2020-05-22 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0010_auto_20200522_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_id',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]