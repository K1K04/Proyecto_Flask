# Proyecto_Flask

![image](https://github.com/K1K04/Proyecto_Flask/assets/95848578/f034a8fe-8bf9-4239-81ab-8689a621f8b7)


Aplicación web para búsqueda y visualización de datos
Este proyecto consiste en la creación de una aplicación web que permite buscar y visualizar datos a partir de un archivo JSON. La aplicación incluye las siguientes características:

Hoja de estilo: Se ha incorporado una plantilla HTML/CSS para mejorar el aspecto visual de la aplicación.
Herencia de plantillas: Las plantillas utilizadas en la aplicación heredan de una plantilla base (base.html), que define la estructura común de todas las páginas.
Página principal: La página principal presenta un logotipo que al ser pulsado nos lleva a una página /xxxs.
Página de búsqueda (/xxxs): Se ha implementado un formulario de búsqueda que permite buscar XXXs por su nombre. Los datos del formulario se envían mediante el método POST a la página /xxxs.
Página de resultados (/xxxs): Esta página muestra los resultados de la búsqueda realizada en la página anterior. La tabla de resultados se genera dinámicamente a partir de los datos del archivo JSON y la búsqueda realizada.
Visualización detallada (/xxx/<identificador> o /xxx?id=xxxxxxxxxx): Se ha implementado la funcionalidad de lista-detalle, donde cada XXX de la lista tiene un enlace que lleva a una página de detalle que muestra todos los datos del XXX con el identificador correspondiente. Si el identificador no existe, se devuelve un error 404.
Despliegue en una Plataforma como Servicio (PaaS): La aplicación ha sido desplegada en una PaaS gratuita (ej. Railway, Dokku), y se ha proporcionado un proceso detallado de despliegue.
Para mejorar la aplicación y obtener más puntos, se han implementado las siguientes mejoras:

Búsqueda utilizando una sola ruta: Se ha modificado la aplicación para que la página de búsqueda y la página de resultados compartan la misma ruta (/xxxs). La información del formulario se envía a la misma página.
Recuerdo de datos de búsqueda: Se ha mejorado la experiencia del usuario haciendo que el formulario recuerde la cadena de búsqueda introducida previamente.
Añadir otro criterio de búsqueda: Se ha añadido un segundo criterio de búsqueda mediante la generación dinámica de una lista desplegable en el formulario.
Recuerdo de opción elegida en la búsqueda: Se ha programado la lista desplegable para que recuerde la opción seleccionada en búsquedas anteriores.
Estas mejoras incrementan la usabilidad y la funcionalidad de la aplicación, proporcionando una experiencia más fluida y eficiente al usuario.
