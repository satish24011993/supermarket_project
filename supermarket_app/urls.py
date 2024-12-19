from django.urls import path
from supermarket_app import views

urlpatterns = [
    path('/',views.ApiOverview, name='home'),
    path('/create/', views.add_item, name='create'),
    path('/list/',views.all_items,name='all_items'),
    path('/update/<int:id>',views.update, name='update'),
    path('/item/delete/<int:id>', views.delete, name='delete')
]
