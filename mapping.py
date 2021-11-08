# Hojas del formulario

sheets = {
    'usuarios': 'Usuarios',
    'productos': 'Productos',
    'puntos': 'Puntos de Venta'
}

# Tablas de la DB

TABLA_USUARIOS ='usuarios.usuario'
TABLA_PRODUCTOS = 'facturador.productos'
TABLA_PUNTOS = 'facturador.puntosventa'
TABLA_OPERADORES = 'facturador.operadores'

# Password genérica para los nuevos usuarios
PASSWORD = 'YWFiOGY3YTAzMjZjMGI2Y2NmZWM2YWVhYjk5MzAwNGYyMzkyMWFiMw==' #Cambiame123+

# para los siguientes esquemas el formato es [<Campo de la Tabla>] = <# Columna Excel>

# Campos de Usuario
usuario_xls ={}
usuario_xls['nombre'] = 1
usuario_xls['apellido'] = 2
usuario_xls['email'] = 3
usuario_xls['puntos_venta'] = 4

# campos de producto
producto_xls = {}
producto_xls['codigo'] = 1
producto_xls['descripcion'] = 2
producto_xls['comentarios'] = 3
producto_xls['unidadmedida_codigo'] = 4
producto_xls['precio'] = 5
producto_xls['an8'] = 6
producto_xls['nac_int'] = 7


# campos de punto venta
puntos_xls = {}
puntos_xls['numero'] = 1
puntos_xls['descripcion'] = 2
puntos_xls['domicilio'] = 3
puntos_xls['cpostal'] = 4
puntos_xls['provincia'] = 5
puntos_xls['municipio'] = 6
puntos_xls['defensa'] = 7








