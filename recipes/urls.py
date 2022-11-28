from django.urls import path

from recipes.views import contato, home, sobre

urlpatterns = [
    path('', home),  # / , que é o home
    path('sobre/', sobre),  # /sobre/
    path('contato/', contato)  # /contato/
]
