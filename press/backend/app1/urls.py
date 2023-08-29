
from . import views
from django.urls import path

urlpatterns = [
     path('submit-feedback/', views.submit_feedback, name='submit_feedback'),

]
