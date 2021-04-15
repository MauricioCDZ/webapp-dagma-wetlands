from django.shortcuts import render, get_object_or_404
from .models import *
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
import json
import urllib
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
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

        if form.is_valid():
            recaptcha_response = self.request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            if result['success']:
                form.save()
                messages.success(self.request, 'New comment added with success!')
            else:
                messages.error(self.request, 'Invalid reCAPTCHA. Please try again.')
            return redirect('reporte-create')


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

def involucrate(request):
    return render(request, 'reporte/involucrate.html', {'title': 'Involucrate'})
def nuestraHistoria(request):
    return render(request, 'reporte/nuestraHistoria.html', {'title': 'About'})
def LaBabilla(request):
    humedal = Humedal.objects.get(nombre= "La Babilla")
    return render(request, 'reporte/humedales/LaBabilla.html', {'title': 'LaBabilla', 'humedal' : humedal})
def ElRetiro(request):
    return render(request, 'reporte/humedales/ElRetiro.html', {'title': 'ElRetiro'})
def EcoparqueLasGarzas(request):
    return render(request, 'reporte/humedales/EcoparqueLasGarzas.html', {'title': 'EcoparqueLasGarzas'})

def babilla_flora(request):
    return render(request, 'reporte/humedales/galeria_flora.html', {'title': 'About'})

def babilla_fauna(request):
    humedal = Humedal.objects.get(nombre= "La Babilla")
    return render(request, 'reporte/humedales/galeria_fauna_terrestre.html', {'title': 'About', 'humedal': humedal})
def babilla_acuatica(request):
    return render(request, 'reporte/humedales/galeria_fauna_acuatica.html', {'title': 'About'})

def planes_manejo(request):
    return render(request, 'reporte/recursos/planes_manejo.html', {'title': 'About'})

def programas(request):
    return render(request, 'reporte/recursos/programas.html', {'title': 'About'})

def videos(request):
    return render(request, 'reporte/recursos/videos.html', {'title': 'videos'})
def registrate(request):
    return render(request, 'reporte/registrate.html', {'title': 'registrate'})
def quejas(request):
    return render(request, 'reporte/quejas.html', {'title': 'quejas'})

def hacer_reporte(request):
    return render(request, 'reporte/hacer_reporte.html', {'title': 'About'})

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
def gestionarBlog(request):
    reportes= Reporte.objects.all()
    return render(request, 'reporte/administrador/gestionarBlog.html', {'title': 'Gestionar Blog', 'reportes': reportes})

def gestionarReportes(request):
    return render(request, 'reporte/administrador/gestionarReportes.html', {'title': 'Gestionar Reportes'})

def gestionarUsuarios(request):
    return render(request, 'reporte/administrador/gestionarUsuarios.html', {'title': 'Gestionar Usuarios'})
