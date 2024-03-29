# Generated by Django 3.0.6 on 2020-05-23 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0016_auto_20200521_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banks',
            name='name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='expense_methods',
            name='name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='expense_types',
            name='name',
            field=models.CharField(max_length=64),
        ),
        migrations.AddConstraint(
            model_name='banks',
            constraint=models.UniqueConstraint(fields=('manager', 'name'), name='unique bank'),
        ),
        migrations.AddConstraint(
            model_name='expense_methods',
            constraint=models.UniqueConstraint(fields=('manager', 'name'), name='unique expense method'),
        ),
        migrations.AddConstraint(
            model_name='expense_types',
            constraint=models.UniqueConstraint(fields=('manager', 'name'), name='unique expense type'),
        ),
    ]
