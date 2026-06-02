from django.db.models import Model
from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate_name(self, value):
        data=Student.objects.filter(name=value)
        if data.exists():
            raise serializers.ValidationError('Student with this name already exists')
        return value
    def validate_phone(self, value):
        if not str(value).startswith("91"):
            raise serializers.ValidationError('start phone number is  91')

        data=Student.objects.filter(phone=value)
        if data.exists():
            raise serializers.ValidationError('Student with this phone already exists')
        return value



