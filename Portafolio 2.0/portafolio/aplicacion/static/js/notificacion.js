document.addEventListener('DOMContentLoaded', function()
{
    if(Notification.permission != "granted")
        Notification.requestPermission();
})

// funcion para llamar a una notificacion

function notificar(titulo, mensaje, url)
{
    var notificacion = new Notification(
        titulo,
        {
            icon:'static/img/logo-xd.png',
            body:mensaje,
            requireInteraction:false
        });
    notificacion.onclick = function()
    {
        window.open(url);
    }
}
//LLAMAR A LA NOTIFIACAION
setTimeout(function()
{
    var titulo = "Turismo Real";
    var mensaje = "Bienvenido";
    var url = "https://www.google.cl"
    notificar(titulo, mensaje, url);
}, 2000)