from django.shortcuts import render, HttpResponse
from .models import Organizers, Flower, User, Competition, Perennials, Annuals
from .Form import Insertflower, Insertuser, Insertcompetition
from .filters import thefilter

# Create your views here.
def home(request):
    return render(request,"home.html")

def search(request):
    u_info = User.objects.all()
    f_info = Flower.objects.all()

    the_filter = thefilter(request.GET, queryset=u_info)

    u_info = the_filter.qs

    context = {'users' : u_info, 
               'flowers' : f_info, 
               'filter' : the_filter}
    return render(request,"search.html",context)

def organizers(request):
    o_info = Organizers.objects.all()
    return render(request,"organizers.html", {'organizers' : o_info})

def changeview(request):
    form = Insertflower()

    if request.method == 'post':
        form = Insertflower(request.POST)
        if form.is_valid():
            form.save()
            return render
        
    form2 = Insertuser()
    form3 = Insertcompetition()
    context = {"Flowerform" : form,
                "Userform" : form2, 
                "Competitionform":form3}
    return render(request,"changeview.html",context)

def pflowers(request):
    return render(request,"pflowers.html")