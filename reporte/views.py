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


<<<<<<< HEAD
def about(request):
    return render(request, 'reporte/example.html', {'title': 'About'})
=======
def nuestraHistoria(request):
    return render(request, 'reporte/nuestraHistoria.html', {'title': 'nuestraHistoria'})
def LaBabilla(request):
    return render(request, 'reporte/humedales/LaBabilla.html', {'title': 'LaBabilla'})
>>>>>>> a9b7b5315417e724dcfd4cff9d9ab4ed59f220cd
