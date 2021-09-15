# Generated by Django 3.2.7 on 2021-09-13 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0002_user_is_super_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_member',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
    ]
