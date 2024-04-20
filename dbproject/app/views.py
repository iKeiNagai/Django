from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Organizers, Flower, User, Competition, Perennials, Annuals
from .Form import Insertflower, Insertuser, Insertcompetition, randc, InsertOrganizer
from .filters import entriesFilter, thefilter, OrganizersFilter, CompetitionsFilter, annualsFilter, perennialFilter
from fuzzywuzzy import fuzz
import random

# Home view
def home(request):
    # Query the database to find the three largest and three smallest plants based on size
    largest_plants = Flower.objects.exclude(size=None).order_by('-size')[:3]
    smallest_plants = Flower.objects.exclude(size=None).order_by('size')[:3]

    context = { 
        'largest_plants': largest_plants,
        'smallest_plants': smallest_plants
    }
    return render(request, "home.html", context=context)


def user(request):
    user_count = User.objects.count()
    entry_count = Flower.objects.count()
    u_info = User.objects.all() #creates user queryset(qs) 
    f_info = Flower.objects.all() #creates flower qs

    the_filter = thefilter(request.GET, queryset=u_info) #filters user qs from GET request

    u_info = the_filter.qs #filtered qs from GET request

    context = {
            'entry_count': entry_count,
             'user_count': user_count,
                'users' : u_info, 
               'flowers' : f_info, 
               'filter' : the_filter} #key/value to return(dictionary)
    return render(request,"user.html",context)

def entries(request, entry):
    u_entry = Flower.objects.filter(u=entry) #returns qs 
    print(entry)
    f_filter = entriesFilter(request.GET, queryset=u_entry)
    u_entry = f_filter.qs
    context = {'entries' : u_entry,
               'filter' : f_filter,
               'entry' : entry}
    return render(request, 'entries.html', context)

def subclass(request, pora, id=None):

    p_info = Perennials.objects.filter(comp=id)
    a_info = Annuals.objects.filter(comp=id)

    if pora == "perennial":
        the_filter = perennialFilter(request.GET, queryset=p_info)
        p_info = the_filter.qs

    if pora == "annual":
        the_filter = annualsFilter(request.GET, queryset=a_info)
        a_info = the_filter.qs

    context={'perennials': p_info,
             'annuals' : a_info,
             'perorann' : pora,
             'filter' : the_filter}
    return render(request, "subclass.html", context)

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

def user_forms(request, what, page, entry=None):
    u_form = Insertuser()
    o_form = InsertOrganizer()
    c_form = Insertcompetition()
    f_form = Insertflower()

    #User insert&update forms
    while page == "User":
        if what == "insert" :
            if request.method == 'POST':
                u_form = Insertuser(request.POST) #data submitted(POST request)
                if u_form.is_valid():
                    u_form.save() #inserts to db if valid
                    return redirect('user')
        elif what == "update":
            user = get_object_or_404(User, pk=entry)
            if request.method == 'POST':
                u_form = Insertuser(request.POST, instance=user)
                if u_form.is_valid():
                    u_form.save()
                return redirect('user')
            else:
                u_form = Insertuser(instance=user)
        elif what == "remove":
            print("remove")
        break

    #Organizer insert&delete forms
    while page == "Organizer":
        if what == "insert" :
            if request.method == 'POST':
                o_form = InsertOrganizer(request.POST) #data submitted(POST request)
                if o_form.is_valid():
                    o_form.save() #inserts to db if valid
                    return redirect('organizers')
        elif what == "update":
            organizer = get_object_or_404(Organizers, pk=entry)
            if request.method == 'POST':
                o_form = InsertOrganizer(request.POST, instance=organizer)
                if o_form.is_valid():
                    o_form.save()
                return redirect('organizers')
            else:
                o_form = InsertOrganizer(instance=organizer)
        elif what == "remove":
            print("remove")
        break

    #Competition insert&update forms
    while page == "Competition":
        if what == "insert" :
            if request.method == 'POST':
                c_form = Insertcompetition(request.POST) #data submitted(POST request)
                if c_form.is_valid():
                    c_form.save() #inserts to db if valid
                    return redirect('competitions')
        elif what == "update":
            competition = get_object_or_404(Competition, pk=entry)
            if request.method == 'POST':
                c_form = Insertcompetition(request.POST, instance=competition)
                if c_form.is_valid():
                    c_form.save()
                return redirect('competitions')
            else:
                c_form = Insertcompetition(instance=competition)
        elif what == "remove":
            print("remove")
        break

    #entries insert&update formss
    while page == "usentry":
        if what == "insert" :
            f_entry= get_object_or_404(Flower, pk=entry)
            if request.method == 'POST':
                f_form = Insertflower(request.POST) #data submitted(POST request)
                if f_form.is_valid():
                    f_form.save() #inserts to db if valid
                    return redirect(reverse('entries', kwargs={'entry' : entry}))
        elif what == "update":
            f_entry= get_object_or_404(Flower, pk=entry)
            if request.method == 'POST':
                f_form = Insertflower(request.POST, instance=f_entry)
                if f_form.is_valid():
                    f_form.save()
                return redirect('user')  # Redirect to the entries page after updating
            else:
                f_form = Insertflower(instance=f_entry)
        elif what == "remove":
            print("remove")
        break
    
    context = {'userform' : u_form,
               'organizerform' : o_form,
               'competitionform' : c_form,
               'flowerform' : f_form,
               'what': what,
               'page':page}
    return render(request,'insert.html',context)

