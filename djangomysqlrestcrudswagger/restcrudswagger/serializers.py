from rest_framework import serializers
from restcrudswagger.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'phone', 'address']        
        extra_kwargs = {'id': {'required': False}}