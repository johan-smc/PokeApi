from django.urls import path, include

urlpatterns = [
    path('pokemon/', include('business.pokemon.urls')),
]
