# Generated by Django 3.0.6 on 2020-05-22 10:21

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('location', '0006_currect_branch'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Currect_Branch',
            new_name='Current_Branch',
        ),
    ]