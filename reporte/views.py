from django.shortcuts import render

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'reporte/home.html', context)


def about(request):
    return render(request, 'reporte/example.html', {'title': 'About'})

def nuestraHistoria(request):
    return render(request, 'reporte/nuestraHistoria.html', {'title': 'About'})
def LaBabilla(request):
    return render(request, 'reporte/humedales/LaBabilla.html', {'title': 'About'})

def babilla_flora(request):
    return render(request, 'reporte/humedales/galeria_flora.html', {'title': 'About'})

def babilla_fauna(request):
    return render(request, 'reporte/humedales/galeria_fauna.html', {'title': 'About'})
def babilla_acuatica(request):
    return render(request, 'reporte/humedales/galeria_acuatica.html', {'title': 'About'})

def planes_manejo(request):
    return render(request, 'reporte/planes_manejo.html', {'title': 'About'})

def programas(request):
    return render(request, 'reporte/programas.html', {'title': 'About'})


def hacer_reporte(request):
    return render(request, 'reporte/hacer_reporte.html', {'title': 'About'})
