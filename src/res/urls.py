from django.contrib import admin
from django.urls import path
from res.views import ( 
    restuarant_details_view, 
    restuarant_view, 
    items_view,

    rslist_delete_view,
    rslist_create_view,
    rslist_update_view,

    menulist_create_view,
    menulist_delete_view,
    menulist_update_view,
   
    cuision_all,
    cuision_update_view,
    cuision_create_view,
    cuision_delete_view,
)

urlpatterns = [
    
   path('admin/', admin.site.urls),
    path('<int:id>/',rslist_update_view, name='res_update'),
    path('<int:id>/delete/',rslist_delete_view, name='res_delete'),
    path('add/',rslist_create_view, name='res_create'),
    
   
    path('',restuarant_details_view, name= 'list'),
    path('restuarant/<int:id>/',restuarant_view , name='view'),
    path('restuarant/items/<int:id>/',items_view , name='item'),

    path('restuarant/<int:res_id>/<int:menu_id>/update/',menulist_update_view, name='item_update' ),
    path('restuarant/<int:res_id>/<int:menu_id>/delete/', menulist_delete_view, name='item_delete' ),
    path('restuarant/<int:res_id>/create/', menulist_create_view, name='item_create' ),

    path('restuarant/<int:res_id>/<int:cuis_id>/cuisines/', cuision_all, name='cuis_view' ),
    path('restuarant/<int:res_id>/<int:cuis_id>/cuisines/delete/', cuision_delete_view, name='cuis_delete' ),
    path('add/cuisines',cuision_create_view, name='cuis_create'),
    path('<int:cui_id>/edit/cuisines',cuision_update_view, name='cuis_create'),

    

]