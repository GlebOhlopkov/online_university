from rest_framework import serializers

from materials.models import Course, Lesson
from materials.validators import validator_lesson_url
from users.models import Subscription


class LessonSerializer(serializers.ModelSerializer):
    video_link = serializers.URLField(validators=[validator_lesson_url])

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set.all', many=True, read_only=True)
    subscription = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['name', 'description', 'lessons_count', 'lessons', 'subscription']

    def get_lessons_count(self, course):
        return Lesson.objects.filter(course=course.id).count()

    def get_subscription(self, course):
        subscription = Subscription.objects.filter(
            course=course,
            user=self.context.get('request').user
        ).all()
        if subscription:
            return True
        else:
            return False
