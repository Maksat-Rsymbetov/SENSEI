from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *

# Create User____________________________________________________________________
class SenseiCreationForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)
	username = forms.CharField(max_length=100)

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'password1', 'password2']

	def clean_username(self):
		name = self.cleaned_data['username']
		if len(name) > 50: 
			raise ValidationError('Username should not contain more than 50 symbols')
		return name

	def clean_first_name(self):
		name = self.cleaned_data['first_name']
		if len(name) > 50: 
			raise ValidationError('Username should not contain more than 50 symbols')
		return name

	def clean_last_name(self):
		name = self.cleaned_data['last_name']
		if len(name) > 50: 
			raise ValidationError('Username should not contain more than 50 symbols')
		return name

# Course Creation Form__________________________________________________________________
class CourseCreationForm(forms.ModelForm):
	name = forms.CharField(max_length=255)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	class Meta:
		model = Course
		fields = ['name', 'description']

		widgets = {
			'name': forms.TextInput(),
			'description': forms.Textarea(attrs={'cols':60, 'rows':10})
		}

#Lesson creation form____________________________________________________________________
class LessonCreationForm(forms.ModelForm):
	lesson_name = forms.CharField(max_length=255)
	content = forms.CharField()

	class Meta:
		model = Lesson
		fields = ['lesson_name', 'content']
		widgets = {
			'lesson_name': forms.TextInput(),
			'content': forms.Textarea(attrs={'cols':60, 'rows':10})
		}

#Uploading files________________________________________________________________________
class AttachmentForm(forms.ModelForm):
	file = forms.FileField()
	comment = forms.CharField(required=False)

	class Meta:
		model = LessonFile
		fields = ['file', 'comment']
		widgets = {
			'comment': forms.Textarea(attrs={'cols':60, 'rows':10})
		}

# Writing a review for the course______________________________________________________
class ReviewForm(forms.ModelForm):
	title = forms.CharField(max_length=255)
	# content = forms.CharField()

	class Meta:
		model = Review
		fields = ['title', 'content']
		widgets = {
			'title': forms.TextInput(),
			'content': forms.Textarea(attrs={'cols':60, 'rows':10}),
		}