# Generated by Django 4.2.3 on 2023-08-04 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_age_profile_location_profile_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Geeks_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('roll', models.PositiveIntegerField()),
                ('author', models.CharField(max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]