# Generated by Django 3.0.6 on 2020-05-20 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0006_sales_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='expenses'),
        ),
        migrations.AlterField(
            model_name='sales',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='sales'),
        ),
    ]
