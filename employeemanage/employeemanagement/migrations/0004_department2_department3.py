# Generated by Django 4.2.9 on 2024-05-13 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeemanagement', '0003_department1_remove_signupdatabase_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='department2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeename', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='department3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeename', models.CharField(max_length=128)),
            ],
        ),
    ]