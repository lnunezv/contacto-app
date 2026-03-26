# Contact App

Aplicación web de una sola página (SPA) que permite capturar datos de contacto, almacenarlos en una base de datos PostgreSQL y enviar una notificación por correo real mediante SMTP.

---

## Tecnologías utilizadas

- **Frontend:** React + Vite
- **Backend:** FastAPI (Python)
- **Base de datos:** PostgreSQL
- **Cliente HTTP:** Axios
- **Correo:** SMTP (Gmail App Password)
- **Contenedores:** Docker + Docker Compose

---

## Arquitectura

La aplicación está dividida en tres servicios:

- **Frontend:** Interfaz en React para capturar y mostrar datos
- **Backend:** API REST en FastAPI que maneja el CRUD y envío de correos
- **Base de datos:** PostgreSQL para persistencia de datos

Todos los servicios están containerizados y orquestados con Docker Compose.

---

## Funcionalidades

- Crear contactos
- Listar contactos
- Editar contactos
- Eliminar contactos
- Guardar datos en PostgreSQL
- Enviar correo real con los datos capturados

---

## Requisitos previos

- Docker Desktop instalado

---

## Configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/lnunezv/contacto-app.git
cd contacto-app