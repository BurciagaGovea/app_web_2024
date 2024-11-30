from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html', {
        'title':'Inicio',
        'content':'Inicio index'
    })

def about(request):
    return render(request, 'mainapp/about.html', {
        'title':'Acerca de',
        'content':'Probando'
    })

def mision(request):
    return render(request, 'mainapp/mision.html', {
        'title':'Prueba misión',
        'content':'Probando2'
    })

def vision(request):
    return render(request, 'mainapp/vision.html', {
        'title':'Vision'
    })

def sesion(request):
    return render(request, 'mainapp/inicio.html', {
        'title':'Inicio sesión',
        'content':'Formulario sesión'
    })

def registro(request):
    return render(request, 'mainapp/registro.html', {
        'title':'Registro de usuario',
        'content':'Formulario de registro'
    })



def error404_2(request, exception):
    return render(request, 'mainapp/404.html', status=404)
