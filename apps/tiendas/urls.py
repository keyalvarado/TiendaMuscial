from django.conf.urls import patterns, url
from .views import CrearTiendaView, ListaTiendaView, EditarTiendaView, EliminarTiendaView

urlpatterns = patterns('',
   url(r'^agregar/$',CrearTiendaView.as_view(),name="create-tienda"),
   url(r'^lista/$',ListaTiendaView.as_view(),name="lista-tienda"),
   url(r'^eliminar/(?P<pk>[0-9]+)/$', EliminarTiendaView.as_view() ,name="eliminar-tienda"),
   url(r'^editar/(?P<pk>\d+)/$', EditarTiendaView.as_view() ,name="editar-tienda"),
)
