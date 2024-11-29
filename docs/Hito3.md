# **Hito 3**

## Diseño de microservicios

En este hito, se han realizado mejoras significativas para profesionalizar el sistema y garantizar su calidad, 
cumpliendo con las exigencias de un entorno de desarrollo moderno y orientado a la producción. A continuación, se 
detallan los avances logrados:

### Sistema de Logs

Se ha implementado un sistema de registro de eventos que proporciona visibilidad sobre las operaciones críticas de la 
aplicación. Los logs se almacenan en el archivo logs/app.log, permitiendo rastrear acciones como la creación, 
actualización y eliminación de recursos. Este enfoque facilita la depuración y el monitoreo del sistema en producción, 
asegurando que los problemas puedan identificarse y resolverse de manera eficiente.

### Separación de Rutas y Servicios

Se reorganizó la estructura del código para desacoplar la lógica de negocio (servicios) de las rutas (controladores). 
Esto proporciona los siguientes beneficios:

- **Mantenibilidad:** El código es más fácil de leer, entender y modificar. 
- **Escalabilidad:** La lógica de negocio puede expandirse sin afectar la lógica de control. 
- **Reutilización:** Los servicios pueden reutilizarse en diferentes partes del sistema.

Las rutas actúan como una capa delgada que recibe solicitudes, delega la lógica a los servicios y devuelve respuestas, 
cumpliendo con las mejores prácticas de diseño de APIs.

### Pruebas Automatizadas

Actualmente existen un total de 32 pruebas automatizadas para validar todos los casos principales:

- **Casos de éxito y error:** Cobertura completa de los escenarios previstos.
- **Validaciones de seguridad:** Pruebas de roles y autenticación.
- **Lógica de negocio:** Asegurando el correcto funcionamiento de cada endpoint.

Este enfoque asegura que el sistema sea confiable y robusto, minimizando riesgos, ya que estos son los mismos tests
integrados en la  pipeline. Este proceso garantiza la calidad del desarrollo mediante.

Como se puede ver en la ejecución de la pipeline el *coverage* de los tests es de un 95%.

### Gestión de Roles y Seguridad

Se implementó un sistema de autenticación basado en JWT para garantizar la seguridad de la API:

- **Control de acceso:** Solo los usuarios autenticados pueden interactuar con los recursos protegidos.
- **Gestión de roles:** Roles específicos como admin, trainer y user son validados en cada endpoint para garantizar que los permisos sean respetados.

Este diseño asegura que las operaciones se lleven a cabo solo por usuarios autorizados, protegiendo la integridad del sistema.