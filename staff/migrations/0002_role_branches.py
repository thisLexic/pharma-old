# Generated by Django 3.0.6 on 2020-05-14 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='branches',
            field=models.ManyToManyField(blank=True, related_name='staffs', to='location.Branche'),
        ),
    ]
