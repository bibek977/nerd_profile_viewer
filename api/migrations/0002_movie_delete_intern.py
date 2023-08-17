# Generated by Django 4.2.3 on 2023-08-17 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('actor', models.CharField(max_length=100)),
                ('actress', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('writer', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('year', models.PositiveIntegerField()),
                ('runtime', models.IntegerField()),
                ('imdb', models.FloatField()),
                ('summary', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Intern',
        ),
    ]