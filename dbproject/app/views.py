from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Organizers, Flower, User, Competition, Perennials, Annuals
from .Form import CompetitionUpdateForm, Insertflower, Insertuser, Insertcompetition, OrganizerUpdateForm, UserUpdateForm, randc, InsertOrganizer
from .filters import entriesFilter, thefilter, OrganizersFilter, CompetitionsFilter
from fuzzywuzzy import fuzz
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
    print(entry)
    f_filter = entriesFilter(request.GET, queryset=u_entry)
    u_entry = f_filter.qs
    context = {'entries' : u_entry,
               'filter' : f_filter,
               'entry': entry}
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

def user_forms(request, what, page, entry):
    u_form = Insertuser()
    o_form = InsertOrganizer()
    c_form = Insertcompetition()
    f_form = Insertflower()

    while page == "User":
        if what == "insert" :
            if request.method == 'POST':
                u_form = Insertuser(request.POST) #data submitted(POST request)
                if u_form.is_valid():
                    u_form.save() #inserts to db if valid
                    return redirect('user')
        elif what == "update":
            print("update")
        elif what == "remove":
            print("remove")
        break

    while page == "Organizer":
        if what == "insert" :
            if request.method == 'POST':
                o_form = InsertOrganizer(request.POST) #data submitted(POST request)
                if o_form.is_valid():
                    o_form.save() #inserts to db if valid
                    return redirect('organizers')
        elif what == "update":
            print("update")
        elif what == "remove":
            print("remove")
        break

    while page == "Competition":
        if what == "insert" :
            if request.method == 'POST':
                c_form = Insertcompetition(request.POST) #data submitted(POST request)
                if c_form.is_valid():
                    c_form.save() #inserts to db if valid
                    return redirect('competitions')
        elif what == "update":
            print("update")
        elif what == "remove":
            print("remove")
        break

    while page == "Userentry":
        if what == "insert" :
            if request.method == 'POST':
                f_form = Insertflower(request.POST) #data submitted(POST request)
                if f_form.is_valid():
                    f_form.save() #inserts to db if valid
                    return redirect('competitions')
        elif what == "update":
            print("update")
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

def pflowers(request):
    return render(request,"pflowers.html")

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
    else:
        # Handle invalid object type
        return HttpResponse("Invalid object type")

    if request.method == 'POST':
        obj.delete()
        return redirect(obj_type)  # Redirect to appropriate page after deletion

    context = {'obj': obj, 'obj_type': obj_type}
    return render(request, 'confirm_delete.html', context)

def confirm_delete_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'confirm_delete_user.html', {'user': user})

def update_user(request, u_id):
    user = get_object_or_404(User, pk=u_id)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user')
    else:
        form = UserUpdateForm(instance=user)
    return render(request, 'update_user.html', {'form': form})

def update_organizer(request, o_id):
    organizer = get_object_or_404(Organizers, pk=o_id)
    if request.method == 'POST':
        form = OrganizerUpdateForm(request.POST, instance=organizer)
        if form.is_valid():
            form.save()
            return redirect('organizers')
    else:
        form = OrganizerUpdateForm(instance=organizer)
    return render(request, 'update_organizer.html', {'form': form})

def update_competition(request, c_id):
    competition = get_object_or_404(Competition, pk=c_id)
    if request.method == 'POST':
        form = CompetitionUpdateForm(request.POST, instance=competition)
        if form.is_valid():
            form.save()
            return redirect('competitions')
    else:
        form = CompetitionUpdateForm(instance=competition)
    return render(request, 'update_competition.html', {'form': form})

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