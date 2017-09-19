from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=128)
    cpf = models.CharField(max_length=128)
    data_nascimento = models.DateField(blank=True, null=True)

class AgendaUsuario(models.Model):
    usuario = models.ForeignKey(Usuario, null = True, blank=False)
    agenda = models.ForeignKey(Agenda, null = True, blank=False)

class Agenda(models.Model):
    nome_agenda = models.CharField(max_length=128)

class Compromisso(models.Model):
    nome = models.CharField(max_length=128)
    data = models.DateField(blank=True, null=True)
    agenda = models.ForeignKey(Agenda, null = True, blank=False)
    usuario = models.ForeignKey(Usuario, null = True, blank=False)

class AgendaInstitucional(Agenda):
    feriado = models.ForeignKey(Feriado, null = True, blank=False)

class Feriado(Compromisso):
    nome = models.CharField(max_length=128)
    data = models.DateField(blank=True, null=True)