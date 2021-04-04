from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.eventList),
    path('/detail/<int:pk>/', views.eventDetail),
    path('/create', views.eventCreate),
    path('/update/<int:pk>/', views.eventUpdate),
    path('/delete/<int:pk>/', views.eventDelete),
]
