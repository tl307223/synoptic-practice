from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'QuizManager'
urlpatterns= [
    path('', views.index, name="index"),
    path('view_question/<int:id>/', views.view_question, name='view_question'),
    path('edit_question/<int:id>/', views.edit_question, name='edit_question'),
    path('delete_question/<int:id>/', views.delete_question, name='delete_question'),
    path('edit_choices/<int:id>/', views.edit_choices, name='edit_choices'),
    path('add_question/<str:quiz>/', views.add_question, name='add_question'),
    path('add_quiz', views.add_quiz, name='add_quiz'),
    path('view_quiz/<int:id>/', views.view_quiz, name='view_quiz'),
    path('view_quizzes', views.view_quizzes, name='view_quizzes'),
    path('edit_quiz/<int:id>/', views.edit_quiz, name='edit_quiz'),
    path('delete_quiz/<int:id>/', views.delete_quiz, name='delete_quiz'),
    path('take_quiz/<int:id>/', views.take_quiz, name='take_quiz'),
    path('view_assigned_quizzes', views.view_assigned_quizzes, name='view_assigned_quizzes'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('admin', admin.site.urls)
]