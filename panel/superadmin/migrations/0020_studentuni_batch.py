# Generated by Django 3.2.7 on 2021-09-19 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0019_schedulemsg_msg'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentuni',
            name='batch',
            field=models.CharField(default='-', max_length=255),
        ),
    ]