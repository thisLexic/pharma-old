# Generated by Django 3.0.6 on 2020-05-20 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_auto_20200520_0639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchases',
            name='invoice_file',
        ),
        migrations.RemoveField(
            model_name='purchases',
            name='proof_of_payment',
        ),
    ]
