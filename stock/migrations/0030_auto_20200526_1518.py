# Generated by Django 3.0.6 on 2020-05-26 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0029_transactions_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchases',
            name='payment_method',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='stock.Purchase_Payment_Method'),
        ),
    ]
