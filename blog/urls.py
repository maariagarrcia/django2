from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog, name="blog"),
    # <jnkj> ---> es una cadena de caracteres hayq ue convertirlo a entero
    path('category/<int:category_id>/', views.category, name='category')   
]
