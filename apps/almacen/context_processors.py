from apps.almacen.models import Producto

def stock_minimo(request):
    risk = []
    producto = Producto.objects.all()
    for item in producto:
        if(item.stock_actual <= item.stock_minimo):
            risk.append(item)
    return {'mensaje_productos':risk,'numero_mensaje':risk.__len__()}