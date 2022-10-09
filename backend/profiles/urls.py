from django.urls import path
from .views import *

urlpatterns = [
    path('profiles/', ProfileApi.as_view()),
    path('publications/', PublicationApi.as_view()),
    path('buildings/', BuildingsApi.as_view()),
]
