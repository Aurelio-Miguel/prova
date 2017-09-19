from django.conf.urls import url
from django.contrib import admin

from agenda.views import agenda
from agenda.views import feriado

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^agendas/', agenda, name='agenda'),
    url(r'^feriado/', feriado, name='feriado'),
    url(r'^agendas/usuario/(\+d)/', agenda, name='agenda'),
]
