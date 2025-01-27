# Generated by Django 5.1.4 on 2025-01-05 04:43

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('legal_name', models.CharField(max_length=255)),
                ('registration_number', models.CharField(max_length=200)),
                ('company_address', models.TextField()),
                ('billing_address', models.TextField()),
                ('website', models.URLField()),
                ('logo', models.URLField()),
                ('primary_color', models.CharField(max_length=20)),
                ('secondary_color', models.CharField(max_length=20)),
                ('billing_email', models.EmailField(max_length=254)),
                ('support_email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=100)),
                ('time_zone', models.CharField(max_length=50)),
                ('currency', models.CharField(max_length=10)),
                ('language', models.CharField(max_length=20)),
                ('subscription_status', models.CharField(max_length=50)),
                ('subscription_plan', models.CharField(max_length=50)),
                ('trail_ends_at', models.DateTimeField()),
                ('settings', models.JSONField()),
                ('branding', models.JSONField()),
                ('is_verified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AgencyBilling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(max_length=200)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(max_length=50)),
                ('due_date', models.DateTimeField()),
                ('paid_date', models.DateTimeField()),
                ('payment_method', models.CharField(max_length=50)),
                ('line_items', models.JSONField()),
                ('currency', models.CharField(max_length=20)),
                ('is_paid', models.BooleanField(default=False)),
                ('pdf_url', models.URLField()),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Campaign_app.agency')),
            ],
        ),
        migrations.CreateModel(
            name='AgencySubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('billing_cycle', models.CharField(max_length=50)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('status', models.CharField(max_length=50)),
                ('team_member_limit', models.IntegerField()),
                ('client_limit', models.IntegerField()),
                ('features', models.JSONField()),
                ('payment_method', models.CharField(max_length=50)),
                ('last_payment_date', models.DateTimeField()),
                ('next_billing_date', models.DateTimeField()),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Campaign_app.agency')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('password_hash', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('auth_provider', models.CharField(blank=True, max_length=255, null=True)),
                ('oauth_token', models.JSONField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=100)),
                ('profile_picture', models.URLField(blank=True)),
                ('time_zone', models.CharField(blank=True, max_length=50, null=True)),
                ('preferences', models.JSONField(blank=True, null=True)),
                ('language', models.CharField(blank=True, max_length=50, null=True)),
                ('email_verified', models.BooleanField(default=False)),
                ('phone_verified', models.BooleanField(default=False)),
                ('last_password_change', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('is_read', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('metadata', models.JSONField()),
                ('priority', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AgencyTeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('permissions', models.JSONField()),
                ('joined_at', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField()),
                ('invitation_status', models.CharField(max_length=80)),
                ('department', models.CharField(max_length=100)),
                ('hourly_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('assigned_clients', models.JSONField()),
                ('notification_preferences', models.JSONField()),
                ('emergency_contact', models.CharField(max_length=255)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Campaign_app.agency')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
