# Generated by Django 3.0.6 on 2020-05-22 10:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('location', '0005_branches_manager'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currect_Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cur_staff', to='location.Branches')),
                ('manager', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='staff_branches', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='cur_branch', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]