# Generated by Django 3.1.1 on 2020-09-06 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20200906_1405'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ('name',)},
        ),
    ]
