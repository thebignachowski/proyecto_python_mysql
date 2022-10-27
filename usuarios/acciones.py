import usuarios.usuario as modelo
import notas.acciones

class Acciones:
     
    def registro(self):
        print("\nOK! Vamos a registrarte en el sistema...")
        nombre = input("Dime tu nombre: ")
        apellidos = input("Dime tu apellido: ")
        email = input("Introduce tu email: ")
        passwd = input("Indica una contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, passwd)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"\nPerfecto { registro[1].nombre } te has registrado con el email { registro[1].email }")
        else:
            print("No te has registrado correctamente")

    def login(self):
        print("Vale! Identificate en el sistema...")

        try:
            email = input("Introduce tu email: ")
            passwd = input("Indica una contraseña: ")

            usuario = modelo.Usuario('', '', email, passwd)
            login = usuario.identificar()

            if email == login[3]:
                print(f"Bienvenido { login[1] }, te has registrado en el sistema el { login[5] }")
                self.proximasAcciones(login)
        except Exception as e:
            print(f"Login incorrecto")

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
        - Crear nota (crear)
        - Mostrar tus notas (mostrar)
        - Eliminar nota (eliminar)
        - Salir (salir)
        """)

        accion = input("¿Qué quieres hacer?: ").lower()
        trabajar_notas = notas.acciones.Acciones()

        if accion == "crear":
            trabajar_notas.crear(usuario)
            self.proximasAcciones(usuario)
        elif accion == "mostrar":
            trabajar_notas.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "eliminar":
            trabajar_notas.borrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "salir":
            print(f"Ok { usuario[1] }, hasta pronto")
            exit()
