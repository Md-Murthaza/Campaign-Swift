from django.db import models

# Create your models here.

# == User models 

class User(models.Model):
    email = models.EmailField(primary_key=True)
    username = models.CharField(max_length=200)
    password_hash = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.CharField(default=False)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField(auto_now_add=True)
    auth_provider = models.CharField(max_length=255)
    oauth_token = models.JSONField()


# == User Profile models

class UserProfile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=100)
    profile_picture = models.URLField()
    time_zone = models.CharField(max_length=50)
    preferences = models.JSONField()
    language = models.CharField(max_length=50)
    email_verified = models.BooleanField(default=False)
    phone_verified = models.BooleanField(default=False)
    last_password_change = models.DateTimeField()


# == Usernotifications models

class UserNotification(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    metadata = models.JSONField()
    priority = models.CharField(max_length=20)



# == Agency  Models

class Agency(models.Model):
    name = models.CharField(max_length=255)
    legal_name = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=200)
    company_address = models.TextField()
    billing_address = models.TextField()
    website = models.URLField()
    logo = models.URLField()
    primary_color = models.CharField(max_length=20)
    secondary_color = models.CharField(max_length=20)
    billing_email = models.EmailField()
    support_email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    time_zone = models.CharField(max_length=50)
    currency = models.CharField(max_length=10)
    language = models.CharField(max_length=20)
    subscription_status = models.CharField(max_length=50)
    subscription_plan = models.CharField(max_length=50)
    trail_ends_at = models.DateTimeField()
    settings = models.JSONField()
    branding = models.JSONField()
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



# == Agencysubscription models

class AgencySubscription(models.Model):
    agency = models.ForeignKey(Agency,on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10 , decimal_places=2)
    billing_cycle = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=50)
    team_member_limit = models.IntegerField()
    client_limit = models.IntegerField()
    features =models.JSONField()
    payment_method = models.CharField(max_length=50)
    last_payment_date = models.DateTimeField()
    next_billing_date = models.DateTimeField()


# == AgentBilling models

class AgencyBilling(models.Model):
    agency = models.ForeignKey(Agency,on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10 ,decimal_places=2)
    status = models.CharField(max_length=50)
    due_date = models.DateTimeField()
    paid_date = models.DateTimeField()
    payment_method = models.CharField(max_length=50)
    line_items = models.JSONField()
    currency = models.CharField(max_length=20)
    is_paid = models.BooleanField(default=False)
    pdf_url = models.URLField()



# == Agencyteammember models

class AgencyTeamMember(models.Model):
    agency = models.ForeignKey(Agency,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    permissions = models.JSONField()
    joined_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField()
    invitation_status = models.CharField(max_length=80)
    department = models.CharField(max_length=100)
    hourly_rate = models.DecimalField(max_digits=10 , decimal_places=2)
    assigned_clients = models.JSONField()
    notification_preferences = models.JSONField()
    emergency_contact = models.CharField(max_length=255)