# Generated by Django 5.1.4 on 2025-01-05 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Campaign_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password_hash',
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]