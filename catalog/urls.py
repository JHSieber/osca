from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('allcoops/', views.AllCoopView.as_view(), name='all-coops'),
    path('allmembers/', views.AllMembersView.as_view(), name='all-members'),
    path('allofficers/', views.AllOfficersView.as_view(), name='all-officers'),
]