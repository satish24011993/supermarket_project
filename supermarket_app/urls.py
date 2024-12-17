from django.urls import path
from supermarket_app import views

urlpatterns = [
    path('/',views.ApiOverview, name='home'),
    path('/create/', views.add_item, name='create'),
]
