# Generated by Django 3.2.7 on 2021-09-20 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0024_remove_uniuni_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='uniuni',
            name='username',
            field=models.CharField(default='-', max_length=255),
        ),
    ]
