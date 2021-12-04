from django.urls import include, path

urlpatterns = [
    path('', include('programadores.urls_api')),
]

