from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "cliente_app"

urlpatterns = [
    #incio index--------------------------------------------------
    path(
        '',
         views.InicioView.as_view(),
         name='index'), 
    #logeandose----------------------------------------------------
    path(
        'login/',
         views.LoginUser.as_view(),
         name='logeo'
          ), 
    path(
        'register/',
         views.UserRegisterView.as_view(),
         name='register'
          ), 
    path(
        'logout',
         views.LogoutView.as_view(),
         name='logout'
          ),
    path(
        'verification/<pk>/',
         views.CodeVerificationView.as_view(),
         name='verification-user'
          ),
    path(
        'update',
         views.UpdatePasswordView.as_view(),
         name='update'
          ),
    path(
        'cliente/',
         views.ListCliente.as_view(),
          name='cliente'
          ),
    path(
        'recuperarcontraseña',
         views.RecuperarContraseñaView.as_view(),
         name='recuperarcontraseña'
          ), 
    path(
        'resultado',
         views.resultado ,
          name='resultado'
          ), 
    path(
        'perfil/',
         views.ListPerfil.as_view(),
         name='perfil'), 
    path(
        'inicio/',
         views.InicioclienteView.as_view(),
         name='inicio'), 
         
    path(
        'resultadotarjeta/',
         views.ResultadoTarjetaView.as_view(),
          name='tarjetaingresada'
          ), 
    path(
        'reserva/',
         views.CrearReservaView.as_view(),
         name='reservando'), 
    path(
        'contacto/',
         views.ContactCreateView.as_view(),
         name='addcontacto'), 
    path(
        'administrador/',
         views.AdministradorView.as_view()
         ), 
    path(
        'funcionario/',
         views.FuncionarioView.as_view()
         ), 
    path(
        'perfil_funcionario/',
         views.PerfilFuncionarioView.as_view()
         ), 
    path(
        'crear_listado/',
         views.CrearlistadoView.as_view()
         ), 
    path(
        'mantener_cliente/',
         views.MantenerClienteView.as_view()
         ), 
    path(
        'mantener_departamento/',
         views.MantenerDepartamentoView.as_view()
         ), 
    path(
        'informepdf/',
         views.ListReservaListView.as_view(),
         name='informepdf'), 
    path(
        'lista-reserva/<pk>/',
         views.ListReservaPdf.as_view(),
         name='reserva_all'
         ), 
    path(
        'pagos_adm/',
         views.PagosView.as_view()
         ), 
    path(
        'lista_tarjeta/<pk>/',
         views.ListTarjeta.as_view(),
          name='listadotarjeta'), 
    path(
        'lista_acompañante/',
         views.ListAcompañante.as_view(),
          name='listadoacompañante'), 
    path(
        'detail_tarjeta/<pk>/',
         views.TarjetaDetailView.as_view()
         ),
    path(
        'tarjetacredito/',
         views.CrearTarjetaView.as_view()
         ),  
    path(
        'registroacom/',
         views.CrearAcompañanteView.as_view(),
          name='registroacom'
          ), 
     path(
         'edit/<pk>/',
          views.TarjetaUpdate.as_view(),
           name='edit'
           ), 
     path(
         'editacom/<pk>/',
          views.AcompañanteUpdate.as_view(),
           name='editacom'
           ), 
     path(
         'deleteacomp/<pk>/',
          views.AcompañanteDelete.as_view(),
           name='deleteacomp'
           ), 
     path(
         'deletetarjeta/<pk>/',
          views.TarjetaDelete.as_view(),
           name='deletetarjeta'
           ), 
     path(
         'cancelarreserva/<pk>/',
          views.ReservaDelete.as_view(),
           name='cancelarreserva'
           ), 
    path(
        'mantener_servicios',
         views.mantener_servicios ,
          name='mantener_servicios'
          ),
    path(
        'generar_estadistica',
         views.generar_estadistica ,
          name='generar_estadistica'
          ), 
    path(
        'generar_informe',
         views.generar_informe ,
          name='generar_informe'
          ), 
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



