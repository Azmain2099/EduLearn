from rest_framework import serializers
from .models import Course, Lesson, Student

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'content', 'video_url']

class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'duration', 'thumbnail', 'lessons']

class StudentSerializer(serializers.ModelSerializer):
    enrolled_courses = CourseSerializer(many=True, read_only=True)
    
    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'enrolled_courses']