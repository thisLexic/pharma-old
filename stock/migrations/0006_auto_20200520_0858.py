# Generated by Django 3.0.6 on 2020-05-20 08:58

from django.db import migrations
import private_storage.fields
import private_storage.storage.files


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_auto_20200520_0640'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchases',
            name='invoice_file',
            field=private_storage.fields.PrivateFileField(blank=True, null=True, storage=private_storage.storage.files.PrivateFileSystemStorage(), upload_to='purchases/invoices'),
        ),
        migrations.AddField(
            model_name='purchases',
            name='proof_of_payment',
            field=private_storage.fields.PrivateFileField(blank=True, null=True, storage=private_storage.storage.files.PrivateFileSystemStorage(), upload_to='purchases/proofOfPayment'),
        ),
    ]
