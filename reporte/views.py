from django.http import request
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
from .decorators import allowed_users
from django.core.mail import *
from django.core.mail import send_mail
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
from .filters import ReporteFilter, BlogFilter
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def home(request):
  
    return render(request, 'reporte/example.html')


#@require_http_methods(["GET"])
#def about(request):
#    context = {
#         'reportes': Reporte.objects.all()
#    }
#    return render(request, 'reporte/home.html', context)

class ReporteListView(ListView):
    model = Reporte
    template_name = 'reporte/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'reportes'
    ordering = ['-fecha_reporte']   


class UserReporteListView(LoginRequiredMixin,ListView):
    model = Reporte
    template_name = 'reporte/user_reports.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'reportes'
    paginate_by = 4

    def get_queryset(self):
        
        user =  CustomUser.objects.filter(email = self.request.user).first()

        return Reporte.objects.filter(autor=user).order_by('-fecha_reporte')
        


class ReporteDetailView(DetailView):
    model = Reporte

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reporte = self.get_object()
        recents =  Reporte.objects.filter(status='Visible').order_by('-fecha_reporte')
        
        lista_labels =  json.loads(reporte.labels)
        #lista_labels =  json.dumps(reporte.labels)
        if type(lista_labels) is dict:
            lista_labels=[" "]
        else:

            lista_labels.reverse()
        context['recents'] = recents[:4]
        context['labels'] = lista_labels
        return context

class ReporteCreateView(LoginRequiredMixin, CreateView):
    model = Reporte
    fields = ['titulo', 'descripcion','image','humedal','tipoReporte']
   
   


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
                messages.success(self.request, 'Nuevo aporte subido con exito!')
            else: 
                messages.error(self.request,
                 'reCAPTCHA Invalido. Por favor intenta otra vez.')
            return redirect('reporte-create')


        return super().form_valid(form)
        
class ReporteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Reporte
    fields = ['titulo', 'descripcion','image','humedal','tipoReporte']


    def form_valid(self, form):
        #self.request.user
        form.instance.autor =  form.instance.autor
        return super().form_valid(form)

    def test_func(self):
        reporte = self.get_object()

        usuarios = CustomUser.objects.all()
        staff_list = []
        for user in usuarios:
            if len(user.groups.all()) != 0:
                staff_list.append(user.name)

    

        if self.request.user == reporte.autor or self.request.user.name in staff_list or self.request.user.is_staff:
            print(staff_list)
            return True
        return False


class ReporteStatusView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Reporte
    fields = ['status', 'importancia']

    def form_valid(self, form):
        form.instance.autor = form.instance.autor
        return super().form_valid(form)

    def test_func(self):
        reporte = self.get_object()


        usuarios = CustomUser.objects.all()
        staff_list = []
        for user in usuarios:
            if len(user.groups.all()) != 0:
                staff_list.append(user.name)

    

        if self.request.user == reporte.autor or self.request.user.name in staff_list:
            #print(staff_list)
            return True
        return False

        
class ReporteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Reporte
    success_url = '/'

    def test_func(self):
        reporte = self.get_object()
        if self.request.user == reporte.autor or self.request.user.is_superuser or self.request.user.is_staff:
            return True
        return False

