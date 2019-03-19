// Inicializar Choosen
$(".chosen-select").chosen({no_results_text: "No se encontró coincidencias con :", width: '100%' ,allow_single_deselect: true });

    var datatable = {

        "oLanguage": {
            "oAria": {
                "sSortAscending": " - ordenar de forma ascendente",
                "sSortDescending": " - ordenar de forma descendente",
                "sInfoEmpty": "No hay información para mostrar",
                "sLengthMenu": "Mostrar _MENU_ registros",
                "sSearch": "Buscar :",
                "sZeroRecords": "No hay ningún registro"

            },
            "oPaginate": {
                "sFirst": "Primera página",
                "sLast": "Última página",
                "sNext": "Página siguiente",
                "sPrevious": "Página anterior"
            },

            "sEmptyTable": "Esta tabla no tiene datos",
            "sInfo": "Mostrando  _START_ - _END_ de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando 0 entradas",
            "sInfoFiltered": "(filtrados de _MAX_  registros en total)",
            "sLengthMenu": "Motrar _MENU_ registros",
            "sSearch": "Buscar :",
            "sZeroRecords": "No se encontraron coincidencias"

        }
    };

// Traer Precio de los Productos por ajax
$(".c-producto").change(function(){
    //var s = $(this).attr("id");
    //var r = /\d+/;
    //var num = s.match(r);
    var precio,cantidad;
    $.ajax({
        url: "/almacen/obtener-producto/"+parseInt($(this).val()),
        type: "GET",
        dataType: "json",
        async: true,
        success: function (msg) {
            //precio  = "#id_formset_producto-"+ num[0]+"-precio";
            //cantidad = "#id_formset_producto-"+num[0]+"-cantidad";
            precio = "#id_precio";
            cantidad = "#id_cantidad";
            $(precio).val(msg.precio);
            $(cantidad).attr("max", msg.max_value);
        },
        error: function (xhr) {
            alert(xhr.status + ": " + xhr.responseText);
        }
    });
});


// Buscar Clientes por ajax
function search_client(){
    $.ajax({
        url: "/cliente/buscar-cliente?dni=" +  $("#BuscarCliente").val(),
        type: "GET",
        //async: true,
        success: function (msj) {
            $('#add_cliente').attr('disabled',true);
            $('#cliente_foto').html(msj['foto']);
            $('#cliente_nombre').html(msj['nombre']);
            $('#cliente_telefono').html(msj['telefono']);
            $('#cliente_email').html('<a href="'+msj['email']+'">'+msj['email']+'</a>');
        },
        error: function (xhr, errmsg, err) {
            $('#cliente_foto').html('No existe');
            $('#cliente_nombre').html('Cliente no encontrado');
            $('#cliente_telefono').html('No existe');
            $('#cliente_email').html('No existe');
            $('#add_cliente').attr('disabled',false);
        }
    });
}

//Registrar cliente via ajax
function registrar_cliente()
{
    var formulario = new FormData( $("#client-form").get(0) );
    $.ajax({
        type: $("#client-form").attr('method'), // GET or POST
        url: $("#client-form").attr('action'), // the file to call
        //data: data,
        data: formulario,
        cache: false,
        contentType: false,
        processData: false,
        //dataType: "json",
        success: function(msg){
            //Alerta
            $("#msg").html("<div class='alert alert-success'><button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button>" + msg.mensaje + "</div>");
            // Completando el DNI en el campo de busqueda
            $("#BuscarCliente").val('');
            $("#BuscarCliente").val(msg.datos.dni);
            $('#client-form')[0].reset();
            search_client();
            //Limpiando Errores de la Ventana Modal
            $("#error_id_dni").html('');
            $("#error_id_nombre").html('');
            $("#error_id_apellido").html('');
            $("#error_id_direccion").html('');
            $("#error_id_telefono").html('');
            $("#error_id_email").html('');
            $("#error_id_fecha_nacimiento").html('');
            $("#error_id_ocupacion").html('');
            $("#error_id_foto").html('');
            $("#cliente-modal").modal('hide');
        },
        error: function(error){
            $("html, #cliente-modal").animate({ scrollTop: 0 }, "slow");
            $("#msg").html("<div class='alert alert-danger'>" + error.responseJSON.mensaje + "</div>");
            //Limpiando Errores de la Ventana Modal
            $("#error_id_dni").html('');
            $("#error_id_nombre").html('');
            $("#error_id_apellido").html('');
            $("#error_id_direccion").html('');
            $("#error_id_telefono").html('');
            $("#error_id_email").html('');
            $("#error_id_fecha_nacimiento").html('');
            $("#error_id_ocupacion").html('');
            $("#error_id_foto").html('');
            //Escribir errores en el formualrio
            $("#error_id_dni").html(error.responseJSON.errores.dni );
            $("#error_id_nombre").html(error.responseJSON.errores.nombre );
            $("#error_id_apellido").html(error.responseJSON.errores.apellido );
            $("#error_id_direccion").html(error.responseJSON.errores.direccion );
            $("#error_id_telefono").html(error.responseJSON.errores.telefono );
            $("#error_id_email").html(error.responseJSON.errores.email );
            $("#error_id_fecha_nacimiento").html(error.responseJSON.errores.fecha_nacimiento );
            $("#error_id_ocupacion").html(error.responseJSON.errores.ocupacion );
            $("#error_id_foto").html(error.responseJSON.errores.foto );
        }
    });
}

