from django.urls import path, include
from .views import Index, Entry, TrackView

urlpatterns = [
    path('', Index.as_view()),
    path('<track_id>/', TrackView.as_view()),
    path('<track_id>/entry/', Entry.as_view()),
]
