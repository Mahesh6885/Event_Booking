from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("Auth/",include('accounts.urls')),
    path("bookings/",include("bookings.urls")),
    path("events",include("events.urls")),
    path("payments",include("payments.urls")),
]
