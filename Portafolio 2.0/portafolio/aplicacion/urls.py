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
          #logeandose terminandose----------------------------------------------------
    path(
        'reserva/',
         views.CrearReservaView.as_view(),
         name='reservando'), 
    path(
        'contacto/',
         views.ContactCreateView.as_view(),
         name='addcontacto'), 
    path(
        'funcionario/',
         views.FuncionarioView.as_view()
         ), 
    path(
        'perfil_funcionario/',
         views.PerfilFuncionarioView.as_view(),
         name='perfil_funcionario'
         ), 
    path(
        'crear_listado/',
         views.CrearlistadoView.as_view()
         ), 
        #Mantener Cliente-------------------------------------------------------------------------------------------------------------------------------------------------
    path(
        'mantener_cliente/',
         views.MantenerClienteView.as_view(),
         name='mantener_cliente'
         ), 
    path(
        'actualizaruser/<pk>/',
         views.ClienteUpdateView.as_view(),
         name='actualizaruser'
         ), 
     path(
         'deleteuser/<pk>/',
         views.UsuarioDeleteView.as_view(),
         name='deleteuser'
        ), 
        #Mantener Departamento-------------------------------------------------------------------------------------------------------------------------------------------------
    path(
        'mantener_departamento/',
         views.MantenerDepartamentoView.as_view(),
         name='mantener_departamento'
         ), 
    path(
        'deletedepartamento/<pk>/',
         views.DepartamentoDeleteView.as_view(),
         name='deletedepartamento'
         ),
    path(
        'actualizardepartamento/<pk>/',
         views.DepartamentoUpdateView.as_view(),
         name='actualizardepartamento'
         ), 
        #Mantener Reservas-------------------------------------------------------------------------------------------------------------------------------------------------
    path(
        'mantener_reserva/',
         views.MantenerReservaView.as_view(),
         name='mantener_reserva'
         ),
    path(
        'actualizarreserva/<pk>/',
         views.ActualizarReservaUpdateView.as_view(),
         name='actualizarreserva'
         ),
    path(
        'deletereserva/<pk>/',
         views.ReservaAdminDeleteView.as_view(),
         name='deletereserva'
         ), 
        #Mantener Servicios--------------------------------------------------------------------------------------------------------------------------------------------------
    path(
        'mantener_servicio/',
         views.MantenerServicioView.as_view(),
         name='mantener_servicio'
         ),
    path(
        'actualizarservicio/<pk>/',
         views.ServicioUpdateView.as_view(),
         name='actualizarservicio'
         ),
    path(
        'deleteservicio/<pk>/',
         views.ServicioAdminDeleteView.as_view(),
         name='deleteservicio'
         ), 
        #Mantener Tour--------------------------------------------------------------------------------------------------------------------------------------------------
    path(
        'mantener_tour/',
         views.TourView.as_view(),
         name='mantener_tour'
         ),
    path(
        'actualizartour/<pk>/',
         views.TourUpdateView.as_view(),
         name='actualizartour'
         ),
    path(
        'deletetour/<pk>/',
         views.TourDeleteView.as_view(),
         name='deletetour'
         ), 
        #Pago--------------------------------------------------------------------------------------------------------------------------------------------------------------
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
        'lista_acompañante/',
         views.ListAcompañante.as_view(),
          name='listadoacompañante'), 
    path(
        'registroacom/',
         views.CrearAcompañanteView.as_view(),
          name='registroacom'
          ), 
     path(
         'editacom/<pk>/',
          views.AcompañanteUpdateView.as_view(),
           name='editacom'
           ), 
     path(
         'deleteacomp/<pk>/',
          views.AcompañanteDelete.as_view(),
           name='deleteacomp'
           ), 
     path(
         'cancelarreserva/<pk>/',
          views.ReservaDelete.as_view(),
           name='cancelarreserva'
           ), 
     path(
        'mantener_servicios/',
         views.ServiciosView.as_view(),
          name='mantener_servicios'
          ), 
     path(
        'generar_estadistica/',
         views.EstadisticaView.as_view(),
          name='generar_estadistica'
          ), 
     path(
        'generar_informe/',
         views.InformeView.as_view(),
          name='generar_informe'
          ), 
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



