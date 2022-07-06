from django.contrib import admin
from django.urls import path
from res.views import restuarant_details_view, restuarant_view, items_view,sub_items_view,rslist_delete_view,rslist_create_view

urlpatterns = [
    
    path('',restuarant_details_view, name= 'list'),
    path('res/<int:id>',restuarant_view , name='view'),
    path('res/items/<int:id>',items_view , name='item'),
    path('res/items/items/<int:id>',sub_items_view, name='subb'),


    path('res/<int:id>/delete',rslist_delete_view , name='view'),
    path('res/<int:id>/create',rslist_create_view, name='create'),
    

]