# Generated by Django 3.0.6 on 2020-05-24 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0021_auto_20200524_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='bank',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='finance.Banks'),
        ),
    ]
