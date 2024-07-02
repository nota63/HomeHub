# homeHub/feedback/urls.py

from django.urls import path
from .views import feedback, feedback_success

urlpatterns = [
    path('', feedback, name='feedback'),
    path('feedback/success/', feedback_success, name='feedback_success'),
]
