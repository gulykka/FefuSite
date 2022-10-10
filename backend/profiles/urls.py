from django.urls import path
from .views import *

urlpatterns = [
    path('buildings/', BuildingsList.as_view()),
    path('publications/', PublicationApi.as_view()),
    path('profiles/', ProfileApi.as_view()),
    path('categories/', CategoryApi.as_view()),
]