function eliminar(numero,tipo){
    var elemento = document.getElementById("tr-"+numero.toString());
    elemento.parentNode.removeChild(elemento);
    //Controlando el input para el número
    if(tipo == "producto")
    {
        var numero =  parseInt($('#NumeroProductos').val());
        numero--; //contador de productos
        $('#NumeroProductos').val(numero);
        for(var i = 0; i< numero;i++)
        {
            document.getElementsByClassName("producto_nombre")[i].name = "producto-codigo-"+ (i+1).toString();
            document.getElementsByClassName("producto_nombre")[i].id = "id_producto-codigo-"+ (i+1).toString();
        }
        for(var i = 0; i< numero;i++)
        {
            document.getElementsByClassName("producto_precio")[i].name = "producto-precio-"+ (i+1).toString();
            document.getElementsByClassName("producto_precio")[i].id = "id_producto-precio-"+ (i+1).toString();
        }
        for(var i = 0; i< numero;i++)
        {
            document.getElementsByClassName("producto_cantidad")[i].name = "producto-cantidad-"+ (i+1).toString();
            document.getElementsByClassName("producto_cantidad")[i].id = "id_producto-cantidad-"+ (i+1).toString();
        }
    }
    else
    {
        var numero =  parseInt($('#NumeroLentes').val());
        numero--; //contador de productos
        $('#NumeroLentes').val(numero);
        for(var i = 0; i< numero;i++)
        {
            document.getElementsByClassName("lente_codigo")[i].name = "lente-codigo-"+ (i+1).toString();
            document.getElementsByClassName("lente_codigo")[i].id = "id_lente-codigo-"+ (i+1).toString();
        }
        for(var i = 0; i< numero;i++)
        {
            document.getElementsByClassName("lente_complementos")[i].name = "lente-complementos-"+ (i+1).toString();
            document.getElementsByClassName("lente_complementos")[i].id = "id_lente-complementos-"+ (i+1).toString();
        }
        for(var i = 0; i< numero;i++)
        {
            document.getElementsByClassName("lente_precio")[i].name = "lente-precio-"+ (i+1).toString();
            document.getElementsByClassName("lente_precio")[i].id = "id_lente-precio-"+ (i+1).toString();
        }
    }
    CalcularTotal();
}

function CalcularTotal(){
    var numero_productos = parseFloat($("#NumeroProductos").val());
    var total = 0;
    for(var x = 1;x<=numero_productos;x++)
    {
        var precio = parseFloat($("#id_producto-precio-"+x).val());
        var cantidad = parseInt($("#id_producto-cantidad-"+x).val());
        console.log(precio,cantidad);
        if( precio >= 0 && cantidad  >= 0)
        {
            total +=  (precio*cantidad)
        }
        else
        {
            total = "ERROR";
            break;
        }
    }
    var numero_lentes = parseInt( $("#NumeroLentes").val() );
    for(var i = 1 ; i<= numero_lentes; i++)
    {
        var precio = parseFloat($("#id_lente-precio-"+i).val());
        console.log(precio);
        if(precio > 0)
        {
            total += precio
        }
        else
        {
            total = "Lente Sin Precio";
            break
        }
    }
    document.getElementById("Total").textContent = total.toString();
    return total;
}