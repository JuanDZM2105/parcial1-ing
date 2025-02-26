# Generated by Django 5.1.3 on 2025-02-26 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('flight_type', models.CharField(choices=[('NTL', 'Nacional'), ('INTL', 'Internacional')], max_length=4)),
            ],
        ),
    ]
