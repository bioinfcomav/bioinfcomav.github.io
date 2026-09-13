
Iniciación a Ubuntu
===================

`Ubuntu <http://www.ubuntu.com/>`_ es una distribución Linux orientada al usuario de escritorio, con el objetivo de ser muy fácil de utilizar y gratuita.
Aunque el escritorio es algo distinto al de Windows o Mac OS X familiarizarse con él para un usuario acostumbrado a cualquiera de los otros sistemas operativos no debe presentar ningún problema.
Su instalación, aunque no vamos explicarla aquí, también resulta extraordinariamente sencilla.

Existen numerosos manuales de utilización de Ubuntu, pero uno de las guías más completas es la `Getting started with ubuntu <http://ubuntu-manual.org/>`_
Vamos a recorrer lo principales conceptos de este sistema operativo basandonos en este :download:`manual <../bibliography/getting_started_with_ubuntu_12_04.2ed.pdf>`


Los usuarios
------------

Los sistemas Unix son multiusuario, es decir soportan que varios usuarios los utilicen simultáneamente.
Todos los usuarios, excepto uno, tienen unos privilegios bastante restringidos y no pueden modificar el sistema.
De este modo unos usuarios se ven protegidos de las acciones de los otros.
Existe un usuario especial llamado *root* con privilegios de administración absolutos sobre el sistema.
Para realizar las tareas cotidianas nunca hay que acceder al sistema como *root*.
En Ubuntu este usuario está deshabilitado por defecto y sólo se pueden adquirir los privilegios de administrador temporalmente.

El escritorio
-------------

Todos las distribciones basadas en entronos graficos (GUI) suelen tener varios entornos de escritorio para eleguir. Los entornos de escritorio suelen diferir por:

* El estilo y apariencia del entorno
* La forma en la que los diferentes elementos se disponen en la pantalla 
* La forma en la que el ususario navega por el escritorio

En el caso de Ubuntu el entorno de escritorio por defecto se denomina Unity.
Se caracteriza por tener dos barras, la denominada Menu Bar y el Launcher.
El Menu Bar incorpora por una lado los menus de las aplicaciones que estań activas y, por otro, un area de indicadores que nos ofrecen informacion actualizada del sistema en todo momento.
El Launcher es la barra vertical que facilita el acceso a las aplicaciones mas usadas y a su estado, además de a los discos montados y a la papelera.
Además tenemos el selector de escritorios virtuales.
En el launcher encontramos varias aplicaciones especiales:

* El menu
* El selector de escritorios virtuales
* La papelera

Los escritorios virtuales sirven para ampliar la zona de trabajo.
Por defecto hay 4 escritorios virtuales que amplían nuestro monitor por cuatro.


Navegando por el sistema de ficheros
------------------------------------

Al sistema de ficheros se accede a traves del menu.
Tenemos la posibilidad de buscar en la barra de busqueda o navegar directamente por el menu.
Una vez que seleccionemos la carpeta se abrirá una ventana del navegador de ficheros con la carpeta seleccionada.
Por cierto, los términos carpeta y directorio son sinónimos, al igual que fichero y archivo.

Desde el launcher también podemos acceder a nuestra carpeta personal.
Este directorio personal y sus subdirectorios son los únicos lugares en los que podremos almacenar nuestros archivos personales.
El resto del sistema de archivos estará restringido para funciones de administración del sistema.

Ejercicios
----------

Para comprobar que no tenemos problemas de manejo del sistema vamos a realizar una serie de tareas:

* Explorar el escritorio abriendo programas, moviéndote entre escritorios virtuales, minimizando y maximizando las aplicaciones, etc.

* Navegar al directorio "Documentos" y comprobar si tenemos algún archivo guardado.

* Crear un subdirectorio llamado "curso" dentro del directorio "Documentos".

* Crear un fichero de texto mediante el editor de textos gedit y guardarlo en el directorio que acabamos de crear.

* Copiar el fichero anterior al directorio personal.

* Eliminar el fichero original.


Bibliografía
============

El excelente `Ubuntu manual <http://ubuntu-manual.org/>`_ (:download:`pdf <../bibliography/getting_started_with_ubuntu_12_04.2ed.pdf>`).

La documentación `oficial <https://help.ubuntu.com/>`_ y de la `comunidad <https://help.ubuntu.com/community>`_ de Ubuntu.

La `referencia <http://www.ubuntupocketguide.com/index_main.html>`_ de bolsillo de Ubuntu (:download:`pdf <../bibliography/ubuntupocketguide-v1-1.pdf>`).

