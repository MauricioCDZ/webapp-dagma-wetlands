<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404
from .models import Reporte
from users.models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def home(request):
  
    return render(request, 'reporte/example.html')



def about(request):
    context = {
         'reportes': Reporte.objects.all()
    }
    return render(request, 'reporte/home.html', context)

class ReporteListView(ListView):
    model = Reporte
    template_name = 'reporte/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'reportes'
    ordering = ['-fecha_reporte']


class UserReporteListView(ListView):
    model = Reporte
    template_name = 'reporte/user_reports.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'reportes'
    

    def get_queryset(self):
        user = get_object_or_404(CustomUser, name=self.kwargs.get('name'))
        return Reporte.objects.filter(autor=user).order_by('-fecha_reporte')


class ReporteDetailView(DetailView):
    model = Reporte


class ReporteCreateView(LoginRequiredMixin, CreateView):
    model = Reporte
    fields = ['titulo', 'descripcion','image','humedal']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class ReporteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Reporte
    fields = ['titulo', 'descripcion','image','humedal']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        reporte = self.get_object()
        if self.request.user == reporte.autor:
            return True
        return False

class ReporteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Reporte
    success_url = '/'

    def test_func(self):
        reporte = self.get_object()
        if self.request.user == reporte.autor:
            return True
        return False

=======
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
>>>>>>> 5752ea43f40a6c0470a69916c429a8a7c275278e

def nuestraHistoria(request):
    return render(request, 'reporte/nuestraHistoria.html', {'title': 'About'})
def LaBabilla(request):
    return render(request, 'reporte/humedales/LaBabilla.html', {'title': 'About'})
<<<<<<< HEAD
=======
def ElRetiro(request):
    return render(request, 'reporte/humedales/ElRetiro.html', {'title': 'ElRetiro'})
def EcoparqueLasGarzas(request):
    return render(request, 'reporte/humedales/EcoparqueLasGarzas.html', {'title': 'EcoparqueLasGarzas'})
>>>>>>> 5752ea43f40a6c0470a69916c429a8a7c275278e

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

<<<<<<< HEAD
=======
def registrate(request):
    return render(request, 'reporte/registrate.html', {'title': 'registrate'})
def videos(request):
    return render(request, 'reporte/recursos/videos.html', {'title': 'videos'})
def quejas(request):
    return render(request, 'reporte/quejas.html', {'title': 'quejas'})
>>>>>>> 5752ea43f40a6c0470a69916c429a8a7c275278e

def hacer_reporte(request):
    return render(request, 'reporte/hacer_reporte.html', {'title': 'About'})

<<<<<<< HEAD
def registro(request):
    return render(request, 'reporte/registrate.html', {'title': 'About'})


def login1(request):
    return render(request, 'reporte/login1.html', {'title': 'About'})


def blog(request):
    return render(request, 'reporte/blog.html', {'title': 'About'})
    
#@login_required
#def user(request):
#    return render(request, 'reporte/user.html', {'title': 'About'})

def misreportes(request):
    return render(request, 'reporte/mis_reportes.html', {'title': 'About'})  
=======
def gestionarBlog(request):
    return render(request, 'reporte/administrador/gestionarBlog.html', {'title': 'Gestionar Blog'})

def gestionarReportes(request):
    return render(request, 'reporte/administrador/gestionarReportes.html', {'title': 'Gestionar Reportes'})

def gestionarUsuarios(request):
    return render(request, 'reporte/administrador/gestionarUsuarios.html', {'title': 'Gestionar Usuarios'})
>>>>>>> 5752ea43f40a6c0470a69916c429a8a7c275278e
