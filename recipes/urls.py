from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),  # / , que é o home
    path('recipes/<int:id>/', views.recipe),
]
