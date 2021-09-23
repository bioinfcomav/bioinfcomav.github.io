
Instalando software
===================

En los sistemas Linux las `distribuciones <http://es.wikipedia.org/wiki/Distribuci%C3%B3n_Linux>`_ se encargan de preparar una gran cantidad de software para ser instalado.
Por ejemplo, cuando queremos instalar un programa de edición fotográfica como el *gimp* no es necesario ni recomendable ir a la página web de los creadores del software para descargar el software.
La distribución que estemos utilizando ya se ha encargado de buscar el software y empaquetarlo para que el software pueda ser instalado de un modo estandarizado.
Por lo tanto si queremos instalar el *gimp* o cualquier otro programa lo que debemos hacer es utilizar las herramientas que la distribución a preparado para administrar el software que tenemos instalado en nuestro ordenador.
Por ejemplo, en Ubuntu, abriríamos la aplicación llamada *Software center* y en ella buscaríamos el *gimp*.
Con un solo *click* el programa quedaría instalado e integrado en nuestro sistema.

Además todo el software instalado por este método se actualiza cuando los desarrolladores del software corrigen fallos o problemas de seguridad sin que nosotros debamos preocuparnos por ello.
La propia distribución se encarga de recopilar esas mejoras y de aplicarlas a todo el software que tengamos instalado.

El modo de operación es bastante distinto al usual en *Windows*.
En *Windows* seríamos nosotros los que compraríamos el software y lo instalaríamos a partir de un CD o de un archivo descargado desde la web.
Esta es, dicho sea de paso, una de las fuentes de virus y troyanos más habitual.
Mientras que las distribuciones Linux facilitan la instalación de un software certificado y libre de virus en *Windows* debemos ser nosotros quienes nos encarguemos de verificar que el software está libre de virus.
Seríamos nosotros también los encargados de estar al tanto de instalar las actualizaciones o los fallos de seguridad a no ser que cada software implemente esta funcionalidad.

En los manuales: :download:`Getting Started with Ubuntu <../bibliography/getting_started_with_ubuntu_12_04.2ed.pdf>` y :download:`Ubuntu Pocket Guide <../bibliography/ubuntupocketguide-v1-1.pdf>` hay una explicación bastante completa sobre qué es una paquete, un repositorio y sobre qué herramientas podemos utilizar en el escritorio y en la línea de comandos para administrar el software por lo que en esta introducción no profundizaremos en estos temas.

Por desgracia, la cantidad de software incluido en las distribuciones no es infinito y, aunque el catálogo es amplio y más que suficiente para la gran mayoría de las aplicaciones que un usuario doméstico o de la administración pueda necesitar, hay programas, especialmente los hechos para campos específicos que no están incluidos en las distribuciones.
Para biología Debian y Ubuntu incluyen programas como el EMBOSS, el Blast o Biopython, pero hay otros muchos que no se incluyen y que tendremos que gestionar nosotros mismos.


Estándar de jerarquía del sistema de archivos
---------------------------------------------

Antes de instalar software no administrado por nuestra distribución conviene que tengamos una idea de como se organiza el sistema de archivos en Linux para que entendamos dónde se instala el software.
Linux sigue una norma estándar llamada `Estándar de jerarquía del sistema de archivos <http://es.wikipedia.org/wiki/Filesystem_Hierarchy_Standard>`_ que define los directorios del sistema y la localización de los distintos tipos de archivos.

En Unix todos los archivos y directorios aparecen bajo el directorio raíz (/).
Es habitual que dentro del directorio raíz existen tres jerarquías en las que se distribuyen los archivos y directorios de los programas:

 * /, *jerarquía primaria*. De ella cuelgan el resto de jerarquías. Los archivos incluidos directamente en esta jerarquía son sólo los esenciales para el sistema, como por ejemplo los comandos: *cp*, *ls* o *mkdir*.
 * /usr/, *jerarquía secundaria*. Contiene la mayoría de aplicaciones del sistema. En las distribuciones Linux es la jerarquía en las que los programas de uso común son instalados, como por ejemplo el LibreOffice o el entorno de usuario Gnome.
 * /usr/local/, *jerarquía terciaria*. Contiene la mayoría de las aplicaciones que instalamos sin la mediación de la distribución.

