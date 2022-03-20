from django.urls import path

from aircraft.views import get

urlpatterns = [
    path('v1/<str:code>/', get, name='index'),
]