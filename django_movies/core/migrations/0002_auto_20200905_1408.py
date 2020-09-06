# Generated by Django 3.1.1 on 2020-09-05 12:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(15), django.core.validators.MinValueValidator(1)]),
        ),
    ]
