# from django.http import HttpResponse
from django.shortcuts import render
from medicSearch.models.Speciality import Speciality
from medicSearch.models.State import State
from medicSearch.models.City import City
from medicSearch.models.Neighborhood import Neighborhood

def home_view(request):
    
    specialties = Speciality.objects.all()
    states = State.objects.all()
    cities = City.objects.all()
    neighborhoods = Neighborhood.objects.all()
    
    context = {
        'specialties': specialties,
        'states': states,
        'cities': cities,
        'neighborhoods': neighborhoods
    }

    return render(request, template_name='home/home.html', context=context, status=200)