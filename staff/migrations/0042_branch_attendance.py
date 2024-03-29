# Generated by Django 3.0.6 on 2020-06-24 10:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import private_storage.fields
import private_storage.storage.files
import staff.models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0009_auto_20200523_1051'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('staff', '0041_auto_20200618_2233'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch_Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('image', private_storage.fields.PrivateFileField(null=True, storage=private_storage.storage.files.PrivateFileSystemStorage(), upload_to=staff.models.Branch_Attendance.user_directory_path)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendance', to='location.Branches')),
                ('manager', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='branch_attendance', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Branch Attendance',
                'verbose_name_plural': 'Branch Attendance',
            },
        ),
    ]