Dentro de cada una de las jerarquías hay varios directorios en los que se distribuyen los archivos de las aplicaciones dependiendo del tipo de archivo.
Por ejemplo, los ejecutables se encuentran en los directorios *bin* y las librerías en *lib*.
En mi ordenador el ejecutable *cp*, que es esencial para el sistema se encuentra en */bin/cp*, el editor de textos *gedit* que ha sido instalado por la distribución y no es esencial para el sistema se encuentra en */usr/bin/gedit* y el alineador de secuencias *bwa* que yo he instalado manualmente sin utilizar el gestor de paquetes se encuentra en */usr/local/bin/bwa*.

A diferencia de otros sistemas operativos en los sistemas Linux las aplicaciones normalmente no están contenidas en un sólo directorio.
Los ejecutables están en *bin*, las librerías de los que dependen en *lib*, etc.
Cuando se instalan programas estáticos, que incluyen todas sus librerías, suelen instalarse en */opt/*.
*opt/* sigue un modelo similar al *Archivos de programa* de *Windows*.
No es muy común que los programas se instalen de esta forma en *Linux*, pero algunos programas como el *IDE java eclipse* sí suelen instalarse en /opt


Instalando programas compilados
-------------------------------

Una vez hemos visto dónde debemos instalar los programas que administremos sin la ayuda de la distribución (en */usr/local*) vamos a ver como instalaríamos el mapeador de secuencias cortas `bowtie <http://bowtie-bio.sourceforge.net/>`_.
En su página de `descargas <http://sourceforge.net/projects/bowtie-bio/files/>`_ encontramos los ficheros:

 * bowtie-0.12.7-macos-10.5-x86_64.zip
 * bowtie-0.12.7-macos-10.5-x86-i386.zip
 * bowtie-0.12.7-win32.zip
 * bowtie-0.12.7-linux-x86_64.zip
 * bowtie-0.12.7-linux-i386.zip
 * bowtie-0.12.7-src.zip

Los ficheros de interés en un sistema Linux son los marcados como linux-x86_64, linux-i386 y src.
Los dos primeros incluyen el programa compilado y el tercero el código fuente listo para compilar.
Normalmente si se nos ofrece el programa precompilado para nuestra arquitectura podemos simplemente copiar el programa a */usr/local*.
En este caso el programa lo han precompilado para dos arquitecturas: x86_64 y i386.
x86_64 se refiere a los microprocesadores *Intel* y *AMD* de 64 bits e i386 a los de 32 bits.
Esta arquitectura no tiene que coincidir con nuestro procesador sino con la versión de la distribución que tenemos instalada.
Por ejemplo, Ubuntu y Debian tienen versiones para 32 y 64 bits, pero en un ordenador con un microprocesador de 64 bits podemos optar por instalar la versión de la distribución de 32 bits.
La arquitectura del programa compilado debe coincidir con la de la distribución que tengamos instalada, no con la de nuestro microprocesador.

Instalando un precompilado
__________________________

Supongamos que queremos instalar la versión de 64 bits del programa precompilado.
Una vez que hemos descargado el fichero zip (que en muchas ocasiones será en realidad un tar.gz), lo descomprimimos.
En el directorio descomprimido encontramos los ejecutables, en este caso el *bowtie* y otros archivos adicionales, en este caso *scrips* en el directorio *scripts* y ficheros de ejemplos en los directorios *indexes*, *genomes* y *reads*.
Es posible que entre todos estos ficheros haya un *README* o un *INSTALL* si es así debemos leerlos antes de continuar.

La forma más sencilla de instalar el programa es mover el directorio completo a */usr/local/bowtie/*.
Una vez hecho deberemos añadir los directorios en los que hay ejecutables a nuestro $PATH.
Sino lo hacemos no podremos ejecutar el programa a no ser que incluyamos la ruta completa al ejecutables */usr/local/bowtie/bowtie*.

