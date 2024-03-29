# Generated by Django 3.0.6 on 2020-07-09 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0009_auto_20200523_1051'),
        ('staff', '0046_roles_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='roles',
            name='hours_in_branches',
            field=models.ManyToManyField(blank=True, related_name='hours_in_staffs', to='location.Branches'),
        ),
        migrations.AddField(
            model_name='roles',
            name='hours_in_days',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
