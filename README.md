# 🏋️‍♂️ **MyGymBro** 🏋️‍♂️

## Descripción del Proyecto

Este **Sistema de Planificación de Rutinas de Gimnasio** es una plataforma diseñada para ofrecer a entrenadores y 
usuarios una herramienta flexible y accesible para crear, gestionar y hacer seguimiento de rutinas personalizadas de 
entrenamiento. El sistema está pensado tanto para entrenadores, que deben gestionar múltiples clientes, como para 
usuarios individuales que deseen un seguimiento personalizado de su progreso físico.

### 🎯 **Objetivo Principal**
El objetivo de esta aplicación es proporcionar una solución integral para la planificación y seguimiento de 
entrenamientos físicos, permitiendo a los usuarios alcanzar sus metas de forma eficiente, ya sea perder peso, 
ganar masa muscular o mejorar su salud en general.

---

## 🚀 **Características Principales**

### **Gestión de Rutinas Personalizadas**
Los entrenadores pueden diseñar rutinas a medida, basadas en los objetivos individuales de cada cliente:
- Pérdida de peso.
- Aumento de masa muscular.
- Tonificación.
  
Los usuarios pueden:
- Seleccionar rutinas predefinidas.
- Recibir sugerencias automáticas basadas en sus objetivos y condición física.

### **📊 Seguimiento de Progreso**
Los usuarios registran detalles sobre sus entrenamientos, como:
- Series, repeticiones y peso utilizado.
- Comentarios sobre el rendimiento.

---

## 📂 Documentación del proyecto

Para seguir la documentación del proyecto existe la carpeta [docs](docs), en la cual se llevará a cabo la 
documentación de este.

En el [Hito 1](docs/Hito1.md) se podrá encontar más información acerca de la configuración de GitHub y los 
pasos iniciales del proyecto

En el [Hito 2](docs/Hito2.md)  se puede encontrar toda la información relacionada con el gestor de tareas del proyecto, 
así como la creación de los primeros tests y la configuración de la pipeline.

---

## **⚙️ Instrucciones**
### Instalación del Proyecto

Asegúrate de tener Poetry instalado. Si no lo tienes, puedes instalarlo con:

``` bash
curl -sSL https://install.python-poetry.org | python3 -
```
Luego, clona este repositorio y navega al directorio del proyecto:

``` bash
git clone https://github.com/tu-usuario/mygymbro.git
cd mygymbro
```

Instala las dependencias:

``` bash
poetry install
```

---

## 🛠️ Órdenes Disponibles

Para iniciar la aplicación:

``` bash
poetry run python wsgi.py
```

Para ejecutar todos los tests:

``` bash
poetry run pytest
```

Para formatear el código con Black:

``` bash
poetry run black .
```

---

## 📄 **Licencia**
Este proyecto está bajo la licencia MIT. Para más información, revisa el archivo [LICENSE](LICENSE).
