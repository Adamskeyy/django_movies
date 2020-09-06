# Generated by Django 3.1.1 on 2020-09-06 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20200906_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='countries',
            field=models.ManyToManyField(related_name='movies', to='core.Country'),
        ),
    ]
