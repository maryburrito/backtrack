from django.urls import path

from tracker.views import hello_world

urlpatterns = [
    path('', hello_world),
]