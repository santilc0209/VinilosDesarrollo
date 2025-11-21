# 🎵 PoliSongStock – Sistema de Gestión de Vinilos en Django

PoliSongStock es una aplicación web desarrollada en Django para la gestión de vinilos, proveedores y canciones.
Permite crear, listar, editar y eliminar vinilos, asociarlos con canciones y gestionar proveedores.

Este proyecto está diseñado como práctica académica.

------------------------------------------------------------

📌 Características principales
- Gestión de Vinilos (CRUD)
- Gestión de Canciones (CRUD)
- Gestión de Proveedores (CRUD)
- Relación de canciones por vinilo
- Panel administrativo

------------------------------------------------------------

🛠️ Tecnologías
- Python 3.9+
- Django 4.x
- HTML + CSS
- SQLite3

------------------------------------------------------------

📁 Estructura del Proyecto

polisongstock/
│── manage.py
│── insertar_datos.py
│── README.md
│
├── polisongstock/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
└── store/
    ├── migrations/
    ├── templates/
    │   └── store/
    │       ├── base.html
    │       ├── vinilo_list.html
    │       ├── vinilo_form.html
    │       ├── vinilo_confirm_delete.html
    │       ├── cancion_list.html
    │       └── proveedor_list.html
    │
    ├── models.py
    ├── views.py
    ├── urls.py
    └── admin.py

------------------------------------------------------------

🚀 Instalación

1. Clonar el repositorio:
git clone https://github.com/tu-usuario/PoliSongStock.git

2. Crear entorno virtual:
python3 -m venv venv
source venv/bin/activate   (Mac/Linux)
venv\Scripts\activate    (Windows)

3. Instalar dependencias:
pip install -r requirements.txt

------------------------------------------------------------

🗄️ Migrar la base de datos:
python manage.py makemigrations
python manage.py migrate

------------------------------------------------------------

🔐 Crear superusuario:
python manage.py createsuperuser

------------------------------------------------------------

📥 Insertar datos automáticos:
python insertar_datos.py

------------------------------------------------------------

▶️ Ejecutar el servidor:
python manage.py runserver

URL de acceso:
http://127.0.0.1:8000/
Panel admin:
http://127.0.0.1:8000/admin/

------------------------------------------------------------

👨‍💻 Autor
Santiago López Cative – Proyecto PoliSongStock
