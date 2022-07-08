
from django.shortcuts import render,get_object_or_404,redirect
from .models import Rslist, Cuision, Menulist
from .forms import RslistForm,CuisionForm,MenulistForm
# Create your views here.

def restuarant_details_view(request):
    restuarant = Rslist.objects.all()
    menuli = Menulist.objects.all()
    cuisines= Cuision.objects.all()
    context = {
        'restuarant' : restuarant, #queryset #obj1
        "cuision" :cuisines,
        "menu" : menuli,
        
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
    
    context = {
        'item_name' : menu_res
       
    }
    return render(request, "rslist/item_view.html",context)



def rslist_delete_view(request,id):
    rs = get_object_or_404(Rslist, id=id)
    if request.method == "POST":                            
        rs.delete() 
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
    obj = get_object_or_404(Rslist, id=id)
    form = RslistForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        form = RslistForm()
    

    context={
        'form':form
    }
    return render(request, "rslist/rslist_update.html",context)



def menulist_create_view(request,res_id):
    form = MenulistForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = MenulistForm()
    

    context={
        'form':form,
        
    }
    return render(request, "menulist/menulist_create.html",context)

def menulist_delete_view(request,res_id,menu_id):
    restuarant = Rslist.objects.get(id=res_id)
    res_name = get_object_or_404(Menulist, id=menu_id)
    if request.method == "POST":
        res_name.delete()
        return redirect('../../')
       
    context = {
        "menu_name" : res_name,
        "restuarant":restuarant
    }
    return render(request, "menulist/menulist_delete.html", context)


def menulist_update_view(request,res_id, menu_id):
    restuarant = Rslist.objects.get(id=res_id)
    res_name = get_object_or_404(Menulist, id=menu_id)
    form =  MenulistForm(request.POST or None, instance=res_name)
    if form.is_valid():
        form.save()
        return redirect('../../')
        
    context = {
        'form' : form,
        "restuarant":restuarant,
    }
    return render(request, "menulist/menulist_update.html", context)
    
def cuision_all(request, res_id, cuis_id):
    restuarant = Rslist.objects.get(id=res_id)
    menu_items= restuarant.sub.all()
    cuisine = Cuision.objects.get(id=cuis_id)
    items = menu_items.filter(cuision_type=cuisine)
    context = {
        'cuisine' : cuisine, 
        'items' : items,
        'restuarant':restuarant
    }
    return render(request, "cuision/cuision_all.html", context)


def cuision_delete_view(request, res_id, cuis_id):
    restuarant = Rslist.objects.get(id=res_id)
    cuisine = get_object_or_404(Cuision, id=cuis_id)
    if request.method == "POST":
        cuisine.delete()
        return redirect('../../../')
        # return HttpResponseRedirect('')
    context = {
        "cuisine" : cuisine, 
        "restuarant" : restuarant
    }
    return render(request, "cuision/cuision_delete.html", context)

def cuision_create_view(request):
    form =  CuisionForm(request.POST or None)
    if form.is_valid():
        form.save()
        # form = CuisForm()
        return redirect('../../')
    context = {
        'form' : form
    }
    return render(request, "cuision/cuision_create.html", context)

def cuision_update_view(request,cui_id):
   
    res_name = get_object_or_404(Cuision, id=cui_id) #obj=
    form =  CuisionForm(request.POST or None,instance=res_name)
    if form.is_valid():
        form.save()
        
        return redirect('../../')
    context = {
        'form' : form,
        
    }
    return render(request, "cuision/cuision_update.html", context)

