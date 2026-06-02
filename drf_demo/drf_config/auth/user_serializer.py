from rest_framework import serializers
from . models import UserModel
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields='__all__'
    def validate_email(self,value):
        if UserModel.objects.filter(email=value).exists():
            return Response({
                "message":"Email already exists"
            })
        return value