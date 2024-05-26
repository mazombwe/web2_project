from django.shortcuts import get_object_or_404, render
from flask import redirect
from .models import *
from .forms import *
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')


def menu(request):
    titre = "Menu Plat"
    plats = Plat.objects.all()
    paginate = Paginator(plats, 4)
    paginate_number = request.GET.get("page")
    pages = paginate.get_page(paginate_number)

    return render(request, 'pages/menu.html', {"plats":pages , 'titre' : titre})

def log_plat(plat):
    with open('medicaments.log', 'a+') as f:
        f.write(f"Nom: {plat.nom}\n")
        f.write(f"Description: {plat.description}\n")
        f.write(f"Prix: {plat.prix}\n")
        f.write("\n")



from django.http import HttpResponse
from django.shortcuts import redirect

def addPlat(request):
    if request.method == "POST":
        form = PlatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            log_plat(form.instance)
            return redirect('/menu')
    else:
        form = PlatForm()

    return HttpResponse(render(request, 'pages/addPlat.html', { "form": form }))


from django.shortcuts import get_object_or_404

def editPlat(request, platId):
    plat = get_object_or_404(Plat, id=platId)

    if request.method == "POST":
        form = PlatForm(request.POST, request.FILES, instance=plat)
        if form.is_valid():
            form.save()
            return redirect('/menu')
    else:
        form = PlatForm(instance=plat)

    return render(request, 'pages/editPlat.html', {'form': form})

def delPlat(request, platId):

    plat = get_object_or_404(Plat, id=platId)
    
    if request.method == "POST":
        plat.delete()
        return redirect('/')
    
    return render(request, 'pages/delPlat.html', {'plat': plat})




def contact(request):
    return render(request, 'pages/contact.html')



def about(request):
    return render(request, 'pages/about.html')

def user_profile(request):
    return render(request, 'registration/profile.html')
