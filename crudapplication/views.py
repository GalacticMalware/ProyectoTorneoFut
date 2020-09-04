from django.shortcuts import render, redirect
from crudapplication.forms import FutForm,FutForm2
from crudapplication.models import Fut,Fut2,Partido
from rest_framework import views
from .serializador import UserSerializer
from rest_framework.response import Response




class UserViewSet(views.APIView):

	def get(self,request):
		resultado = []
		queryset = Fut.objects.all()
		#serializer_class = UserSerializer
		resultado = UserSerializer(queryset,many=True).data

		return Response(resultado)





def emp(request):
	if  request.method == "POST":
		form = FutForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect("/show")
			except:
				pass
	else:
		form = FutForm()
	return render(request,"index.html",{'form':form})

def show(request):
	equiposs = Fut.objects.all()
	return render(request, "show.html",{'equiposs':equiposs})


def edit(request, id):
	equipos = Fut.objects.get(id=id)
	return render(request,"edit.html",{'equipos':equipos})

def update(request, id):
	equipos = Fut.objects.get(id=id)
	form = FutForm(request.POST, instance= equipos)
	if form.is_valid():
		form.save()
		return redirect('/show')
	return render(request,"edit.html",{'equipos': equipos})

def delete(request, id):
	equipos = Fut.objects.get(id=id)
	equipos.delete()
	return redirect("/show")


def inicio(request):
	if  request.method == "POST":
		form = Fut(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect("/show")
			except:
				pass
	else:
		form = FutForm()
	return render(request,"inicio.html",{'form':form})




def jugador(request,id):
	jugadoress = Fut2.objects.filter(id_equipo=id).all()
	#form2 = FutForm2(request.POST)
	#form2 = FutForm2()
	#jugadoress = Fut2.objects.all()
	return render(request, "jugadores.html",{'jugadoress':jugadoress})



def partidos(request):
	equiposs = Fut.objects.all()
	return render(request,"Resultados.html",{'equiposs':equiposs})

#equipos = Fut.objects.get(id=id)
#	return render(request,"edit.html",{'equipos':equipos})