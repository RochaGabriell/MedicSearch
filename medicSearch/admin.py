from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):

    #                          Customização o Admin

    # Esse componente nos permite criar um filtro de data dentro da listagem do admin

    # date_hierarchy = 'created_at'

    # Esse componente nos permite dizer ao Django quais elementos desejamos que sejam
    # exibidos na listagem dos dados damodel no admin

    # list_display = (
    #     'user',
    #     'role',
    #     'birthday',
    #     'created_at',
    # )

    # Esse componente nos permite alterar a apresentação dos campos vazios em nosso sistema

    # employ_value_display = 'Vazio'

    # Para podermos deixar outras linhas com o link de edição habilitado
    # Obs: Ela só funcionará se estiver listada napropriedade list_display

    # list_display_links = (
    #     'user',
    #     'role',
    # )

    # Permite que criemos um filtro de dados baseado noscampos que forem adicionados a essa lista.
    # Esse filtro fica alocadoao lado direito da tela de listagem da model admin

    # list_filter = ('user__is_active', )

    # Permite dizer quais campos serão exibidos no formulário equais não serão

    # fields = (
    #     'user',
    #     ('role', ),
    #     'image',
    #     'birthday',
    #     'specialties',
    #     'addresses',
    # )

    # É o oposto do fields.

    # exclude = (
    #     'favorites',
    #     'created_at',
    #     'updated_at',
    # )

    # deixa o campo apenas como leitura no formuláriode edição e criação.
    # Isso aqui para que não seja permitidoalterar o usuário atrelado a este perfi

    # readonly_fields = ('user', )

    # lista de campos que poderão ser pesquisados natela de listagem do admin

    # search_fields = (
    #     'user__username',
    #     'role',
    # )

    #                              Customização avançada

    # Agrupar os campos no formulário para que ele fique dividido de forma organizada na tela

    # fieldsets = (
    #     ('Usuário', {
    #         'fields': (
    #             'user',
    #             'birthday',
    #             'image',
    #         )
    #     }),
    #     ('Função', {
    #         'fields': ('role', )
    #     }),
    #     ('Extras', {
    #         'fields': (
    #             'specialties',
    #             'addresses',
    #         )
    #     }),
    # )

    # Customizar a exibição de um campono list_display simplesmente criando um método para ele

    # list_display = (
    #     'user',
    #     'birth',
    # )

    # def birth(self, obj):
    #     if obj.birthday:
    #         return obj.birthday.strftime("%d/%m/%Y")

    # Personalizar aforma com que o exibiremos quando estiver vazio

    # list_display = (
    #     'user',
    #     'birth',
    # )

    # def birth(self, obj):
    #     if obj.birthday:
    #         return obj.birthday

    # birth.empty_value_display = '___/___/_____'

    # Listar os campos que são do tipo ManyToMany em nossa aplicação.

    # list_display = (
    #     'user',
    #     'specialtiesList',
    #     'addressesList',
    # )

    # def specialtiesList(self, obj):
    #     return [i.name for i in obj.specialties.all()]

    # def addressesList(self, obj):
    #     return [i.name for i in obj.addresses.all()]

    # Adicionar arquivos css ejs em nosso admin

    # list_display = (
    #     'user',
    #     'specialtiesList',
    #     'addressesList',
    # )

    # class Media:
    #     css = {"all": ("css/custom.css", )}
    #     js = ("js/custom.js", )

    pass


# Register your models here.
admin.site.register(Rating)
admin.site.register(DayWeek)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Address)
admin.site.register(Speciality)
admin.site.register(Profile, ProfileAdmin)