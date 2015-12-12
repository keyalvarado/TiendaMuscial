from django.core.checks import messages
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, TemplateView,View

from apps.tiendas.forms import CrearTiendaForm
from apps.tiendas.models import Tienda


class CrearTiendaView(CreateView):
    model = Tienda
    form_class = CrearTiendaForm
    template_name = "tienda/form.html"
    success_url = reverse_lazy('tienda:lista-tienda')

class ListaTiendaView(ListView):

    model = Tienda
    template_name = "tienda/list.html"
    context_object_name = "tiendas"

    def dispatch(self, request, *args, **kwargs):
        return super(ListaTiendaView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Tienda.objects.all()
        return queryset


class EliminarTiendaView(DeleteView):
    model = Tienda
    success_url = reverse_lazy('tienda:lista-tienda')
    template_name = "tienda/delete.html"



class EditarTiendaView(UpdateView):
    model = Tienda
    form_class = CrearTiendaForm
    template_name = "tienda/form.html"
    success_url = reverse_lazy('tienda:lista-tienda')