def randcomp(request) :
    form = randc()
    user_list = list(User.objects.all())
    list_len = len(user_list)
    top_three = [None, None, None]

    rand_items = random.sample(user_list,0)
    if request.method == 'GET' :
        personNo = request.GET.get('PersonNo')
        if personNo is not None:
            rand_items = random.sample(user_list,int(personNo))

            for item in rand_items:
                for i in range(len(top_three)):
                    if top_three[i] is None or item.entriesno>top_three[i].entriesno:
                        top_three.insert(i, item)
                        top_three.pop()
                        break

        name = request.GET.get('Name')
    context = {'comp' : user_list,
               'rand_items' : rand_items,
               'randc' : form,
               'len' : list_len,
               'compname' : name,
               'winners' : top_three}
    return render(request, "randcomp.html", context)

def delete_object(request, obj_type, obj_id):
    if obj_type == 'user':
        obj = get_object_or_404(User, pk=obj_id)
    elif obj_type == 'organizers':
        obj = get_object_or_404(Organizers, pk=obj_id)
    elif obj_type == 'competition':
        obj = get_object_or_404(Competition, pk=obj_id)
    elif obj_type == 'entries':  # Handle deletion of entries
        obj = get_object_or_404(Flower, pk=obj_id)
    else:
        # Handle invalid object type
        return HttpResponse("Invalid object type")

    if request.method == 'POST':
        
        obj.delete()
        if (obj_type=='entries'):
            return redirect('user')
        else:
         return redirect(obj_type)  # Redirect to appropriate page after deletion

    context = {'obj': obj, 'obj_type': obj_type}
    return render(request, 'confirm_delete.html', context)

def confirm_delete_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'confirm_delete_user.html', {'user': user})

def pflowers(request):
    if request.method == 'POST':
        selected_color = request.POST.get('color', '')
        # Retrieve all flowers from the database
        flowers = Flower.objects.all()
        # Calculate similarity scores between selected color and each flower's color
        recommendations = []
        for flower in flowers:
            color_similarity = fuzz.ratio(selected_color.lower(), flower.color.lower())
            recommendations.append((flower, color_similarity))
        # Sort recommendations by similarity score
        recommendations.sort(key=lambda x: x[1], reverse=True)
        context = {'recommendations': recommendations}
    else:
        context = {}
    return render(request, "pflowers.html", context)