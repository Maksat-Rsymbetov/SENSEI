from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout as log_out
from .models import *
from .forms import *
# Create your views here.

# See all Courses______________________________________________________
class CoursesView(LoginRequiredMixin, ListView):
	model = Course
	template_name = 'sensei/home.html'
	context_object_name = 'course_list'
	login_url = reverse_lazy('login')

	def get_queryset(self):
		return Course.objects.all()

#See all Users_________________________________________________________
class UsersView(ListView):
	model = Profile
	template_name = 'sensei/senseis.html'
	context_object_name = 'profile_list'

	def get_queryset(self):
		return Profile.objects.all()

#See all lessons of chosen course_______________________________________
class LessonsView(ListView):
	model = Lesson
	template_name = 'sensei/course.html'

	def get_context_data(self, *, object_list=None, **kwargs):
		courseID = self.kwargs['courseId']
		ct = super().get_context_data(**kwargs)
		dt = {
		'courseId': courseID,
		'cc': Course.objects.get(pk = courseID),
		}
		return dict(list(ct.items()) + list(dt.items()))

	def get_queryset(self):
		return Lesson.objects.filter(course_id = self.kwargs['courseId'])

# See all Reviews of chosen course______________________________________
class ReviewsView(ListView):
	model = Review
	template_name = 'sensei/reviews.html'

	def get_context_data(self, *, object_list=None, **kwargs):
		ct = super().get_context_data(**kwargs)
		dt = {'courseId': self.kwargs['courseId']}
		return dict(list(ct.items()) + list(dt.items()))	

	def get_queryset(self):
		return Review.objects.filter(course_id = self.kwargs['courseId'])

# See chosen lesson______________________________________________________
def view_lesson(request, lessonId):
	lesson = Lesson.objects.get(pk = lessonId)
	comments = Comment.objects.filter(lesson_id = lessonId)
	attachments = LessonFile.objects.filter(lesson_id = lessonId)

	context = {
		'lesson': lesson,
		'comments': comments,
		'attachments': attachments,
		'lessonId': lessonId,
	}
	return render(request, 'sensei/lesson.html', context)

# See a profile of chosen user____________________________________________
def view_profile(request, userId):
	user1 = User.objects.get(pk = userId)
	profile = Profile.objects.get(user = user1)

	context = {
		'u': user1,
		'p': profile,
	}
	return render(request, 'sensei/profile.html', context)
#________________________________________________________________

# Register and login
class RegisterSensei(CreateView):
	form_class = SenseiCreationForm
	template_name = 'sensei/register.html'
	success_url = reverse_lazy('login')

	def form_valid(self, form):
		user1 = form.save()
		login(self.request, user1)
		Profile.objects.create(user=user1)
		return redirect('home')

class LoginSensei(LoginView):
	form_class = AuthenticationForm
	template_name = 'sensei/login.html'

	def get_success_url(self):
		return reverse_lazy('home')

def logout(request):
	log_out(request)
	return redirect('login')

# Creating courses______________________________________________________________
class CreateCourse(LoginRequiredMixin, CreateView):
	form_class = CourseCreationForm
	template_name = 'sensei/createcourse.html'
	login_url = reverse_lazy('login')

	def form_valid(self, form):
		query = form.cleaned_data
		user1 = self.request.user
		course = Course(name=query.get('name'), description=query.get('description'), author=user1)
		course.save()
		return redirect('home')

# Adding Lessons to Courses_____________________________________________________
class CreateLesson(LoginRequiredMixin, CreateView):
	form_class = LessonCreationForm
	template_name = 'sensei/createlesson.html'
	login_url = reverse_lazy('login')

	def form_valid(self, form):
		key = self.kwargs['courseId']
		query = form.cleaned_data
		course1 = Course.objects.get(pk = key)
		lesson = Lesson(lesson_name=query.get('lesson_name'), content=query.get('content'), course=course1)
		lesson.save()
		return redirect('course', key)

# Attaching files to lessons________________________________________________________
class AttachFile(LoginRequiredMixin, CreateView):
	form_class = AttachmentForm
	template_name = 'sensei/attach.html'
	login_url = reverse_lazy('login')

	def form_valid(self, form):
		key = self.kwargs['lessonId']
		ls = Lesson.objects.get(pk = key)
		q = form.cleaned_data
		lf = LessonFile(lesson=ls, comment=q.get('comment'), file = q.get('file'))
		lf.save()
		return redirect('lesson', key)

# Writing reviews____________________________________________________________________
class WriteReview(LoginRequiredMixin, CreateView):
	form_class = ReviewForm
	template_name = 'sensei/write_review.html'
	login_url = reverse_lazy('login')

	def form_valid(self, form):
		q = form.cleaned_data
		course_key = self.kwargs['courseId']
		user1 = self.request.user
		course1 = Course.objects.get(pk = course_key)
		review = Review(title=q.get('title'), content=q.get('content'), course=course1, reviewer=user1)
		review.save()
		return redirect('reviews', course_key)