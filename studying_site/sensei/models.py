from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.ImageField(upload_to = "avatars/%Y/%m/%d")
	about = models.TextField(blank=True)
	deleted = models.BooleanField(default=False)
	subscribed_courses = models.ManyToManyField('Course')

class Course(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(blank=True)
	author = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

class Lesson(models.Model):
	lesson_name = models.CharField(max_length=255)
	content = models.TextField(blank=True)
	course = models.ForeignKey('Course', on_delete=models.CASCADE)

class Review(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField(blank=True)
	course = models.ForeignKey('Course', on_delete=models.CASCADE)
	reviewer = models.ForeignKey(User, on_delete=models.CASCADE)

class LessonFile(models.Model):
	lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)
	file = models.FileField(upload_to="files/%Y/%m/%d")
	comment = models.TextField(blank=True)

class Comment(models.Model):
	comment = models.TextField()
	lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)
	commentator = models.ForeignKey(User, on_delete=models.CASCADE)