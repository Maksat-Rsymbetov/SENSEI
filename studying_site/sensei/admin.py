from django.contrib import admin
from .models import *
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
	list_display = ['name', 'author']
	list_display_links = ['name',]
	search_fields = ['name', 'author']
	list_filter = ['author',]

class LessonAdmin(admin.ModelAdmin):
	list_display = ['lesson_name', 'course']
	list_display_links = ['lesson_name',]
	search_fields = ['id', 'lesson_name']
	list_filter = ['lesson_name',]

class ReviewAdmin(admin.ModelAdmin):
	list_display = ['title', 'course', 'reviewer']
	list_display_links = ['title',]
	search_fields = ['title',]

class CommentAdmin(admin.ModelAdmin):
	list_display = ['id', 'comment', 'lesson', 'commentator']
	list_display_links = ['id',]
	search_fields = ['id', 'comment', 'lesson', 'commentator']

class ProfileAdmin(admin.ModelAdmin):
	list_display = ['id', 'user', 'avatar']
	list_display_links = ['id', 'user', 'avatar']
	search_fields = ['user', 'about']

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Profile, ProfileAdmin)