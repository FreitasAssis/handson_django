from django.shortcuts import render
from django.http import HttpResponse


def aprovar_candidato(request):
    return HttpResponse("Candidato aprovado!")


def desaprovar_candidato(request):
    return HttpResponse('{"result": "Sucess", errors: []}')
