from rest_framework import serializers
from .models import  User, UserProfile, UserNotification, Agency, AgencySubscription, AgencyBilling, AgencyTeamMember


# == User Serializer ==

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','username','is_active','is_staff','is_superuser','last_login','date_joined']

# == User Registration Serializer == 

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True , min_length=8)
    
    class Meta:
        model = User
        fields = ['email','username','password']

    def validate_password(self,value):
        if len(value)< 8:
            raise serializers.ValidationError("Password must be at least 8 characters long. ")

        return value
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    


# == UserProfile Serializer == 

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ['user','first_name','last_name','phone_number','profile_picture','time_zone','preferences','language','email_verified','phone_verified','last_password_change']

    def update(self,instance,validated_data):
        user_data = validated_data.pop('user',None)
        if user_data:
            for key, value  in user_data.items():
                setattr(instance.user,key, value)
                instance.user.save()
        return super().update(instance,validated_data)


# == UserNotificationSeru=ializer == 

class UserNotificationSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserNotification
        fields = ['user','type','message','is_read','created_at','metadata','priority']


# == Agency Models == 

class AgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Agency
        fields = '__all__'

# == Agencysubscription Serialzier == 

class AgencySubscriptionSerializer(serializers.ModelSerializer):
    agency = AgencySerializer()

    class Meta:
        model = AgencySubscription
        fields = '__all__'


#== AgencyBillingSerilaizer == 

class AgencyBillingSerilaizer(serializers.ModelSerializer):
    agency = AgencySerializer()

    class Meta:
        model = AgencyBilling
        fields = '__all__'

    
#== AgencyTeamMemberSerialzier == 

class AgencyTeamMemberSerializer(serializers.ModelSerializer):

    agency = AgencySerializer()
    user = UserSerializer()

    class Meta:
        model = AgencyTeamMember
        fields = '__all__'