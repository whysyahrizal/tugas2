from django.urls import path
from study_tracker.views import show_tracker

app_name = 'study_tracker'

urlpatterns = [
    path('', show_tracker, name='show_tracker'),
]
