# Generated by Django 3.2.7 on 2021-09-19 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0021_studentuni_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentuni',
            name='number',
            field=models.CharField(default='-', max_length=255),
        ),
    ]
