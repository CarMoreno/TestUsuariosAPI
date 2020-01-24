from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Usuario
from .serializers import UsuarioSerializer
import requests

class UsuarioList(APIView):
    def get(self, request):
        usuarios = Usuario.objects.all()
        data = UsuarioSerializer(usuarios, many=True).data
        return Response(data)

class UsuarioDetail(APIView):
    def get(self, request, pk):
        usuario = get_object_or_404(Usuario, pk=pk)
        data = UsuarioSerializer(usuario).data
        return Response(data, status=HTTP_200_OK)

class UsuarioCreate(APIView):
    def post(self, request):
        try:
            nombre = request.data.get('nombre')
            apellido = request.data.get('apellido')
            direccion = request.data.get('direccion')
            ciudad = request.data.get('ciudad')

            usuario = Usuario(nombre=nombre, apellido=apellido, direccion=direccion, ciudad=ciudad)
            usuario.save()
            serializer = UsuarioSerializer(usuario)
            return Response(serializer.data, status=HTTP_200_OK)
        except:
            return Response({'message': 'error server'}, HTTP_500_INTERNAL_SERVER_ERROR)

class UsuarioDelete(APIView):
    def delete(self, request, pk):
        usuario = get_object_or_404(Usuario, pk=pk)
        usuario.delete()
        return Response({"message": "Usuario con id `{}` ha sido eliminado.".format(pk)},status=HTTP_204_NO_CONTENT)


class UsuarioLatLong(APIView):

        API_KEY_GEOCODING = 'AIzaSyB0PLLiELJiVb1INOoJI3ye0ZAtLzbRGCs'

        def obtener_latlong(self, usuario):
            ubicacion = '{ciudad}+{direccion}'.format(ciudad=usuario.ciudad, direccion=usuario.direccion)
            stringRequest = 'https://maps.googleapis.com/maps/api/geocode/json?address={ubicacion}&key={API_KEY}'\
                .format(API_KEY=self.API_KEY_GEOCODING, ubicacion=ubicacion)
            dataFromGeocoding = requests.get(stringRequest).json()

            if len(dataFromGeocoding['results']) > 0:
                geometry = dataFromGeocoding['results'][0]['geometry']
                usuario.latitud = geometry['location']['lat']
                usuario.longitud = geometry['location']['lng']
                usuario.estadogeo = True
                usuario.save()
            else:
                usuario.latitud = 0
                usuario.longitud = 0

        def get(self, request):
            usuarios_sin_latlong = Usuario.objects.filter(latitud=None, longitud=None)
            for usuario in usuarios_sin_latlong:
                self.obtener_latlong(usuario)
            data = UsuarioSerializer(usuarios_sin_latlong, many=True).data
            return Response(data)