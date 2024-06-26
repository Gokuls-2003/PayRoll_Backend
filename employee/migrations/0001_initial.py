# Generated by Django 5.0.4 on 2024-04-13 17:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_id', models.EmailField(blank=True, max_length=100, null=True, verbose_name='Email Id')),
                ('contact_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone Number')),
                ('role', models.CharField(choices=[('SD', 'Software Developer'), ('T', 'Tester'), ('D', 'Designer'), ('M', 'Manager')], default=None, max_length=3, verbose_name='role')),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Strart Date')),
                ('end_date', models.DateField(verbose_name='end Date')),
                ('reason', models.TextField(max_length=200, verbose_name='Reason')),
                ('leave_status', models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('D', 'Denied')], default='P', max_length=1, verbose_name='Leave Status')),
                ('Employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
