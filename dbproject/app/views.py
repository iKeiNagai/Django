from django.shortcuts import render, HttpResponse
from .models import Organizers, Flower, User, Competition, Perennials, Annuals
from .Form import Insertflower, Insertuser, Insertcompetition
from .filters import thefilter

# Home view
def home(request):
    return render(request,"home.html") #render home url

#Search view
def user(request):
    u_info = User.objects.all() #creates user queryset(qs) 
    f_info = Flower.objects.all() #creates flower qs

    the_filter = thefilter(request.GET, queryset=u_info) #filters user qs from GET request

    u_info = the_filter.qs #filtered qs from GET request

    context = {'users' : u_info, 
               'flowers' : f_info, 
               'filter' : the_filter} #key/value to return(dictionary)
    return render(request,"search.html",context)

def organizers(request):
    o_info = Organizers.objects.all() #creates organizers qs
    context = {'organizers' : o_info} #key/value to return(dictionary)
    return render(request,"organizers.html",context)

def competitions(request):
    inserted = False

    #create form objects
    form = Insertflower() 
    form2 = Insertuser()
    form3 = Insertcompetition()

    if request.method == 'POST':
        form2 = Insertuser(request.POST) #data submitted(POST request)
        inserted = True
        if form2.is_valid():
            form2.save() #inserts to db if valid
        
    context = {"Flowerform" : form,
                "Userform" : form2, 
                "Competitionform":form3} #key/value to return(dictionary)
    return render(request,"changeview.html",context)

def pflowers(request):
    return render(request,"pflowers.html")