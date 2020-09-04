from rest_framework import serializers
from .models import Fut


	 

class UserSerializer(serializers.ModelSerializer):
		class Meta:
			model = Fut
			fields = ('cant_jugador', 'nombre_Dire','nombre','partidos_total','partidos_ganados','partidos_perdidos','partidso_empate','puntos')

