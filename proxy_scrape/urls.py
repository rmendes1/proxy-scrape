from proxy_scrape.views import *
from django.urls import path

urlpatterns = [ 
    path('', index, name = 'index'),
    path('add-item', add_item, name= "add-item"),
    path('<int:pk>/edit/', edit_item, name= "edit-item"),
    path('<int:pk>/delete/', delete_item, name= "delete-item"),
]