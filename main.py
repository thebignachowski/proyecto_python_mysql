"""
Proyecto Python Mysql:
- Abrir un asistente, que me permita registrarme o
logearme.
-Si elegimos registro, creará un usuario en la bbdd
-Si elegimos login, identificará al usuario y nos 
preguntará
- Crear nota, mostrar nota o borrer nota.
"""
from usuarios import acciones

print("""
Acciones disponibles:
    - Registro
    - Login
""")

acciones_modulo = acciones.Acciones()
accion = input("¿Qué quiers hacer?: ").lower()

if accion == "registro":
    acciones_modulo.registro()

elif accion == "login":
    acciones_modulo.login()


