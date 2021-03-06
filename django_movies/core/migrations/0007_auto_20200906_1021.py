# Generated by Django 3.1.1 on 2020-09-06 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200906_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='age_limit',
            field=models.IntegerField(blank=True, choices=[(7, '7'), (13, '13'), (16, '16'), (18, '18'), (21, '21')], null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.genre'),
        ),
    ]
