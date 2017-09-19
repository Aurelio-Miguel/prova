from django.shortcuts import render
from django.http import HttpResponse

from .models import Agenda
from .models import Feriado
from .models import AgendaUsuario

def agenda(request):
    lista_agenda = Agenda.objects.all()
    retorno = ""
    for agenda in lista_agenda:
        retorno += "<li>"+agenda.nome_agenda+"</li>"
    return HttpResponse(retorno)

def feriado(request):
    lista_feriado = Feriado.objects.all()
    retorno = ""
    for feriado in lista_feriado:
        retorno += "<li>"+feriado.nome+"</li>"
    return HttpResponse(retorno)

def agenda(request,id):
    lista_agenda = AgendaUsuario.objects.all()
    retorno = ""
    for agenda in lista_agenda:
        if id == agenda.usuario:
            retorno += "<li>"+agenda.nome+"</li>"
    return HttpResponse(retorno)
