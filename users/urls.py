from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('connexion/', views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
]