Para incluir el directorio con los ejecutables en la variable *$PATH* debemos modificar la variable con la siguiente orden::

  $ export PATH=$PATH:/usr/local/bowtie/:/usr/local/bowtie/scripts/

Una vez ejecutada esta orden ya podríamos ejecutar el bowtie en la terminal.
El problema de este método es que cada vez que nos salimos de la sesión del terminal esta modificación del $PATH se pierde.
Para que el $PATH sea el que deseamos siempre que entremos al sistema el comando anterior debe ser ejecutado, esto podemos conseguirlo incluyéndolo en el fichero *.bashrc* situado en nuestra $HOME.
*.bashrc* se ejecuta automáticamente cada vez que entramos en un *shell* y se utiliza para adaptar las variables de entorno, como por ejemplo $PATH, a nuestras necesidades.

Instalando un programa desde el código fuente
_____________________________________________


Podemos optar por instalar un programa partiendo desde el código fuente, para ello debemos antes compilarlo.
Este suele ser un caso bastante habitual en las aplicaciones bioinformáticas, para los casos en los que los desarrolladores no han creado binarios compilados para nuestra arquitectura.

Normalmente los ficheros con el código fuente con ficheros comprimidos *tar.gz*, pero en el ejemplo que nos ocupa es un fichero comprimido *zip*.
Una vez descomprimido normalmente encontraremos un fichero *INSTALL* o *README* si es así debemos leerlos antes de continuar.

El caso más habitual es que entre los archivos descomprimidos haya un *shell script* ejecutable llamado *configure*.
Si es así el procedimiento a seguir suele ser ejecutar la secuencia de comandos *./configure*, *make*, *make install*.
*configure* verificará que nuestro sistema dispone de todos las librerías y utilidades necesarias para instalar el programa y creará una serie de ficheros *Makefile*.
Una vez terminado el *configure* y creados los *Makefile* satisfactoriamente podemos ejecutar el comando *make* y el programa se compilará para nuestra arquitectura.
El *configure* también suele ser el encargado de determinar en qué jerarquía del sistema de archivos se instalará el programa.
Lo habitual es que estos programas compilados manualmente se instalen en la tercera jerarquía, */usr/local/*.

Para poder compilar los programas necesitamos tener instaladas una serie de aplicaciones.
En Ubuntu por defecto estas aplicaciones no se instalan en el sistema.
Para instalarlas debemos instalar el paquete build-essential::

  $ sudo apt-get install build-essential

Este comando instalará, entre otras cosas el compilador *gcc* y los *headers* de las librerías básicas del sistema.
Los *headers* se encuentran en los paquetes *dev* (*devel* en *RedHat* y derivados) y son necesarios para poder compilar programas que requieran las librerías.
Para compilar un programa que utilice una librería no es suficiente con tener instalada la librería, necesitamos instalar el paquete *dev* con los *headers*.
Si el *configure* se queja de que alguna librería no está instalada lo más habitual es que no tengamos el correspondiente paquete *dev* instalado.

Una vez tenemos todas las librerías requeridas instaladas el compilador podrá compilar el programa cuando ejecutemos el *make*.
Este proceso debe terminar sin errores, si algo falla debemos leer la salida del *make* y buscar el fallo.
Normalmente el fallo suele deberse a la falta de alguna librería.
Si el fallo es más complicado lo más recomendable es buscar primero en *google* y si no encontramos la solución preguntar a los desarrolladores del software por el problema.

Una vez compilado soló queda ejecutar *make install* para que el software se instale.
Como lo habitual es que el programa esté destinado a ser instalado en */usr/local/* para pode ejecutar el *make install* deberemos tener privilegios de administrador.

::

  $ sudo make install

Con esto el programa debe estar listo para ser ejecutado puesto que el binario ejecutable debe haber sido copiado por el comando *make install* a algún directorio del $PATH, normalmente a */usr/local/bin*.

