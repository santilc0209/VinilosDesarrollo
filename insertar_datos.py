import os
import django

# Configuración para usar Django dentro de este script
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'polisongstock.settings')
django.setup()

from store.models import Proveedor, Cancion, Vinilo

# ----------------------------
# INSERTAR PROVEEDORES
# ----------------------------
proveedores = [
    ("Sony Music Colombia", "contacto@sonymusic.com", "3001234567"),
    ("Universal Music Group", "ventas@umg.com", "3109876543"),
    ("Warner Music Latin", "latam@warnermusic.com", "3154448899"),
]

for nombre, correo, telefono in proveedores:
    Proveedor.objects.get_or_create(
        nombre=nombre,
        correo=correo,
        telefono=telefono
    )

print("✔ Proveedores insertados correctamente.")

# ----------------------------
# INSERTAR CANCIONES
# ----------------------------
canciones = [
    ("Billie Jean", "Michael Jackson", 1982, 293, 4500),
    ("Come Together", "The Beatles", 1969, 259, 4500),
    ("Hotel California", "Eagles", 1976, 390, 5000),
    ("Blinding Lights", "The Weeknd", 2020, 200, 5200),
    ("Smells Like Teen Spirit", "Nirvana", 1991, 301, 4800),
]

lista_canciones = []
for titulo, artista, año, duracion, precio in canciones:
    obj, created = Cancion.objects.get_or_create(
        titulo=titulo,
        artista=artista,
        año=año,
        duracion_seg=duracion,
        precio=precio
    )
    lista_canciones.append(obj)

print("✔ Canciones insertadas correctamente.")

# ----------------------------
# INSERTAR VINILOS
# ----------------------------
proveedor_sony = Proveedor.objects.get(nombre="Sony Music Colombia")
proveedor_universal = Proveedor.objects.get(nombre="Universal Music Group")

vinilos = [
    ("Thriller", "Michael Jackson", 1982, 120000, 10, proveedor_sony, ["Billie Jean"]),
    ("Abbey Road", "The Beatles", 1969, 90000, 7, proveedor_universal, ["Come Together"]),
    ("Hotel California", "Eagles", 1976, 100000, 4, proveedor_universal, ["Hotel California"]),
    ("After Hours", "The Weeknd", 2020, 80000, 5, proveedor_sony, ["Blinding Lights"]),
    ("Nevermind", "Nirvana", 1991, 95000, 8, proveedor_sony, ["Smells Like Teen Spirit"])
]

for titulo, artista, año, precio, stock, prov, canciones_nombres in vinilos:
    vinilo, created = Vinilo.objects.get_or_create(
        titulo=titulo,
        artista=artista,
        año=año,
        precio=precio,
        stock=stock,
        proveedor=prov
    )
    # Relacionar canciones
    for nombre_cancion in canciones_nombres:
        cancion = Cancion.objects.get(titulo=nombre_cancion)
        vinilo.canciones.add(cancion)

print("✔ Vinilos insertados correctamente con sus canciones asociadas.")

print("🎉 TODOS LOS DATOS FUERON INSERTADOS EXITOSAMENTE")
