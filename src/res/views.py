
from django.shortcuts import render,get_object_or_404,redirect
from .models import Rslist, Cuision, Menulist
from .forms import RslistForm,CuisionForm,MenulistForm
# Create your views here.

def restuarant_details_view(request):
    restuarnt = Rslist.objects.all()
    
    context = {
        'retaurants' :restuarnt, #queryset #obj1
        
    }
    return render(request, "rslist/rslist_list.html", context)

def restuarant_view(request,id):
    restuarant= Rslist.objects.get(id=id)
    cuision_name= restuarant.cuision.all()
    res_name = restuarant.sub.all()
    context = {
        'retaurants' : restuarant, #obj2
        'cuision_names' : cuision_name ,#obj
        'menu_name' : res_name #obj3
    }
    return render(request, "rslist/rslist_view.html",context)

def items_view(request,id):
    menu_res= Menulist.objects.get(id=id)
    # queryset2 =  queryset.cuision.all()
    context = {
        'item_name' : menu_res
        # 'obj' : queryset2
    }
    return render(request, "rslist/item_view.html",context)






def rslist_delete_view(request,id):
    rs = get_object_or_404(Rslist, id=id)
    # POST request  
    if request.method == "POST":                            
        rs.delete() #conforming delete 
        return redirect('../../')
    context={
        'restaurant': rs
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

def rslist_update_view (request,id=id):
    form = RslistForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = RslistForm()
    

    context={
        'form':form
    }
    return render(request, "rslist/rslist_update.html",context)

def cuision_create_view(request,id=id):
    form = CuisionForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CuisionForm()
    

    context={
        'form':form
    }
    return render(request, "cuision/cuision_create.html",context)

def menulist_create_view(request,id=id):
    form = MenulistForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = MenulistForm()
    

    context={
        'form':form
    }
    return render(request, "menulist/menulist_create.html",context)

def menulist_delete_view(request,id):
    mn = get_object_or_404(Menulist,id=id)
    # POST request  
    if request.method == "POST":                            
        mn.delete() #conforming delete 
        return redirect('../../')
    context={
        'menuitem': mn
    }
    return render(request, "menulist/menulist_delete.html",context)