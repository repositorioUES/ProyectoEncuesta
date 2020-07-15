from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse,reverse_lazy
from django.views.generic import TemplateView,CreateView
from .models import Usuario, Respuesta, Tipo_transporte, Reclamo 
from .forms import UsuarioForm, RespuestaForm
from django.shortcuts import redirect

# Create your views here.
#model = None

def loginT(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		print(user)
		if user is not None:
			login(request,user)
			return HttpResponseRedirect(reverse('inicio'))
		else:
			messages.error(request,'Credenciales incorrectas')

	return render(request,'login.html',{})

def logoutT(request):
	logout(request)
	return HttpResponseRedirect(reverse('inicio'))


class Inicio(TemplateView):
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["qs"] = Usuario.objects.all()
		context["p1"] = Respuesta.objects.filter(numerodepregunta=1).count()
		context["p2"] = Respuesta.objects.filter(numerodepregunta=2).count()
		context["p3"] = Respuesta.objects.filter(numerodepregunta=3).count()
		context["p4"] = Respuesta.objects.filter(numerodepregunta=4).count()
		context["p5"] = Respuesta.objects.filter(numerodepregunta=5).count()
		context["p6"] = Respuesta.objects.filter(numerodepregunta=6).count()
		context["p7"] = Respuesta.objects.filter(numerodepregunta=7).count()
		context["p8"] = Respuesta.objects.filter(numerodepregunta=8).count()
		context["p9"] = Respuesta.objects.filter(numerodepregunta=9).count()
		return context

#noDui = ""
class UsuarioCrear(CreateView):
	model = Usuario
	form_class = UsuarioForm
	template_name = 'Usuario_Form.html'

	def post(self, request, *args, **kwargs):
		#global noDui
		noDui = request.POST.get('dui') 
		nom = request.POST.get('nombre')
		apel = request.POST.get('apellidos')
		ed = request.POST.get('edad') 
		sex = request.POST.get('sexo')
		dom = request.POST.get('domicilio')
		tipo = request.POST.get('tipo_transporte')
		ipoTrasporte = Tipo_transporte.objects.get(tipo_transporte = tipo)		
		usuario = Usuario(dui = noDui, nombre = nom, apellidos = apel, edad = ed, sexo = sex, domicilio = dom, tipo_transporte = ipoTrasporte)
		usuario.save()
		obtenerDui(request)
		crearReclamo(request)
		return redirect('llenar_e')

def crearReclamo(request):
	usuario = Usuario.objects.get(dui =numeroDui)
	existe = Reclamo.objects.filter(idreclamo = usuario).exists()
	if existe != True:
		reclamoADD = Reclamo(idreclamo = usuario, realizado = False) 
		reclamoADD.save()
			
def obtenerDui(request):
	global numeroDui
	numeroDui = request.POST.get('dui') 

	
def Encuesta(request):
		if request.method == 'POST':
			guardarPreguntas(request)
			actualizarReclamo(request)
			print(numeroDui, "CAMBIO")
			return redirect('inicio')
		return render(request, 'llenarE.html')

def guardarPreguntas(request):
	global bandera
	usuario = Usuario.objects.get(dui =numeroDui)
	pregunta1 = request.POST.get('p1')
	if pregunta1 != None:
		respuesta1 = Respuesta.objects.filter(dui =numeroDui).filter(numerodepregunta = pregunta1).exists()
		if respuesta1 != True:
			print(respuesta1,'FILTRO OBTENIDO')
			respuesta = Respuesta(dui = usuario, numerodepregunta = pregunta1)
			respuesta.save()
			bandera = 1
	
	pregunta2 = request.POST.get('p2')
	if pregunta2 != None:
		respuesta2 = Respuesta.objects.filter(dui =numeroDui).filter(numerodepregunta = pregunta2).exists()
		if respuesta2 != True:
			respuesta = Respuesta(dui = usuario, numerodepregunta = pregunta2)
			respuesta.save()
			bandera = 1
			print(pregunta2, 'EL VALOR ES CORRECTO')
	
	pregunta3 = request.POST.get('p3')
	if pregunta3 != None:
		respuesta3 = Respuesta.objects.filter(dui =numeroDui).filter(numerodepregunta = pregunta3).exists()
		if respuesta3 != True:
			respuesta = Respuesta(dui = usuario, numerodepregunta = pregunta3)
			respuesta.save()
			bandera = 1
			print(pregunta3, 'EL VALOR ES CORRECTO')
	
	pregunta4 = request.POST.get('p4')
	if pregunta4 != None:
		respuesta4 = Respuesta.objects.filter(dui =numeroDui).filter(numerodepregunta = pregunta4).exists()
		if respuesta4 != True:
			respuesta = Respuesta(dui = usuario, numerodepregunta = pregunta4)
			respuesta.save()
			bandera = 1
			print(pregunta4, 'EL VALOR ES CORRECTO')
	
	pregunta5 = request.POST.get('p5')
	if pregunta5 != None:
		respuesta5 = Respuesta.objects.filter(dui =numeroDui).filter(numerodepregunta = pregunta5).exists()
		if respuesta5 != True:
			respuesta = Respuesta(dui = usuario, numerodepregunta = pregunta5)
			respuesta.save()
			print(pregunta5, 'EL VALOR ES CORRECTO')
			bandera = 1
			print(pregunta5, ' EL VALOR ES CORRECTO')
	
	pregunta6 = request.POST.get('p6')
	if pregunta6 != None:
		respuesta6 = Respuesta.objects.filter(dui =numeroDui).filter(numerodepregunta = pregunta6).exists()
		if respuesta6 != True:
			respuesta = Respuesta(dui = usuario, numerodepregunta = pregunta6)
			respuesta.save()
			bandera = 1
			print(pregunta6, 'EL VALOR ES CORRECTO')
	
	pregunta7 = request.POST.get('p7')
	if pregunta7 != None:
		respuesta7 = Respuesta.objects.filter(dui =numeroDui).filter(numerodepregunta = pregunta7).exists()
		if respuesta7 != True:
			respuesta = Respuesta(dui = usuario, numerodepregunta = pregunta7)
			respuesta.save()
			bandera = 1
			print(pregunta7, 'EL VALOR ES CORRECTO')
	
	pregunta8 = request.POST.get('p8')
	if pregunta8 != None:
		respuesta8 = Respuesta.objects.filter(dui =numeroDui).filter(numerodepregunta = pregunta8).exists()
		if respuesta8 != True:
			respuesta = Respuesta(dui = usuario, numerodepregunta = pregunta8)
			respuesta.save()
			bandera = 1
			print(pregunta8, 'EL VALOR ES CORRECTO')
	
	pregunta9 = request.POST.get('p9')
	if pregunta9 != None:
		respuesta9 = Respuesta.objects.filter(dui =numeroDui).filter(numerodepregunta = pregunta9).exists()
		if respuesta9 != True:
			respuesta = Respuesta(dui = usuario, numerodepregunta = pregunta9)
			respuesta.save()
			bandera = 1
			print(pregunta9, 'EL VALOR ES CORRECTO')

def actualizarReclamo(request):
	usuario = Usuario.objects.get(dui =numeroDui)
	reclamo = Reclamo.objects.filter(idreclamo = usuario).exists()
	#print(bandera, reclamo)
	if bandera == 1 and reclamo == True:
		preguntaOpcional = request.POST.get('campoOpcional')
		Reclamo.objects.filter(idreclamo = usuario).update(descripcion = preguntaOpcional,realizado = True)
		print("DENTRO DEL IF")
		




			

