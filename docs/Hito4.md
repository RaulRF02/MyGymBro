# **Hito 4**

## Composición de servicios

En este hito, se ha diseñado e implementado un sistema de servicios utilizando Docker y Docker Compose para orquestar y 
desplegar la aplicación de backend y su base de datos SQLite. Este sistema permite un despliegue consistente y 
reproducible en diferentes entornos, cumpliendo con los principios de configuración-como-código y modularidad.

## Decisiones y Soluciones Implementadas

### 1. Creación de un contenedor con la aplicación

- **Problema:** Asegurar que la aplicación desarrollada en hitos anteriores sea ejecutable en un entorno aislado y consistente.
- **Solución:** 
  - Crear un Dockerfile basado en la imagen oficial de Python python:3.12-slim.
  - Incluir las dependencias necesarias (librerías de Python y herramientas como gunicorn) para ejecutar la aplicación.
  - La aplicación se ejecuta con Gunicorn, lo que asegura un servidor WSGI escalable y adecuado para producción.
  - La estructura del Dockerfile sigue las mejores prácticas, como el uso de una imagen base ligera y la eliminación de 
  dependencias innecesarias tras la instalación.

### 2. Uso de contenedores de datos (volúmenes)

- **Problema:** Asegurar la persistencia de datos en SQLite incluso tras reiniciar los contenedores.
- **Solución:** 
  - Se configuró un contenedor dedicado a SQLite y se vinculó a un volumen persistente llamado app_data.
  - Este enfoque desacopla los datos del contenedor de la aplicación, lo que facilita el mantenimiento y migración de 
  los datos.

### 3. Configuración del clúster

- **Problema:** Garantizar que los servicios (app y base de datos) puedan comunicarse correctamente.
- **Solución:** 
  - Usamos una red predeterminada en Docker Compose para que los servicios compartan un espacio de red.
  - La variable de entorno DATABASE_URL en .env apunta a la base de datos SQLite en el contenedor sqlite.

### 4. Configuración-como-código
- **Problema:**  Garantizar que la infraestructura sea reproducible y funcione en cualquier entorno.
- **Solución:** 
  - Usar variables de entorno almacenadas en archivos .env.dev y .env.prod para gestionar configuraciones 
  específicas de cada entorno.
  - Esto permite cambiar el entorno (desarrollo o producción) simplemente especificando el archivo de entorno en el 
  comando docker-compose.

#### Ejemplo de uso en desarrollo:

```
docker compose --env-file .env.dev up --build
```

#### Ejemplo de uso en producción:
```
docker compose --env-file .env.prod up --build
```