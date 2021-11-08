# ABM de Facturador GCS (v1.0)

Permite tomar un archivo XLSX con un formato prefijado y toma la información de ahí para dar de alta Usurios, Produtos y Puntos de Venta.
También realiza INSERTS en la tabla Operadores de manera de asociar Usuarios con Puntos de Venta.


## Instalación de librerías


    % python3 -m pip install -r requirements.txt


## Credenciales de la base de datos

Se debe crear un archivo `credentials.py` con las credenciales de la base de datos.

Ver `credentials.py.example` 

## Modo de Uso

     main.py [-h] [-u] [-p] [-s] [ABM_file]


### Argumentos

  **ABM_file**         Toma el archivo de de entrada especificado en _[ABM_file.xlsx]_. 
  
Por defecto '_./Solicitud Facturador GCS.xlsx_'

  **-h, --help**       muestra esta ayuda

  **-u, --usuarios**   Carga de usuarios

  **-p, --productos**  Carga de productos

  **-s, --puntos**     Carga de puntos de venta

### Ejemplo

    %  python3 main.py -us 


Genera usuarios y puntos de venta en función de la información provista en el archivo de entrada './Solicitud Facturador GCS.xlsx'

Si hubiera información de productos en el archivo, se ignora.

### LOG

La ejecución del script queda registrada en el archivo '**./abm.log**'