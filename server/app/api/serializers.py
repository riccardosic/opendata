from app.models import Gyms, Courses, Category
from rest_framework import serializers

class GymsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Gyms
        fields = '__all__'
        read_only_fields = ['id']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['id']

class CoursesSerializer(serializers.ModelSerializer):
    idGym = GymsSerializer(read_only=True)
    idCategory = CategorySerializer(read_only = True)
    
    class Meta:
        model = Courses
        fields = '__all__'
        read_only_fields = ['id']