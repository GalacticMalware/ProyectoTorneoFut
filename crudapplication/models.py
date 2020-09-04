from django.db import models

class Fut(models.Model):
	cant_jugador = models.CharField(max_length=20)
	nombre_Dire = models.CharField(max_length=100)
	##email = models.EmailField()
	nombre = models.CharField(max_length=100)
	partidos_total = models.CharField(max_length=20)
	partidos_ganados = models.CharField(max_length=20)
	partidos_perdidos = models.CharField(max_length=100)
	partidso_empate = models.CharField(max_length=100)
	puntos = models.CharField(max_length=100)
	#posicion = models.CharField(max_length=100)
	class Meta:
		db_table = "equipos"



class Fut2(models.Model):
	nombre = models.CharField(max_length=20)
	edad = models.CharField(max_length=100)
	##email = models.EmailField()
	numero_juga = models.CharField(max_length=100)
	id_equipo = models.CharField(max_length=100)
	class Meta:
		db_table = "jugadores"

		

class Partido(models.Model):
	partidos_total = models.CharField(max_length=20)
	partidos_ganados = models.CharField(max_length=20)
	partidos_perdidos = models.CharField(max_length=100)
	partidso_empate = models.CharField(max_length=100)
	puntos = models.CharField(max_length=100)
	id_equipo = models.CharField(max_length=100)
	class Meta:
		db_table = "Partidos"



class Arbitro(models.Model):
	nombre = models.CharField(max_length=20)
	edad = models.CharField(max_length=20)
	id_equipo_a = models.CharField(max_length=100)
	id_equipo_b = models.CharField(max_length=100)
	infracciones = models.CharField(max_length=100)


	class Meta:
		db_table = "Partidos"
	
	
	
