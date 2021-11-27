from django.urls import path

from . import views

urlpatterns = [
    path('', views.personALL, name='person'),
    path('<int:userid>/', views.detail, name='detail'),
]