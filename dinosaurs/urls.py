from django.urls import path
from dinosaurs import views


urlpatterns = [
    path("", views.home, name="home")
]
