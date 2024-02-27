from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='name')
    preview = models.ImageField(blank=True, null=True, verbose_name='preview')
    description = models.TextField(blank=True, null=True, verbose_name='description')
    price = models.PositiveIntegerField(default=100, verbose_name='price')
    owner = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='owner')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'


class Lesson(models.Model):
    name = models.CharField(max_length=50, verbose_name='name')
    description = models.TextField(blank=True, null=True, verbose_name='description')
    preview = models.ImageField(upload_to='materials/', blank=True, null=True, verbose_name='preview')
    video_link = models.URLField(blank=True, null=True, verbose_name='video_link')
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, verbose_name='course')
    price = models.PositiveIntegerField(default=100, verbose_name='price')
    owner = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='owner')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'
