# Generated by Django 4.2.9 on 2024-05-14 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeemanagement', '0004_department2_department3'),
    ]

    operations = [
        migrations.CreateModel(
            name='profileimagedb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profileimage', models.ImageField(upload_to='photos/')),
            ],
        ),
    ]
