# Generated by Django 4.1.3 on 2022-11-22 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_alter_employee_first_name_alter_employee_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.TextField(default=' ', max_length=1000),
        ),
    ]
