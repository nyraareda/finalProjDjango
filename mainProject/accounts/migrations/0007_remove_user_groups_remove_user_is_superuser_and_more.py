# Generated by Django 5.0.4 on 2024-04-16 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_user_groups_user_is_superuser_user_last_login_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
    ]
