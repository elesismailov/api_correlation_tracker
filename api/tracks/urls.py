from django.urls import path, include
from .views import Index, Entry

urlpatterns = [
    path('', Index.as_view()),
    path('entry/', Entry.as_view()),
]
