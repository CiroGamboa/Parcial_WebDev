from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from artist.models import *
from artist.forms import ImageForm


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

# Metodo para logearse
def login_usuario(request,nickname,passw):
	if request.method == 'GET':
		try:
			usuario = Autor.objects.get(nombreart=nickname,artpassword=passw)
			idUsuario = usuario.id

		except User.DoesNotExist:
			return JSONResponse('0')

		request.session['nickname'] = nickname
		return JSONResponse(idUsuario) #HttpResponseRedirect(pagina de inicio)
	else:
		return HttpResponse(status=404)

# Metodo para cerrar sesion
def logout(request):
	try:
		del request.session['nickname']
	except:
		pass
	#return HttpResponseRedirect("/login")
	return JSONResponse("Bye") 



# Create your views here.
def imageView(request):
	if request.method == 'POST':
		form = ImageForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('formImagen:index')
	else:
		form = ImageForm()
	return render(request, 'imagenSubida.html', {'form': form,})

def finalView(request):
	return render(request, 'index.html')



def init_db():
	Autor.objects.create(nombreart='Gsus',artpassword='123',nombres="Jesus Alfonso",apellidos="Gamboa Nazareth",email="gsus@perdonadordepecados.dios")
	Estilo.objects.create(estilo="Pintura sobre oleo")
	TipoObra.objects.create(tipoobra="Pintura")

# Metodo para agregar otro artista

# Metodo para subir obras

# Metodo para obtener un numero determinado de obras para mostrar sin necesidad de registro

# 
