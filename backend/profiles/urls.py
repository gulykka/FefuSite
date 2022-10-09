from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryList.as_view()),
    path('profiles/', ProfileList.as_view()),
    path('publicationlist/', PublicationsList.as_view()),
]
