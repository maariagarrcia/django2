from django.urls import path
from . import views

urlpatterns = [
    # paths del views
    path('<int:page_id>/<slug:page_slug>/',views.page,name="page"),
]

