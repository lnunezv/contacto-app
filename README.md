# Contact App

Aplicación web fullstack para la gestión de contactos, con envío de correo real, construida con React, FastAPI y PostgreSQL, totalmente containerizada con Docker.


## Funcionalidades

- Crear contactos
- Listar contactos
- Editar contactos
- Eliminar contactos
- Guardar datos en PostgreSQL
- Enviar correo real con los datos capturados


## Arquitectura

La aplicación está compuesta por 3 servicios en Docker:

- contacts_db → Base de datos PostgreSQL
- contacts_backend → API REST con FastAPI
- contacts_frontend → Aplicación web en React


## Requisitos previos

- Docker Desktop
- Git

## Instalación y ejecución

### 1. Clonar el repositorio

git clone https://github.com/lnunezv/contacto-app.git
cd contacto-app

### 2. Crear archivo de configuración

Copiar el archivo .env.example a .env

En Git Bash:
cp .env.example .env

En PowerShell:
Copy-Item .env.example .env


### 3. Configurar variables de entorno

Editar el archivo .env y completar:

SMTP_USER
SMTP_PASSWORD
SMTP_FROM


### 4. Levantar la aplicación

docker compose up --build   (uso --build para que las imágenes se construyan desde cero y el proyecto pueda ejecutarse en cualquier entorno sin dependencias previas y mas si se ejecuta por primera vez)

### 5. Acceder a la aplicación

Frontend:
http://localhost:5173

Documentación del backend:
http://127.0.0.1:8000/docs


### 6. Uso

Desde la aplicación web puedes:

- Crear contactos
- Ver registros
- Editar registros
- Eliminar registros
- Enviar correos reales


### 7. Detener la aplicación

docker compose down

## Tecnologías utilizadas

Frontend: React + Vite  
React se utilizó para construir la interfaz de usuario como SPA.  
Vite permite un desarrollo rápido y ligero.

Backend: FastAPI  
Permite crear APIs REST de forma rápida, estructurada y eficiente.

Base de datos: PostgreSQL  
Base de datos relacional robusta para almacenamiento de datos.

Cliente HTTP: Axios  
Se utilizó para comunicar el frontend con el backend.

Envío de correos: SMTP (Gmail)  
Se implementó para cumplir el requisito de envío de correos reales.

Contenedores: Docker + Docker Compose  
Docker permite aislar cada servicio.  
Docker Compose permite levantar toda la solución con un solo comando.