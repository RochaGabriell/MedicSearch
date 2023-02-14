from django.forms import ModelForm
from django import forms
from medicSearch.models.Profile import Profile
from django.contrib.auth.models import User


class UserProfileForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.role != 1:  # A classe ModelForm tem um atributo dentro dela que retorna a instance atual do formulário, que nesse caso é opróprio perfil.
            del self.fields['role']

    # classe que usamos para configurar o nosso formulário que é baseado em uma model do sistema. Não é necessário quando criamos um formulário customizado que não usa uma model como base.
    class Meta:
        model = Profile
        fields = [ 'user', 'role', 'birthday', 'image']  # usamos esse atributo recebendo uma lista correspondente aos campos que desejamos que sejam exibidos em nosso formulário.
        # Usamos '__all__' para exibir todos os campos como itens do formulário
        # Usamos exclude para excluir campos específicos do sistema
        # exclude = ['']

        widgets = {
            'user': forms.HiddenInput(),
            'role': forms.Select(attrs={'class': "form-control"}),
            'birthday': forms.DateInput(attrs={
                'class': "form-control",
                "type": "date"
            }),
            'image': forms.FileInput(attrs={'class': "form-control"})
        }  # Dicionário onde podemos passar o nome do campo que desejamos modificar, podemos mudar o tipo de campo, de um input text para e-mail, por exemplo, ou podemos passar um input text para textarea, podemos criar máscaras para uma data, definir um disabled para o input, required etc


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'})
        }