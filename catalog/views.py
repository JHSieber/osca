from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
import time
import subprocess

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin




from django.template import RequestContext

from catalog.forms import addMemberInfo


# Create your views here.

from .models import Coop, Member, Officer, Allergy, AllergySeverity, Budget, Meal, Menu, Shift, WorkChartRow

KEEP = 1
TANK = 2
PYLE = 3
HARKNESS = 4
THIRDWORLD= 5

def index1(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_coops = Coop.objects.all().count()
    num_members = Member.objects.all().count()
     

    # Available books (status = 'a')
    #num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    #num_authors = Author.objects.count()

    context = {
        'num_coops': num_coops,
        'num_members': num_members,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def index(request): 
    """
    View function to show every office in Pyle
    """

    officers_pyle= Officer.objects.select_related("coop").filter(coop_id__exact=PYLE)
    num_officers=Officer.objects.all().count()

    current_time = int(time.time() % 3)
    print(current_time)
    if current_time % 2 == 0:
        subprocess.check_call(['python', 'quickstart.py'])


    context={
        'officers_pyle': officers_pyle

    }


    return render(request,'index.html',context=context)


class AllMembersView(generic.ListView):
    model = Member
    paginate_by = 30
    num_members= Member.objects.all().count()
    template_name = 'catalog/allmembers.html'  # Specify your own template name/location


# def allmembers(request):
#     """
#     Displays all members in all Coops 

#     """

#     allmember= Member.objects.all()
#     num_members=Member.objects.all().count()

#     context={
#         'allmember':allmember
#     }

#     return render(request,'catalog/allmembers.html',context=context)

def memberspyle(request): 
    """
    View function to show members of Pyle Coop
    """

    pylemembers= Member.objects.select_related("coop").filter(coop_id__exact=PYLE)

    context={
        'pylemembers': pylemembers
    }


    return render(request,'memberspyle.html',context=context)

def membersthirdworld(request): 
    """
    View function to show members of Third World Coop
    """

    thirdworldm= Member.objects.select_related("coop").filter(coop_id__exact=THIRDWORLD)

    context={
        'thirdworldm': thirdworldm
    }

    return render(request,'membersthirdworld.html',context=context)


def memberstank(request): 
    """
    View function to show members of Tank Coop
    """

    tankmembers= Member.objects.select_related("coop").filter(coop_id__exact=TANK)

    context={
        'tankmembers': tankmembers
    }

    return render(request,'memberstank.html',context=context)

def membersharkness(request): 
    """
    View function to show members of Harkness Coop
    """

    harknessmembers= Member.objects.select_related("coop").filter(coop_id__exact=HARKNESS)

    context={
        'harknessmembers': harknessmembers
    }

    return render(request,'membersharkness.html',context=context)

def memberskeep(request):

    "View function to show members of Keep Coop"

    keepmembers=Member.objects.select_related("coop").filter(coop_id__exact=KEEP)

    context={
        'keepmembers': keepmembers
    }

    return render(request,'memberskeep.html',context=context)


class AllOfficersView(generic.ListView):
    model = Officer
    paginate_by = 30
    template_name = 'catalog/allofficers.html'  # Specify your own template name/location
    


def all_officers(request):
    """
    View fucntion to show every officer in the Officer's Database
    """   

    allofficers=Officer.objects.all()
    num_officers=Officer.objects.all().count()

    context={
        'allofficers':allofficers,
        'num_officers':num_officers,
    } 

    return render(request,'allofficers.html',context=context)

def pyleofficers(request): 
    """
    View function to show every officer in the Pyle Coop
    """

    officers_pyle= Officer.objects.select_related("coop").filter(coop_id__exact=PYLE)

    context={
        'officers_pyle': officers_pyle
        
    }

    return render(request,'pyleofficers.html',context=context)

def harknessofficers(request):
    """
    View function to show every officer in the Pyle Coop
    """

    officers_harkness= Officer.objects.select_related("coop").filter(coop_id__exact=HARKNESS)

    context={
        'officers_harkness': officers_harkness
        
    }

    return render(request,'harknessofficers.html',context=context)

def tankofficers(request):

    """
    View function to show every officer in the Tank Coop
    """

    officers_tank= Officer.objects.select_related("coop").filter(coop_id__exact=TANK)

    context={
        'officers_tank': officers_tank
        
    }

    return render(request,'tankofficers.html',context=context)

def keepofficers(request):

    """
    View function to show every officer in the Keep Coop
    """

    officers_keep= Officer.objects.select_related("coop").filter(coop_id__exact=KEEP)

    context={
        'officers_keep': officers_keep
        
    }

    return render(request,'tankofficers.html',context=context)

def thirdworldofficers(request):

    """
    View function to show every officer in the Keep Coop
    """

    officers_thirdworld= Officer.objects.select_related("coop").filter(coop_id__exact=THIRDWORLD)

    context={
        'officers_thirdworld': officers_thirdworld
        
    }

    return render(request,'thirdworldofficers.html',context=context)

class AllCoopView(generic.ListView):
    model = Coop
    paginate_by = 30
    template_name = 'catalog/allcoops.html'  # Specify your own template name/location


    

# def all_coops(request):
    
    
#     """
#     View fucntion to show a list of every coop in the Coop database
#     """   

#     allcoops=Coop.objects.all()
#     num_coop=Coop.objects.all().count()

#     context={
#         'allcoops':allcoops,
#         'num_coop':num_coop,
#     } 

#     return render(request,'allcoops.html',context=context)

def allallergies(request):

    """
    View function to show a list of allergies in all coops
    """

    allallergies= Allergy.objects.all()

    context={
        'allallergies':allallergies
    }
    
    return render(request, 'allallergies.html',context=context)

def allergiestank(request):
    """
    View function to show every allergy in the Tank Coop
    """

    allergytank= Allergy.objects.select_related("coop").filter(coop_id__exact=TANK)

    context={
        'allergytank': allergytank
        
    }

    return render(request,'allergytank.html',context=context)

def allergiespyle(request):

    """
    View function to show every allergy in the Pyle Coop
    """

    allergypyle= Allergy.objects.select_related("coop").filter(coop_id__exact=PYLE)

    context={
        'allergypyle': allergypyle
        
    }

    return render(request,'allergypyle.html',context=context)

    

def allergiesharkness(request):
    """
    View function to show every allergy in the Tank Coop
    """

    allergyharkness= Allergy.objects.select_related("coop").filter(coop_id__exact=HARKNESS)

    context={
        'allergyharkness': allergyharkness
        
    }

    return render(request,'allergyharkness.html',context=context)


def allergieskeep(request):
    """
    View function to show every allergy in the Keep Coop
    """

    allergykeep= Allergy.objects.select_related("coop").filter(coop_id__exact=KEEP)

    context={
        'allergykeep': allergykeep
        
    }

    return render(request,'allergykeep.html',context=context)
 

def allergiesthirdworld(request):
    """
    View function to show every allergy in the Third World Coop
    """

    allergythirdworld= Allergy.objects.select_related("coop").filter(coop_id__exact=THIRDWORLD)

    context={
        'allergythirdworld': allergythirdworld
        
    }

    return render(request,'allergythirdworld.html',context=context)
           

def tankbudget(request):
    """

    View function to show Tank Coop's budget
    """

    tankbudget=Budget.objects.select_related("coop").filter(coop_id=1)

    context={
        'tankbudget':tankbudget
    }

    return render(request,'tankbudget.html', context=context)

def pylebudget(request):
    """

    View function to show Pyle Coop's Budget
    """

    pylebudget=Budget.objects.select_related("coop").filter(coop_id=2)

    context={
        'pylebudget':pylebudget
    }

    return render(request,'pylebudget.html', context=context)

def harknessbudget(request):
    """

    View function to show Harkness Coop's Budget
    """

    harkbudget=Budget.objects.select_related("coop").filter(coop_id=3)

    context={
        'harkbudget':harkbudget
    }

    return render(request,'harkbudget.html', context=context)


def keepbudget(request):
    """

    View function to show Keep Coop's Budget
    """

    keepbudget=Budget.objects.select_related("coop").filter(coop_id=4)

    context={
        'keepbudget':keepbudget
    }

    return render(request,'keepbudget.html', context=context)


def thirdworldbudget(request):
    """

    View function to show Third World Coop's Budget
    """

    thirdworldbudget=Budget.objects.select_related("coop").filter(coop_id=5)

    context={
        'thirdworldbudget':thirdworldbudget
    }

    return render(request,'thirdworldbudget.html', context=context)


# Form Views -------------------->

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from catalog.models import Member

class MemberCreate(PermissionRequiredMixin, CreateView, SuccessMessageMixin):
    permission_required = 'catalog.add_officer'
    model = Member
    fields = ['id','first_name','last_name','preferred_name','tnumber','coop','email','pronouns','time_aid','missed_jobes']
    success_url = reverse_lazy('all-members')

class MemberUpdate(UpdateView):
    model = Member
    fields = ['id','first_name','last_name','preferred_name','tnumber','coop','email','pronouns','time_aid','missed_jobes']
    success_url = reverse_lazy('all-members')

class MemberDelete(DeleteView):
    model = Member
    success_url = reverse_lazy('authors')

class OfficersCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'catalog.add_officer'
    model=Officer
    fields = ['id','coop','member','position_name','position_description','hours_required','emergency_contact','all_osca']
    success_url=reverse_lazy('all-officers')

  
class OfficersUpdate(UpdateView):
    model=Officer
    fields = ['id','coop','member','position_name','position_description','hours_required','emergency_contact','all_osca']
    success_url=reverse_lazy('all-officers')

#Menu Views

def PyleMenu(request):

    context={
        
    }

    return render(request,'catalog/pyle_menu.html', context=context)

def TwcMenu(request):

    context={
        
    }

    return render(request,'catalog/twc_menu.html', context=context)

def HarknessMenu(request):

    context={
        
    }

    return render(request,'catalog/harkness_menu.html', context=context)    

def KeepMenu(request):
    context={

    }
    return render(request,'catalog/keep_menu.html',context=context)

def TankMenu(request):

    context={
        
    }

    return render(request,'catalog/tank_menu.html', context=context)    





class WorkChartKeep(generic.ListView):
    model=WorkChartRow
    template_name = 'catalog/keepworkchart.html'  # Specify your own template name/location

    def get_queryset(self):
        keep = Coop.objects.get(name = "Keep")
        return WorkChartRow.objects.filter(coop=keep)

class WorkChartPyle(generic.ListView):
    model=WorkChartRow
    template_name = 'catalog/pyleworkchart.html'  # Specify your own template name/location

    def get_queryset(self):
        pyle = Coop.objects.get(name = "Pyle")
        return WorkChartRow.objects.filter(coop=pyle)

class WorkChartTank(generic.ListView):
    model=WorkChartRow
    template_name = 'catalog/tankworkchart.html'  # Specify your own template name/location

    def get_queryset(self):
        tank = Coop.objects.get(name = "Tank")
        return WorkChartRow.objects.filter(coop=tank)

class WorkChartHarkness(generic.ListView):
    model=WorkChartRow
    template_name = 'catalog/harknessworkchart.html'  # Specify your own template name/location

    def get_queryset(self):
        harkness = Coop.objects.get(name = "Harkness")
        return WorkChartRow.objects.filter(coop=harkness)

class WorkChartThirdWorld(generic.ListView):
    model=WorkChartRow
    template_name = 'catalog/thirdworldcoopworkchart.html'  # Specify your own template name/location

    def get_queryset(self):
        thirdWorld = Coop.objects.get(name = "Third World House")
        return WorkChartRow.objects.filter(coop=thirdWorld)