@require_http_methods(["GET","POST"])  # Sensitive
def involucrate(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        send_mail(
            name +" "+subject,
            message+" "+email,
            email,
            ['calihumedalesurbanos@gmail.com'],
        )
        
        return render(request, 'reporte/involucrate.html', {'title': 'Involucrate'})
    else:
        return render(request, 'reporte/involucrate.html', {'title': 'Involucrate'})


@require_http_methods(["GET"])  # Sensitive        
def nuestraHistoria(request):
    return render(request, 'reporte/nuestraHistoria.html', {'title': 'About'})

@require_http_methods(["GET"])  # Sensitive
def LaBabilla(request):
    humedal = Humedal.objects.get(nombre= "La Babilla")
    return render(request, 'reporte/humedales/LaBabilla.html', {'title': 'LaBabilla','humedal':humedal})

@require_http_methods(["GET"])  # Sensitive
def ElRetiro(request):
    return render(request, 'reporte/humedales/ElRetiro.html', {'title': 'ElRetiro'})

@require_http_methods(["GET"])  # Sensitive
def EcoparqueLasGarzas(request):
    return render(request, 'reporte/humedales/EcoparqueLasGarzas.html', {'title': 'EcoparqueLasGarzas'})



####################### HUMEDAL LA BABILLA GALERIA
@require_http_methods(["GET"])  # Sensitive
def babilla_flora(request):
    humedal = Humedal.objects.get(nombre= "La Babilla")
    flora = humedal.flora.all()
    return render(request, 'reporte/humedales/galeria_flora_babilla.html', {'title': 'About','humedal': flora})
@require_http_methods(["GET"])  # Sensitive
def babilla_fauna(request):
    humedal = Humedal.objects.get(nombre= "La Babilla")
    fauna = humedal.faunaTerrestre.all()
    return render(request, 'reporte/humedales/galeria_fauna_babilla.html', {'title': 'About', 'humedal': fauna})
@require_http_methods(["GET"])  # Sensitive
def babilla_acuatica(request):
    humedal = Humedal.objects.get(nombre= "La Babilla")
    fauna_acutica = humedal.FaunaAcuatica.all()
    return render(request, 'reporte/humedales/galeria_acuatica_babilla.html', {'title': 'About','humedal': fauna_acutica})



####################### HUMEDAL LAS GARZAS GALERIA
@require_http_methods(["GET"])  # Sensitive
def garzas_flora(request):
    humedal = Humedal.objects.get(nombre= "Ecoparque Las Garzas")
    flora = humedal.flora.all()
    return render(request, 'reporte/humedales/galeria_flora_garzas.html', {'title': 'About','humedal':flora})
@require_http_methods(["GET"])  # Sensitive
def garzas_fauna(request):
    humedal = Humedal.objects.get(nombre="Ecoparque Las Garzas")
    fauna = humedal.faunaTerrestre.all()
    return render(request, 'reporte/humedales/galeria_fauna_garzas.html', {'title': 'About', 'humedal': fauna})

@require_http_methods(["GET"])  # Sensitive    
def garzas_acuatica(request):
    humedal = Humedal.objects.get(nombre= "Ecoparque Las Garzas")
    fauna_acutica = humedal.FaunaAcuatica.all()
    return render(request, 'reporte/humedales/galeria_acuatica_garzas.html', {'title': 'About','humedal':fauna_acutica})

####################### HUMEDAL EL RETIRO GALERIA
@require_http_methods(["GET"])  # Sensitive
def retiro_flora(request):
    humedal = Humedal.objects.get(nombre="El Retiro")
    flora = humedal.flora.all()
    return render(request, 'reporte/humedales/galeria_flora_retiro.html', {'title': 'About','humedal':flora})


@require_http_methods(["GET"])  # Sensitive
def retiro_fauna(request):
    humedal = Humedal.objects.get(nombre= "El Retiro")
    fauna = humedal.faunaTerrestre.all()
    return render(request, 'reporte/humedales/galeria_fauna_retiro.html', {'title': 'About', 'humedal': fauna})

@require_http_methods(["GET"])  # Sensitive    
def retiro_acuatica(request):
    humedal = Humedal.objects.get(nombre= "El Retiro")
    fauna_acutica = humedal.FaunaAcuatica.all()
    return render(request, 'reporte/humedales/galeria_acuatica_retiro.html', {'title': 'About','humedal': fauna_acutica})

#######################
@require_http_methods(["GET"])  # Sensitive
def planes_manejo(request):
    return render(request, 'reporte/recursos/planes_manejo.html', {'title': 'About'})

@require_http_methods(["GET"])  # Sensitive
def programas(request):
    return render(request, 'reporte/recursos/programas.html', {'title': 'About'})


@require_http_methods(["GET"])  # Sensitive
def videos(request):
    return render(request, 'reporte/recursos/videos.html', {'title': 'videos'})

#@require_http_methods(["GET", "POST"])  # Sensitive
#def registrate(request):
#    return render(request, 'reporte/registrate.html', {'title': 'registrate'})

@require_http_methods(["GET"])  # Sensitive
def quejas(request):
    return render(request, 'reporte/quejas.html', {'title': 'quejas'})
########################

#@require_http_methods(["GET", "POST"])  # Sensitive
#def hacer_reporte(request):
#    return render(request, 'reporte/hacer_reporte.html', {'title': 'About'})


class ReporteCreateViewInvitado(CreateView):
    model = Reporte
    fields = ['titulo', 'descripcion','image','humedal','tipoReporte']
   
   


    def form_valid(self, form):
        
        form.instance.autor = CustomUser.objects.filter(email='invitado@gmail.com').first()
        

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
                messages.success(self.request, 'Nuevo aporte subido con exito!')
            else:
                messages.error(self.request, 'Invalid reCAPTCHA. Please try again.')
            return redirect('reporte-hacer-reporte')


        return super().form_valid(form)
        

@require_http_methods(["GET"])  # Sensitive
def login1(request):
    return render(request, 'reporte/login1.html', {'title': 'About'})

@require_http_methods(["GET"])  # Sensitive
def blog(request):


    permitidos =  Reporte.objects.filter(status='Visible').order_by('importancia')

    paginator = Paginator(permitidos, 3) # Show 3 reports per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'reporte/blog.html', 
    {'title': 'About','permitidos':permitidos,'page_obj': page_obj})
    
