from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("menu", views.menu, name="menu"),
    path("contacto", views.contacto, name="contacto"),
    path("acerca",views.acerca,name="acerca"),
    path("login", views.login, name="login"),
    path("registrar", views.registrar, name="registrar")
]
