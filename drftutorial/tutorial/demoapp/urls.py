from django.urls import path
from demoapp import views


urlpatterns = [
    path('', views.demo_list),
    path('<int:pk>/', views.demo_detail),
]






