# Generated by Django 5.1.4 on 2025-01-06 12:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Campaign_app', '0003_user_id_alter_user_email_alter_user_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
