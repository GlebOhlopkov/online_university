from rest_framework import serializers


def validator_lesson_url(value):
    if value.find('youtube.com') == -1:
        raise serializers.ValidationError(
            'You use wrong URL for lesson-link (Your lesson must be upload on youtube.com)')
