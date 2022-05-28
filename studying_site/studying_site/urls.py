"""studying_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sensei.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CoursesView.as_view()),
    path('home/', CoursesView.as_view(), name='home'),
    path('users/', UsersView.as_view(), name='users'),
    path('course/<int:courseId>', LessonsView.as_view(), name='course'),
    path('reviews/<int:courseId>', ReviewsView.as_view(), name='reviews'),
    path('reviews/<int:courseId>/write_review/', WriteReview.as_view(), name='write_review'),
    path('lesson/<int:lessonId>', view_lesson, name='lesson'),
    path('register/', RegisterSensei.as_view(), name='register'),
    path('login/', LoginSensei.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('profile/<int:userId>', view_profile, name='profile'),
    path('create_course/', CreateCourse.as_view(), name='create_course'),
    path('course/<int:courseId>/create_lesson', CreateLesson.as_view(), name='create_lesson'),
    path('lesson/<int:lessonId>/attach_file', AttachFile.as_view(), name='attach'),
]
