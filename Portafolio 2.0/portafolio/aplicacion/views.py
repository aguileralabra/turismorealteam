from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.db import connection
from .models import *
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View, TemplateView, ListView, CreateView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic import (CreateView)
from .forms import AcompañanteForm, UserRegisterForm, LoginForm, UpdatePasswordForm, VerificationForm, ContactForm, ReservaForm, DepartamentoForm
from django.views.generic.edit import (FormView)
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .functions import code_generator, render_to_pdf
from django.core.mail import send_mail
from django.template import context



class InicioView(TemplateView):
    template_name = "index.html"


'''

Login---------------------------------------------------------

'''
class UserRegisterView(FormView):
    template_name = 'register.html'
    form_class = UserRegisterForm
    success_url =  reverse_lazy('cliente_app:logeo')

    def form_valid(self, form):
        #generamos codigo
        codigo = code_generator()

        usuario = User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['cli_Rut'],
            form.cleaned_data['password1'],
            cli_Nombre=form.cleaned_data['cli_Nombre'],
            cli_Apellidos=form.cleaned_data['cli_Apellidos'],
            cli_Edad=form.cleaned_data['cli_Edad'],
            cli_Nacionalidad=form.cleaned_data['cli_Nacionalidad'],
            email=form.cleaned_data['email'],
            cli_Telefono=form.cleaned_data['cli_Telefono'],
            codregistro=codigo
        )
        #enviar el codigo al email del user
        asunto = 'Confirmacion de Email'
        mensaje = 'Codigo de Verificacion: ' + codigo
        email_remitente = 'aguilerajordan2@gmail.com'
        send_mail(asunto, mensaje, email_remitente, [form.cleaned_data['email'],])
        #redirigir a pantalla de validacion
        return HttpResponseRedirect(
            reverse(
                'cliente_app:verification-user',
                kwargs={'pk': usuario.id}
            )
        )


class LoginUser(FormView):
    template_name = "registration/login.html"
    form_class = LoginForm
    success_url =  reverse_lazy('cliente_app:inicio')

    def form_valid(self, form):
        user = authenticate(
            username= form.cleaned_data['username'],
            password= form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)

class LogoutView(View):
    
    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'cliente_app:logeo'
            )
        )

class UpdatePasswordView(FormView):
    template_name = 'update.html'
    form_class = UpdatePasswordForm
    success_url =  reverse_lazy('cliente_app:logeo')

    def form_valid(self, form):
        usuario = self.request.user
        user = authenticate(
            username=usuario.username,
            password=form.cleaned_data['password1']
        )

        if user:
            new_password = form.cleaned_data['password2']
            usuario.set_password(new_password)
            usuario.save()

        logout(self.request)

        return super(UpdatePasswordView, self).form_valid(form)

class CodeVerificationView(FormView):

    template_name = "verification.html"
    form_class = VerificationForm
    success_url =  reverse_lazy('cliente_app:logeo')

    def get_form_kwargs(self):
        kwargs = super(CodeVerificationView, self).get_form_kwargs()
        kwargs.update({
            'pk': self.kwargs['pk']
        })
        return kwargs

    def form_valid(self, form):
        User.objects.filter(
            id=self.kwargs['pk']
        ).update(
            is_active=True
        )
        return super(CodeVerificationView, self).form_valid(form)

class RecuperarContraseñaView(TemplateView):
    template_name = "recuperarcontraseña.html"


'''

Aqui terminar login---------------------------------------------------------

'''
'''

Cliente------------------------------------------------------

'''
#listando las tarjetas de credito
''' TEMPLATEVIEW-------------------------------------------- '''


class InicioclienteView(LoginRequiredMixin, TemplateView):
    template_name = "inicio.html"
    login_url = reverse_lazy('cliente_app:logeo')


''' ----------------------------LISTVIEW--------------------- '''

class ListCliente(LoginRequiredMixin, ListView):
    template_name = 'cliente.html'
    model = Reserva
    context_object_name = 'reservita'
    login_url = reverse_lazy('cliente_app:logeo')

 #   def get_queryset(self):
  #      #identificar cliente
   #     id = self.kwargs['pk']
    #    #filtrar tarjetas
     #   lista = TarjetaCredito.objects.filter(
      #      clientes=id
       # )
        #devolver resultado
        #return lista

class ListPerfil(LoginRequiredMixin, TemplateView):
    template_name = 'perfil.html'
    login_url = reverse_lazy('cliente_app:logeo')


class ListAcompañante(LoginRequiredMixin, ListView):
    template_name = 'lista_acompañante.html'
    model = Acompañante
    context_object_name = 'acompañante'
    login_url = reverse_lazy('cliente_app:logeo')

class ListReservaListView(LoginRequiredMixin, ListView):
    template_name = 'informepdf.html'
    model = Reserva
    paginate_by = 1
    context_object_name = 'reservitapdf'
    login_url = reverse_lazy('cliente_app:logeo')
    