#@login_required
#def user(request):
#    return render(request, 'reporte/user.html', {'title': 'About'})


@require_http_methods(["GET"])  # Sensitive
@allowed_users(allowed_roles=['staff','admin']) 
def gestionarBlog(request):
    
    reportes= Reporte.objects.filter(status='Visible').order_by('importancia')
    users = CustomUser.objects.all()  
    f = BlogFilter(request.GET,queryset = reportes)
    paginator = Paginator(f.qs, 3) # Show 3 reports per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
             'title': 'Gestionar Blog',
             'reportes': reportes,
             'users': users,
             'filter': f,
             'page_obj': page_obj
              
              }
    return render(request, 'reporte/administrador/gestionarBlog.html', context)



@require_http_methods(["GET"])  # Sensitive
@allowed_users(allowed_roles=['staff','admin']) 
def gestionarReportes(request):
    
    all_reports =  Reporte.objects.order_by('-fecha_reporte')
    #all_reports =  Reporte.objects.all()
    f = ReporteFilter(request.GET,queryset= all_reports)
    paginator = Paginator(f.qs, 3) # Show 3 reports per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
         'reportes':all_reports,
         'page_obj': page_obj,
         'filter': f
    }
    return render(request, 'reporte/administrador/gestionarReportes.html', context)


def count_posts_of(user):
    return Reporte.objects.filter(author=user.id).count()


@require_http_methods(["GET"])  # Sensitive
@allowed_users(allowed_roles=['staff','admin'])
def gestionarUsuarios(request):
    reportes= Reporte.objects.all()
    users = CustomUser.objects.all()
    num_reports_per_user= [0 for i in range(len(users))]
    total_reportes = len(reportes)
    if total_reportes == 0:
        total_reportes = 1

    porcentaje_reportes = [0 for i in range(len(users))]
    for i in range (len(users)):
        num_reports_per_user[i]=len(reportes.filter(autor=users[i].id))
        porcentaje_reportes[i] =  (num_reports_per_user[i]/total_reportes)*100



    return render(request, 'reporte/administrador/gestionarUsuarios.html', {'title': 'Gestionar Usuarios',
    'reportes': reportes,'users':users,'user_reports':num_reports_per_user,'porcentaje_reportes':porcentaje_reportes})


