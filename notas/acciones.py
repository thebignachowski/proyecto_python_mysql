import notas.nota as modelo

class Acciones:

    def crear(self, usuario):
        print(f"\nOk { usuario[1] }!! Vamos a crear una nueva nota...")
        titulo = input("Introduce el título de tu nota")
        descripcion = input("Introduce el contenido de tu nota")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nPerfecto has guardado la nota: { nota.titulo }")
        else:
            print(f"\nNo se ha podido guardar la nota, lo siento { usuario[1] }")

    def mostrar(self, usuario):
        print(f"\nVale { usuario[1] }, Aquí tienes tus notas")

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()
        print(notas)

        for nota in notas:
            print("\n*****************************")
            print(nota[2])
            print(nota[3])

    def borrar( self, usuario ):
        print(f"\nOK { usuario[1] }, vamos a borrar notas")
        titulo = print("Introduce el título de la nota a borrar")

        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"Hemos eliminado la nota: { nota.titulo } ")

        else:
            print("No se ha borrado la nota")

