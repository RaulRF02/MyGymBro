# **Hito 1**

## Descripción del Proyecto

Este **Sistema de Planificación de Rutinas de Gimnasio** es una aplicación backend, que permite a los usuarios gestionar
y consultar rutinas de entrenamiento personalizadas. Está diseñada para entrenadores, administradores y usuarios 
finales, con distintos niveles de acceso y funcionalidades. Utiliza **Swagger** para probar los distintos endpoints de 
la API, facilitando la interacción con el sistema.

La aplicación tiene tres tipos de usuarios:
- **Administrador**: Gestor de usuarios y creador de rutinas generales accesibles a todos los usuarios.
- **Entrenador**: Creador de rutinas personalizadas para sus usuarios y monitorización del progreso de estos.
- **Usuario común**: Puede acceder a rutinas generales o personalizadas, dependiendo de si ha pagado por un entrenador.

Además esta aplicación se beneficia enormemente de estar desplegado en la nube por las siguientes razones:

- Acceso Remoto
- Escalabilidad
- Manejo de Múltiples Usuarios Simultáneamente
- Sincronización de Datos
- Seguridad y Respaldo de Datos
- Actualizaciones y Mantenimiento Simplificados

## Funcionalidades Principales
- Gestión de usuarios (alta, baja, permisos)
- Creación de rutinas generales y personalizadas
- Visualización de rutinas y progreso de entrenamiento
- Autenticación y roles (admin, entrenador, usuario)
- Uso de Swagger para probar la API

## Planificación del Proyecto

Se han creado diferentes Milestones con sus respectivos issues para facilitar la planificaión de este. Además se han 
añadido una serie de labels más explicativas y específicas para esta aplicaión.

- **Milestone 1:** Configuración Inicial y Diseño del Sistema

- **Milestone 2:** Implementación de Roles y Autenticación

- **Milestone 3:** Gestión de Rutinas y Entrenamientos

- **Milestone 4:** Integración Continua y Pruebas Automáticas

- **Milestone 5:** Despliegue en la Nube y Monitoreo

## Configuración del Repositorio

El primer paso fue crear el repositorio, eligiendo el nombre y añadiendo tanto la [licencia](/LICENSE) como el archivo 
[gitignore](/.gitignore), el cual actualmente se encuentra vacío, pues por el momento no se necesita (este archivo se 
irá actualizando a medida que avanza el poryecto).

El siguiente paso fue clonar el repositorio con la [clave SSH](https://docs.github.com/es/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
 correspondiente, la cual ya tenía generada como se muestar en la figura 1.1.

![Imagen de la configuración de claves SSH](./images/KeyConfig.jpeg)

*Figura 1.1: Configuración de claves SSH*

Para el desarrollo del proyecto se debe clonar primero el repositorio usando el comando:

```bash
git clone git@github.com:tu_usuario/MyGymBro.git
```

