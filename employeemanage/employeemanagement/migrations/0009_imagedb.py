# Generated by Django 4.2.9 on 2024-05-14 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeemanagement', '0008_trainingdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='imagedb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos/')),
            ],
        ),
    ]
