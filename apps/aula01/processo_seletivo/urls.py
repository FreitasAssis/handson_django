from django.urls import path
from .views import aprovar_candidato, desaprovar_candidato

urlpatterns = [
    path('candidato/aprovar/', aprovar_candidato, name='processo_seletivo__aprovar_candidato'),
    path('candidato/desaprovar/', desaprovar_candidato, name='processo_seletivo__desaprovar_candidato'),
]
