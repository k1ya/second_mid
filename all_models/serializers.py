from rest_framework import serializers
from .models import *
#my serializers

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields='__all__'
        
class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=employee
        fields='__all__'

class teacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=teacher
        fields='__all__'