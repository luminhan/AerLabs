# Generated by Django 4.0.3 on 2022-03-20 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('Id', models.CharField(max_length=12, primary_key=True, serialize=False, unique=True)),
                ('type', models.CharField(blank=True, max_length=225, null=True)),
                ('name', models.CharField(max_length=225)),
                ('latitude_deg', models.DecimalField(decimal_places=9, max_digits=12)),
                ('longitude_deg', models.DecimalField(decimal_places=9, max_digits=12)),
                ('gps_code', models.CharField(blank=True, max_length=6, null=True)),
                ('iata_code', models.CharField(blank=True, max_length=4, null=True)),
            ],
        ),
    ]
