from django.contrib import admin
from django.urls import path
from res.views import restuarant_details_view, restuarant_view, items_view,rslist_delete_view,rslist_create_view,rslist_update_view,cuision_create_view,menulist_create_view,menulist_delete_view
#sub_items_view,
urlpatterns = [
    
    path('',restuarant_details_view, name= 'list'),
    path('res/<int:id>',restuarant_view , name='view'),
    path('res/items/<int:id>',items_view , name='item'),
    # path('res/items/items/<int:id>',sub_items_view, name='subb'),





    path('res/<int:id>/delete',rslist_delete_view , name='delete'),
    path('res/<int:id>/update',rslist_update_view , name='update'),
    path('create/',rslist_create_view, name='create'),


    path('add/',menulist_create_view, name='menu-create'),
    path('res/items/<int:id>/update',menulist_create_view, name='menu-update'),
    path('delete/',menulist_delete_view, name='menu-delete'),



    path('cui_add/',cuision_create_view, name='cui_create'),
    
    

]