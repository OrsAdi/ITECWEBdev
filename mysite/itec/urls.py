from . import views
from django.urls import path


urlpatterns = [
    path("",views.home, name="home"),
    path("manele",views.manele, name="manele"),
]
