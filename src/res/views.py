
from django.shortcuts import render,get_object_or_404,redirect
from .models import Rslist, Cuision, Menulist
from .forms import RslistForm
# Create your views here.

def restuarant_details_view(request):
    queryset = Rslist.objects.all()
    context = {
        'obj' : queryset
    }
    return render(request, "rslist/rslist_list.html", context)

def restuarant_view(request,id):
    queryset= Rslist.objects.get(id=id)
    queryset2= queryset.cuision.all()
    context = {
        'obj2' : queryset,
        'obj' : queryset2
    }
    return render(request, "rslist/rslist_view.html",context)

def items_view(request,id):
    queryset = Cuision.objects.get(id=id)
    queryset2 =  queryset.cuision.all()
    context = {
        'title' : queryset,
        'obj' : queryset2
    }
    return render(request, "rslist/item_view.html",context)

def sub_items_view(request,id):
    queryset = Menulist.objects.get(id=id)
    # queryset2= queryset.menulist.all()
    context = {
        'title' : queryset,
        # 'obj' : queryset2
    }
    return render(request, "menulist/sub_item_list.html",context)


def rslist_delete_view(request,id):
    obj = get_object_or_404(Rslist, id=id)
    # POST request  
    if request.method == "POST":                            
        obj.delete() #conforming delete 
        return redirect('../../')
    context={
        'object': obj
    }

    return render(request, "rslist/rslist_delete.html",context)

def rslist_create_view(request,id=id):
    form = RslistForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = RslistForm()
    

    context={
        'form':form
    }
    return render(request, "rslist/rslist_create.html",context)