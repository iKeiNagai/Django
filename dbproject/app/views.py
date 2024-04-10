from django.shortcuts import render, HttpResponse
from .models import Organizers, Flower, User, Competition, Perennials, Annuals
from .Form import Insertflower, Insertuser, Insertcompetition, randc
from .filters import thefilter, OrganizersFilter, CompetitionsFilter
import random

# Home view
def home(request):
    return render(request,"home.html") #render home url


def user(request):
    u_info = User.objects.all() #creates user queryset(qs) 
    f_info = Flower.objects.all() #creates flower qs

    the_filter = thefilter(request.GET, queryset=u_info) #filters user qs from GET request

    u_info = the_filter.qs #filtered qs from GET request

    context = {'users' : u_info, 
               'flowers' : f_info, 
               'filter' : the_filter} #key/value to return(dictionary)
    return render(request,"user.html",context)

def entries(request, entry):
    u_entry = Flower.objects.filter(u=entry) #returns qs 
    context = {'entries' : u_entry}
    return render(request, 'entries.html', context)

def organizers(request):
    o_info = Organizers.objects.all() #creates organizers qs
    o_filter = OrganizersFilter(request.GET, queryset=o_info)

    o_info = o_filter.qs
    context = {'organizers' : o_info,
               'filter' : o_filter} #key/value to return(dictionary)
    return render(request,"organizers.html",context)

def competitions(request):
    inserted = False

    c_info = Competition.objects.all()
    c_filter = CompetitionsFilter(request.GET, queryset=c_info)
    c_info = c_filter.qs
    #create form objects
        
    context = { 'filter': c_filter,
               'competitions' : c_info} #key/value to return(dictionary)
    return render(request,"competitions.html",context)

def insert(request):
    test = True
    form = Insertuser()

    if request.method == 'POST':
        form = Insertuser(request.POST) #data submitted(POST request)
        inserted = True
        if form.is_valid():
            form.save() #inserts to db if valid
    context = {'test' : test,
               'userform' : form}
    return render(request,'insert.html',context)

def pflowers(request):
    return render(request,"pflowers.html")

def randcomp(request) :
    form = randc()
    user_list = list(User.objects.all())
    list_len = len(user_list)

    rand_items = random.sample(user_list,0)
    if request.method == 'GET' :
        personNo = request.GET.get('PersonNo')
        if personNo is not None:
            rand_items = random.sample(user_list,int(personNo))
        name = request.GET.get('Name')
    context = {'comp' : user_list,
               'rand_items' : rand_items,
               'randc' : form,
               'len' : list_len,
               'compname' : name}
    return render(request, "randcomp.html", context)