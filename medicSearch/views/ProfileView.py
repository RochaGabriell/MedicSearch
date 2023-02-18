from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from medicSearch.models import Profile
from django.core.paginator import Paginator
from medicSearch.forms.UserProfileForm import UserProfileForm, UserForm

def list_profile_view(request, id=None):
    profile = None
    if id is None and request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()
    elif id is not None:
        profile = Profile.objects.filter(user__id=id).first()
    elif not request.user.is_authenticated:
        return redirect(to='/')

    favorites = profile.show_favorites()
    if len(favorites) > 0:
        paginator = Paginator(favorites, 8)
        page = request.GET.get('page')
        favorites = paginator.get_page(page)

    ratings = profile.show_ratings()
    if len(ratings) > 0:
        paginator = Paginator(ratings, 8)
        page = request.GET.get('page')
        ratings = paginator.get_page(page)

    context = {
        'profile': profile,
        'favorites': favorites,
        'ratings': ratings
    }

    return render(request, template_name='profile/profile.html', context=context, status=200)


@login_required
def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    message = None
    # Caso o tipo de método seja GET, significa que a página acabou de carregar pela primeira vez, então não devemos passar o valor de request.POST para as classes UserProfileForm e UserForm, mas apenas a instância que carregará e preencherá os valores atuais no formulário. Caso o método seja do tipo POST, entraremos no fluxo que passará como primeiro parâmetro para as classes UserProfileForm e UserForm o request.POST, para que possamos informar os novos valores para as duas classes de forms, assim futuramente salvaremos esses valores no lugar dos valores anteriores.
    if request.method == 'POST': # Informa o tipo de requisição que foi feita, GET ou POST.
        
        profileForm = UserProfileForm(request.POST, request.FILES, instance=profile) # request.FILES - Estamos dizendo ao Django que queremos salvar arquivos enviados via formulário.
        userForm = UserForm(request.POST, instance=request.user)

        # Verifica se o e-mail que o usuário está tentando utilizar em seu perfil já existe em outro perfil
        verifyEmail = Profile.objects.filter(user__email=request.POST['email']).exclude(user__id=request.user.id).first()
        emailUnused = verifyEmail is None
    else:
        profileForm = UserProfileForm(instance=profile)
        userForm = UserForm(instance=request.user)

    if profileForm.is_valid() and userForm.is_valid() and emailUnused:
        profileForm.save() # Método do django form que usamos para pegar os valores válidos do formulário e salvar na model que o formulário representa.
        userForm.save()
        message = { 'type': 'success', 'text': 'Dados atualizados com sucesso' }
    else:
        if request.method == 'POST':
            if emailUnused:
                # Se o e-mail não está em uso mas o formulário tiver algum dado inválido.
                message = { 'type': 'danger', 'text': 'Dados inválidos' }
            else:  
                # Se o e-mail que o usuário tentou usar já está em uso por outra pessoa.
                message = { 'type': 'warning', 'text': 'E-mail já usado por outro usuário' }
    
    context = {
        'profileForm': profileForm,
        'userForm': userForm,
        'message': message
    }

    return render(request, template_name='user/profile.html', context=context, status=200)