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
