import photo

def main():
    print("Bienvenido al simulador de una foto sin luz :D \n")
    print("Seleccione una opcion")
    print("1. Foto por defecto")
    print("2. Cargar foto")
    option = int(input())

    match option:
        case 1:
            img = photo.create_photo()
            new = photo.new_photo(img)
            photo.save_photo(img, "gato.png")
            photo.save_photo(new, "gato_cuantico.png")
        case 2:
            print("Ingrese la ruta de la imagen (Ej: gato.png)")
            path = input()
            print("Ingrese el tamaño de la matriz (Ej: 32 = 32x32)")
            size = int(input())
            img = photo.load_bw_photo(path, (size, size))
            new = photo.new_photo(img)
            photo.save_photo(img, "imagen_cuantica.png")
        case _:
            print("Opcion invalida")

if __name__ == "__main__":
    main()





