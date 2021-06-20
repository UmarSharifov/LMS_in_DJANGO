from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('profile_change/', views.profile_change, name='profile_change'),
    path('about/', views.about, name='about'),
    path('courses/',views.courses, name='courses'),
    path('course_create/', views.course_create, name='course_create'),
    path('course_detail/<int:course_id>/', views.course_detail, name='course_detail'),
    path('addTextInCourse/<int:course_id>/<int:section_id>/', views.addTextInCourse, name='addTextInCourse'),
    path('addVideoInCourse/<int:course_id>/<int:section_id>/', views.addVideoInCourse, name='addVideoInCourse'),
    path('addQuizInCourse/<int:course_id>/<int:section_id>/', views.addQuizInCourse, name='addQuizInCourse'),
    path('course_element_learning/<int:course_id>/<int:element_id>', views.course_element_learning, name='course_element_learning'),
    path('course_confirm/<int:course_id>/', views.course_confirm, name='course_confirm'),
]