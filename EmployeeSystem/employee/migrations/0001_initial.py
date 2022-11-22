# Generated by Django 4.1.3 on 2022-11-22 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('first_name', models.TextField(max_length=100)),
                ('last_name', models.TextField(max_length=100)),
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('emp_salary', models.FloatField()),
                ('emp_profile_picture', models.ImageField(default='profilepic.jpg', upload_to='profile_pictures')),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.TextField(max_length=1000)),
            ],
        ),
    ]