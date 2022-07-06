from django.urls import path
from .views import (
    RslistCreateView,
    RslistDeleteView,
    # RslistDetailView,
    RslistListView,
    RslistUpdateView,
    MenuDetailView
    
  
)


app_name = 'rslist' #you can slove rslist reverse
# app_name2 = "menulist"
urlpatterns = [
    path('', RslistListView.as_view(), name='rslist-list'),
    path('create/', RslistCreateView.as_view(), name='rslist-create'),
    # path('<int:id>/', RslistDetailView.as_view(), name='rslist-detail'),
    path('<int:id>/', MenuDetailView.as_view(), name='rslist-detail'),
    path('<int:id>/update/', RslistUpdateView.as_view(), name='rslist-update'),
    path('<int:id>/delete/', RslistDeleteView.as_view(), name='rslist-delete'),
]