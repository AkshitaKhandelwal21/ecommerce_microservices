from rest_framework import serializers
 
from auths.models import Users

class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'email', 'phone', 'password', 'confirm_password']
    
    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Password fields don't match")
        return data
        
    def create(self, valid_data):
        if valid_data:
            valid_data.pop('confirm_password')
            user = Users.objects.create_user(valid_data.email, valid_data.password)
            return user
