# from django.http import HttpResponse
from django.shortcuts import render
from medicSearch.models.Speciality import Speciality
from medicSearch.models.State import State
from medicSearch.models.City import City
from medicSearch.models.Neighborhood import Neighborhood
from medicSearch.models.Profile import Profile


def home_view(request):
    # Filtro os perfis que têm pelo menos uma especialidade associada a ele
    medics_has_specialties = Profile.objects.filter(specialties__isnull=False).distinct()
    medics_has_specialties = medics_has_specialties.values_list('specialties__id', flat=True) # values_list é utilizado para selecionar apenas o campo 'id' da relação many-to-many com a model Speciality através do campo 'specialties'. O argumento flat=True indica que queremos uma lista plana (ao invés de uma lista de tuplas) contendo apenas os valores de 'id'.
    specialties = []
    for speciality_id in medics_has_specialties:
        specialties.append(Speciality.objects.get(id=speciality_id))


    medics_has_states = Profile.objects.filter(addresses__neighborhood__city__state__isnull=False).distinct()
    medics_has_states = medics_has_states.values_list('addresses__neighborhood__city__state__id', flat=True)

    states = []
    for state_id in medics_has_states:
        states.append(State.objects.get(id=state_id))
    
    
    medics_has_city = Profile.objects.filter(addresses__neighborhood__city__isnull=False).distinct()
    medics_has_city = medics_has_city.values_list('addresses__neighborhood__city__id', flat=True)

    cities = []
    for city_id in medics_has_city:
        cities.append(City.objects.get(id=city_id))
    

    medics_has_neighborhood = Profile.objects.filter(addresses__neighborhood__isnull=False).distinct()
    medics_has_neighborhood = medics_has_neighborhood.values_list('addresses__neighborhood__id', flat=True)

    neighborhoods = []
    for neighborhood_id in medics_has_neighborhood:
        neighborhoods.append(Neighborhood.objects.get(id=neighborhood_id))


    context = {
        'specialties': specialties,
        'states': states,
        'cities': cities,
        'neighborhoods': neighborhoods
    }

    return render(request, template_name='home/home.html', context=context, status=200)


def page_not_found(request, exception):
    return render(request, template_name='status/404.html', status=404) 