from tracemalloc import get_object_traceback
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
import requests

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView,
   
)

from .forms import RslistModelForm
from .models import Rslist,Menulist



class RslistCreateView(CreateView):
    template_name = 'rslist/rslist_create.html'
    form_class = RslistModelForm
    queryset = Rslist.objects.all() # <blog>/<modelname>_list.html
    # success_url = '/' another method for...

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # def get_success_url(self):
    #    return '/'

class RslistListView(ListView):
    template_name = 'rslist/rslist_list.html'
    queryset = Rslist.objects.all() # <res>/<modelname>_list.html



class MenuDetailView(DetailView):
    # template_name = 'rslist/rslist_detail.html'
    template_name = 'menulist/menulist_list.html'
    # queryset = Menulist.objects.all()

    # queryset = Rslist.objects.all()
    # queryset = Menulist.objects.all() # <blog>/<modelname>_list.html
    # success_url = 'cuision/cuision_list.html' 

    def get_object(self):
        id_ = self.kwargs.get("id") 
        return get_object_or_404(Menulist,id=id_)
        
    
   
    
       
       
        



    
    
        


class RslistUpdateView(UpdateView):
    template_name = 'rslist/rslist_create.html'
    form_class = RslistModelForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Rslist, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class RslistDeleteView(DeleteView):
    template_name = 'rslist/rslist_delete.html'
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Rslist, id=id_)

    def get_success_url(self):
        return reverse('rslist:rslist-list')