class ListReservaPdf( View):

    def get(self, request, *args, **kwargs):
        reservitapdf = Reserva.objects.all()
        data = {
            'reservitapdf' : reservitapdf
        }
        pdf = render_to_pdf('listareserva.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

    def get_queryset(self):
        #identificar cliente
        id = self.kwargs['pk']
        #filtrar tarjetas
        reservitapdf = Reserva.objects.filter(
            user=id
        )
        #devolver resultado
        return reservitapdf

''' ----------------------------DETAILVIEW-------------------'''

#class TarjetaDetailView(LoginRequiredMixin, DetailView):
 #   model = TarjetaCredito
  #  template_name = "detail_tarjeta.html"
   # login_url = reverse_lazy('cliente_app:logeo')

''' -----------------------------CreateVIEW-------------------- '''

class ContactCreateView(LoginRequiredMixin, CreateView):
    template_name = "contacto.html"
    form_class = ContactForm
    success_url = '.'
    login_url = reverse_lazy('cliente_app:logeo')


class CrearAcompañanteView(LoginRequiredMixin, CreateView):
    template_name = "registroacom.html"
    model = Acompañante
    form_class = AcompañanteForm
    success_url =  reverse_lazy('cliente_app:listadoacompañante')
    login_url = reverse_lazy('cliente_app:logeo')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(CrearAcompañanteView, self).form_valid(form)

class CrearReservaView(LoginRequiredMixin, CreateView):
    template_name = "reserva.html"
    model = Reserva
    form_class = ReservaForm
    success_url =  reverse_lazy('cliente_app:informepdf')
    login_url = reverse_lazy('cliente_app:logeo')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(CrearReservaView, self).form_valid(form)


''' -----------------------------UPDATEVIEW--------------------- '''

class AcompañanteUpdate(LoginRequiredMixin, UpdateView):
    template_name = "editacom.html"
    model = Acompañante
    fields = ('__all__')
    success_url =  reverse_lazy('cliente_app:listadoacompañante')
    login_url = reverse_lazy('cliente_app:logeo')

''' -----------------------------DELETEVIEW--------------------- '''

class AcompañanteDelete(LoginRequiredMixin, DeleteView):
    template_name = "deleteacomp.html"
    model = Acompañante
    success_url =  reverse_lazy('cliente_app:listadoacompañante')
    login_url = reverse_lazy('cliente_app:logeo')

class ReservaDelete(LoginRequiredMixin, DeleteView):
    template_name = "cancelarreserva.html"
    model = Reserva
    success_url =  reverse_lazy('cliente_app:cliente')
    login_url = reverse_lazy('cliente_app:logeo')

'''

termina aqui Cliente------------------------------------------------------

'''

'''

Empieza Funcionario------------------------------------------------------

'''


class FuncionarioView(LoginRequiredMixin,TemplateView):
    template_name = 'funcionario.html'
    login_url = reverse_lazy('cliente_app:logeo')

class PerfilFuncionarioView(LoginRequiredMixin,TemplateView):
    template_name = 'perfil_funcionario.html'
    login_url = reverse_lazy('cliente_app:logeo')

class CrearlistadoView(LoginRequiredMixin,TemplateView):
    template_name = 'crear_listado.html'
    login_url = reverse_lazy('cliente_app:logeo')

'''

termina aqui Funcionario------------------------------------------------------

'''
'''

Empieza Administrador------------------------------------------------------

'''

class MantenerClienteView(LoginRequiredMixin, View):
    model = User
    form_class = UserRegisterForm
    template_name = 'mantener_cliente.html'
    login_url = reverse_lazy('cliente_app:logeo')

    def get_queryset(self):
        return self.model.objects.filter(is_staff = False)

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto['usuario'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return redirect('cliente_app:mantener_cliente')

class UsuarioUpdate(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserRegisterForm
    template_name = "mantener_cliente.html"
    success_url =  reverse_lazy('cliente_app:mantener_cliente')
    login_url = reverse_lazy('cliente_app:logeo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usuario'] = User.objects.filter(is_staff = False)
        return context

class UsuarioDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "deleteuser.html"
    model = User
    success_url =  reverse_lazy('cliente_app:mantener_cliente')
    login_url = reverse_lazy('cliente_app:logeo')

'''hasta aqui mantenedor cliente ------------------------------------------------------'''

class MantenerDepartamentoView(LoginRequiredMixin,View):
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'mantener_departamento.html'
    login_url = reverse_lazy('cliente_app:logeo')

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name, self.get_context_data())

class PagosView(LoginRequiredMixin,TemplateView):
    template_name = 'pagos_adm.html'
    login_url = reverse_lazy('cliente_app:logeo')

class ServiciosView(LoginRequiredMixin,TemplateView):
    template_name = 'mantener_servicios.html'
    login_url = reverse_lazy('cliente_app:logeo')

class EstadisticaView(LoginRequiredMixin, TemplateView):
    template_name = 'generar_estadistica.html'
    login_url = reverse_lazy('cliente_app:logeo')

class InformeView(LoginRequiredMixin,TemplateView):
    template_name = 'generar_informe.html'
    login_url = reverse_lazy('cliente_app:logeo')

'''

termina aqui Administrador------------------------------------------------------

'''

def resultado(request):
    return render (request, 'resultado.html')
