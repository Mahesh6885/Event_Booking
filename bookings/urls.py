from django.urls import path
from .views import UserBookingView,createBookingView

urlpatterns=[
    path("create/",createBookingView.as_view()),
    path("my/",UserBookingView.as_view()),
]