from rest_framework import serializers
from .models import Course, Department, University

class CourseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
    

# class CourseModelSerializer(serializers.Serializer):
#     def create(self, validated_data):
#         return Course.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.credit = validated_data.get('credit', instance.credit)
#         instance.department = validated_data.get('department', instance.department)
#         instance.university = validated_data.get('university', instance.university)
#         instance.year = validated_data.get('year', instance.year)
#         instance.semester = validated_data.get('semester', instance.semester)
#         instance.syllabus = validated_data.get('syllabus', instance.syllabus)
#         instance.save()
#         return instance