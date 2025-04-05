from . import views
from django.urls import path


urlpatterns = [
    path("",views.home, name="home"),
    path("manele",views.manele, name="manele"),
    path("rap",views.rap, name="rap"),
    path("trap",views.trap, name="trap"),
    path("rock",views.rock, name="rock"),
    path("pop",views.pop, name="pop"),
    path("jaz",views.jaz, name="jaz"),
]
