# Generated by Django 5.0.4 on 2024-04-13 18:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_salary', models.IntegerField(verbose_name='Basic Salary')),
                ('allowances', models.IntegerField(default=0, verbose_name='Allowance')),
                ('deductions', models.IntegerField(default=0, verbose_name='Deduction')),
                ('final_salary', models.IntegerField(default=0, verbose_name='Final Salary')),
                ('generated_at', models.DateTimeField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Deduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(verbose_name='Amount')),
                ('salary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salary_deductions', to='payment.salary')),
            ],
        ),
        migrations.CreateModel(
            name='Allowance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(verbose_name='Amount')),
                ('salary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salary_allowances', to='payment.salary')),
            ],
        ),
    ]
