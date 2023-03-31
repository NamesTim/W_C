from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='home'),
    path('auth/register',views.register,name='register'),
    path('auth/login',views.userlogin,name='login'),
    path('questions/<int:questionId>/',views.question,name='question'),
    path('questions',views.questions,name='questions'),
    path('questions/<int:questionId>/answers',views.answer,name='answers'),
    path('questions/<int:questionId>/answers/<int:answerId>',views.answers,name='answer')
]
