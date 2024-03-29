# Generated by Django 3.0.6 on 2020-05-23 02:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock', '0011_auto_20200522_1559'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchasePaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('is_active', models.BooleanField(default=True)),
                ('manager', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchase_payment_method', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Purchase Payment Method',
                'verbose_name_plural': 'Purchase Payment Methods',
            },
        ),
        migrations.AddConstraint(
            model_name='purchasepaymentmethod',
            constraint=models.UniqueConstraint(fields=('manager', 'name'), name='unique purchase payment method'),
        ),
    ]
