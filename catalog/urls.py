from django.urls import path
from django.contrib import admin

from . import views
from django.conf.urls import include


urlpatterns = [
    path('', views.index, name='index'),
    path('allcoops/', views.AllCoopView.as_view(), name='all-coops'),
    path('allmembers/', views.AllMembersView.as_view(), name='all-members'),
    path('allofficers/', views.AllOfficersView.as_view(), name='all-officers'),
    path('addmemberinfo/',views.MemberCreate.as_view(),name='member-create'),
    path('addofficerinfo/',views.OfficersCreate.as_view(),name='officer-create'),
    path('keepworkchart/', views.WorkChartKeep.as_view(),name='keep-work-chart'),
    path('pylemenu/',views.PyleMenu,name='pyle-menu'),
    path('twcmenu/',views.TwcMenu,name='twc-menu'),
    path('harknessmenu/',views.HarknessMenu,name='harkness-menu'),
    path('keepmenu/',views.KeepMenu,name='keep-menu'),
    path('tankmenu/',views.TankMenu,name='tank-menu'),
    path('pylemenu/pylemembers',views.memberspyle,name=';pyle-members;'),
    path('harknessmenu/harknessmembers',views.membersharkness,name=';harkness-members;'),
    path('twcmenu/twcmembers',views.membersthirdworld,name=';twc-members;'),
    path('keepmenu/keepmembers',views.memberskeep,name=';keep-members;'),
    path('tankmenu/tankmembers',views.memberstank,name=';tank-members;'),
    path('pylemenu/pyleofficers',views.pyleofficers,name=';pyle-officers;'),
    path('harknessmenu/harknessofficers',views.harknessofficers,name=';harkness-officers;'),
    path('twcmenu/twcofficers',views.thirdworldofficers,name=';twc-officers;'),
    path('keepmenu/keepofficers',views.keepofficers,name=';keep-officers;'),
    path('tankmenu/tankofficers',views.tankofficers,name=';tank-officers;'),
    path('pylemenu/pyleallergies',views.allergiespyle,name=';pyle-allergies;'),
    path('harknessmenu/harknessallergies',views.allergiesharkness,name=';harkness-allergies;'),
    path('twcmenu/twcallergies',views.allergiesthirdworld,name=';twc-allergies;'),
    path('keepmenu/keepallergies',views.allergieskeep,name=';keep-allergies;'),
    path('tankmenu/tankallergies',views.allergiestank,name=';tank-allergies;'),
    path('pylemenu/pylebudget',views.pylebudget,name=';pyle-budget;'),
    path('harknessmenu/harknessbudget',views.harknessbudget,name=';harkness-budget;'),
    path('twcmenu/twcbudget',views.thirdworldbudget,name=';twc-budget;'),
    path('keepmenu/keepbudget',views.keepbudget,name=';keep-budget;'),
    path('tankmenu/tankbudget',views.tankbudget,name=';tank-budget;'),
    path('pylemenu/pyleworkchart',views.WorkChartPyle.as_view(),name=';pyle-workchart;'),
    path('harknessmenu/harknessworkchart',views.WorkChartHarkness.as_view(),name=';harkness-workchart;'),
    path('twcmenu/twcworkchart',views.WorkChartThirdWorld.as_view(),name=';twc-workchart;'),
    path('keepmenu/keepworkchart',views.WorkChartKeep.as_view(),name=';keep-workchart;'),
    path('tankmenu/tankworkchart',views.WorkChartTank.as_view(),name=';tank-workchart;'),

]

#Important account auth urls
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
