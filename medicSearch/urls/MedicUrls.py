from django.urls import path
from medicSearch.views.MedicView import list_medics_view, add_favorite_view

urlpatterns = [
    path('', list_medics_view, name='medics'),
    path('favorite', add_favorite_view, name='medic-favorite'),
]