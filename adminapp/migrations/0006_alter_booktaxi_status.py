# Generated by Django 3.2.3 on 2021-06-01 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0005_alter_car_kilometer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booktaxi',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
