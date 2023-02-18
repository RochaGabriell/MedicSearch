# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from medicSearch.models import Profile, Rating
from medicSearch.forms.MedicForm import MedicRatingForm
from django.db.models import Q
from django.core.paginator import Paginator


def list_medics_view(request):
    name = request.GET.get("name")
    speciality = request.GET.get("speciality")
    neighborhood = request.GET.get("neighborhood")
    city = request.GET.get("city")
    state = request.GET.get("state")

    medics = Profile.objects.filter(role=2)
    
    if name is not None and name != '':
        medics = medics.filter(user__first_name__contains=name)
    if speciality is not None:
        medics = medics.filter(specialties__id=speciality)

    if neighborhood is not None:
        medics = medics.filter(addresses__neighborhood=neighborhood)
    else:
        if city is not None:
            medics = medics.filter(addresses__neighborhood__city=city)
        elif state is not None:
            medics = medics.filter(addresses__neighborhood__city__state=state)

    if len(medics) > 0:
        paginator = Paginator(medics, 8)
        page = request.GET.get('page')
        medics = paginator.get_page(page)

    get_copy = request.GET.copy()
    # Criando uma variável chamada parameters e copiando para ela os parâmetros atuais da url através do request.GET.copy(), removendo o parâmetro page com o método pop('page', True).
    parameters = get_copy.pop('page', True) and get_copy.urlencode() # Com o método get_copy.urlencode(), ao trocarmos de um número de paginação para outro não perdemos os parâmetros da url, pois foi usado a variável parameters para resolver isso

    context = {
        'medics': medics,
        'parameters': parameters
    }

    return render(request, template_name='medic/medics.html', context=context, status=200) # render possui um parâmetro chamado context, que é onde podemos passar um dicionário com dados que poderão ser acessados pelo nosso template.


def add_favorite_view(request):
    page = request.POST.get("page")
    name = request.POST.get("name")
    speciality = request.POST.get("speciality")
    neighborhood = request.POST.get("neighborhood")
    city = request.POST.get("city")
    state = request.POST.get("state")
    id = request.POST.get("id")

    try:
        profile = Profile.objects.filter(user=request.user).first()
        medic = Profile.objects.filter(user__id=id).first()
        profile.favorites.add(medic.user)
        profile.save()
        msg = "Favorito adicionado com sucesso"
        _type = "success"

    except Exception as erro:
        print(f"Erro {erro}")
        msg = "Um erro ocorreu ao salvar o médico nos favoritos"
        _type = "danger"

    if page:
        arguments = f"?page={page}"
    else:
        arguments = "?page=1"

    if name:
        arguments += f"&name={name}"
    if speciality:
        arguments += f"&specinality={speciality}"
    if neighborhood:
        arguments += f"&neighborhood={neighborhood}"
    if city:
        arguments += f"&city={city}"
    if state:
        arguments += f"&state={state}"

    arguments += f"&msg={msg}&type={_type}"

    return redirect(to=f'/medic/{arguments}')


def remove_favorite_view(request):
    page = request.POST.get("page")
    id = request.POST.get("id")

    try:
        profile = Profile.objects.filter(user=request.user).first()
        medic = Profile.objects.filter(user__id=id).first()
        profile.favorites.remove(medic.user)
        profile.save()
        msg = "Favorito removido com sucesso."
        _type = "success"
    except Exception as erro:
        print(f"Erro {erro}")
        msg = "Um erro ocorreu ao remover o médico nos favoritos."
        _type = "danger"

    if page:
        arguments = f"?page={page}"
    else:
        arguments = "?page=1"

    arguments += f"&msg={msg}&type={_type}"

    return redirect(to=f'/profile/{arguments}')


@login_required # Informar a view que o usuário precisa se autenticar para acessá-la.
def rate_medic(request, medic_id=None):
    medic = Profile.objects.filter(user__id=medic_id).first()
    rating = Rating.objects.filter(user=request.user, user_rated=medic.user).first()
    message = None
    initial = {'user': request.user, 'user_rated': medic.user} # Preencher o formulário informando quem avaliou e quem está sendo avaliado. Como os campos user e user_rated foram modificados para hidden,o usuário não poderá vê-lo e nem alterá-lo, deixar os valores desses campos já preenchidos.

    if request.method == 'POST':
        ratingForm = MedicRatingForm(request.POST, instance=rating, initial=initial)
    else:
        ratingForm = MedicRatingForm(instance=rating, initial=initial)

    if ratingForm.is_valid() and medic.role == 2:
        ratingForm.save()
        message = {'type': 'success', 'text': 'Avaliação salva com sucesso!'}
    elif medic.role != 2 and request.method == 'POST':
        message = {'type': 'danger', 'text': 'Esse usuário não é Médico!'}
    else:
        if request.method == 'POST':
            message = {'type': 'danger', 'text': 'Erro ao salvar avaliação!'}

    context = {
        'ratingForm': ratingForm,
        'medic': medic,
        'message': message
    }

    return render(request, template_name='medic/rating.html', context=context, status=200)