from django.urls import path, include
from .views import UsuarioList, UsuarioDetail, UsuarioCreate, UsuarioDelete, UsuarioLatLong
urlpatterns = [
    path('lista/',  UsuarioList.as_view(), name='usuario_list'),
    path('usuario/<int:pk>', UsuarioDetail.as_view(), name='usuario_detail'),
    path('crear/', UsuarioCreate.as_view(), name='usuario_create'),
    path('eliminar/<int:pk>', UsuarioDelete.as_view(), name='usuario_eliminar'),
    path('geocodificar_base/', UsuarioLatLong.as_view(), name='usuario_lat_long')
]