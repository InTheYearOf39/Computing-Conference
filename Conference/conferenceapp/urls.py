from django.urls import path
from  . import views

app_name = "conferenceapp"

urlpatterns = [
    path('',views.home, name="home"),
]