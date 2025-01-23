# **Hito 5**

## Razones para elegir Heroku como plataforma de despliegue

Cuando se trata de desplegar aplicaciones en la nube, existen diversas plataformas como servicio (PaaS) que permiten 
gestionar la infraestructura de manera sencilla y eficiente. Entre las principales alternativas a Heroku destacan 
Render, Fly.io y Vercel, cada una con características específicas que las hacen adecuadas según las necesidades del 
proyecto. Sin embargo, tras analizar sus ventajas y desventajas, he seleccionado Heroku como la opción más 
adecuada para el despliegue de esta aplicación basada en Python y Flask.

### Análisis de alternativas

#### Render
Render es una plataforma atractiva, reconocida por su configuración sencilla a través de archivos YAML y la ausencia de 
"dormancy" en el plan gratuito, lo que asegura que las aplicaciones permanezcan activas en todo momento. Además, permite
la integración con GitHub y soporta dominios personalizados incluso en su nivel gratuito. Sin embargo, su ecosistema de 
soporte y comunidad de usuarios es aún limitado en comparación con Heroku. Esto puede dificultar la resolución de 
problemas en proyectos más complejos o personalizados.

#### Fly.io
Fly.io se orienta hacia proyectos que requieren baja latencia y despliegue en múltiples regiones geográficas, 
características ideales para aplicaciones que priorizan el rendimiento geolocalizado. A través del archivo fly.toml, 
permite configurar parámetros avanzados de infraestructura, y su integración con GitHub es bastante fluida. No obstante,
Fly.io presenta una curva de aprendizaje más pronunciada y una documentación limitada para frameworks específicos como 
Flask, lo que puede representar un desafío para desarrolladores con menos experiencia.

#### Vercel
Vercel es una solución popular para proyectos orientados al desarrollo frontend y aplicaciones serverless. Su facilidad 
de uso, combinada con la capacidad de desplegar directamente desde GitHub con configuraciones mínimas, la convierten en 
una herramienta ideal para aplicaciones ligeras. Sin embargo, dado su enfoque principal en el desarrollo frontend, 
adaptar Vercel para manejar APIs completas con Flask requiere esfuerzos adicionales, lo que la hace menos adecuada 
para este proyecto.

### Ventajas de Heroku

Heroku se destaca como la mejor opción para este proyecto debido a su equilibrio entre facilidad de uso, soporte 
robusto y compatibilidad con los requisitos técnicos del mismo. Sus principales ventajas incluyen:
- **Facilidad de uso y despliegue:** Heroku simplifica el proceso de despliegue con configuraciones mínimas, utilizando 
archivos estándar como el Procfile, runtime.txt y requirements.txt. Estas herramientas permiten definir el entorno y 
los comandos necesarios para ejecutar el proyecto sin complicaciones.
- **Integración nativa con GitHub:** La integración de Heroku con GitHub permite configurar despliegues automáticos. 
Esto significa que cualquier cambio en la rama configurada del repositorio se implementa automáticamente en la 
aplicación, reduciendo el tiempo y esfuerzo manuales.
- **Soporte para aplicaciones Flask:** Heroku ofrece una documentación extensa y específica para aplicaciones Flask, lo 
que simplifica la configuración de dependencias, el manejo del servidor y la conexión a bases de datos.
- **Infraestructura preconfigurada:** La plataforma elimina la necesidad de gestionar servidores, bases de datos y 
dependencias, proporcionando una infraestructura lista para usar. Esto ahorra tiempo y minimiza la complejidad técnica.
- **Planes gratuitos y escalabilidad:** Aunque el plan gratuito tiene limitaciones, como horas de uso restringidas y 
"dormancy" (las aplicaciones se suspenden tras un periodo de inactividad), resulta suficiente para proyectos pequeños 
o académicos. Además, Heroku ofrece un camino sencillo para escalar a planes pagos en caso de ser necesario.
- **Amplia comunidad y soporte:** Heroku cuenta con una comunidad activa, lo que facilita encontrar soluciones a 
problemas comunes. Su documentación oficial es clara y completa, ofreciendo guías detalladas para usuarios de todos 
los niveles.

Aunque existen alternativas competitivas como Render, Fly.io y Vercel, he elegido Heroku por su simplicidad, 
su robusto ecosistema de soporte y su capacidad para manejar aplicaciones Flask de manera eficiente. Su integración 
nativa con GitHub, junto con herramientas preconfiguradas que facilitan el despliegue, lo convierten en la opción ideal
a mi criterio.

## Despliegue

### Infraestructura

Para definir la infraestructura de la aplicación en Heroku y garantizar su reproducibilidad, existen varios archivos 
de configuración estándar. Entre ellos, el Procfile es fundamental, ya que indica cómo se ejecutará la aplicación en el 
entorno de producción. En este caso, contiene la línea web: gunicorn app:app, donde gunicorn es el servidor WSGI 
recomendado para aplicaciones Flask, y app:app define el archivo principal de la aplicación y su objeto Flask.

El archivo requirements.txt lista todas las dependencias necesarias para ejecutar la aplicación. Este archivo se genera
automáticamente con el comando pip freeze > requirements.txt y puede incluir dependencias como Flask, Gunicorn y 
Psycopg2 para la base de datos.

La configuración de variables de entorno es otro aspecto esencial, ya que permite manejar información sensible como 
claves secretas o credenciales de bases de datos. Estas variables pueden definirse fácilmente mediante el CLI de Heroku 
con el comando heroku config:set.

### Despliegue directo desde GitHub

Heroku permite una integración nativa con GitHub para habilitar el despliegue automático de la aplicación. Esta 
funcionalidad asegura que cualquier cambio realizado en el repositorio principal se refleje de forma inmediata en la 
versión desplegada. Para configurar esta integración, primero he vinculado la aplicación a mi repositorio de GitHub.
Esto se puede hacer desde la consola de Heroku CLI utilizando el comando heroku git:remote -a nombre-de-la-app, lo que 
establece una conexión entre el repositorio local y la aplicación en Heroku.

Una vez vinculada, es posible habilitar los despliegues automáticos desde la interfaz web de Heroku. Accediendo a la 
pestaña Deploy, se selecciona GitHub como método de integración y se vincula el repositorio correspondiente. Al activar
la opción Automatic Deploys, cualquier push realizado a la rama principal desencadenará un despliegue automático. Para 
realizar el despliegue inicial, simplemente se debe realizar un git push origin main. Heroku se encargará de construir, 
probar y desplegar la aplicación según las configuraciones definidas en los archivos del repositorio.

El estado del despliegue puede verificarse fácilmente mediante el comando heroku open, que abre la aplicación en el 
navegador, o inspeccionando los logs con heroku logs --tail.

## Aplicación desplegada

La api ya desplegada se puede encontrar en la ruta https://mygymbro-1ea8dc7c55ba.herokuapp.com/apidocs/
