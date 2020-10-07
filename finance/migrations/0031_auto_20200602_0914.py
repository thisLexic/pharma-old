# Generated by Django 3.0.6 on 2020-06-02 01:14

from django.db import migrations, models
import finance.models
import private_storage.fields
import private_storage.storage.files


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0030_expenses_prf_pay'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses',
            name='attch_doc',
            field=private_storage.fields.PrivateFileField(blank=True, null=True, storage=private_storage.storage.files.PrivateFileSystemStorage(), upload_to=finance.models.Expenses.user_directory_path_attch_doc),
        ),
        migrations.AddField(
            model_name='expenses',
            name='doc_desc',
            field=models.CharField(blank=True, default='extra-doc', max_length=64),
        ),
    ]