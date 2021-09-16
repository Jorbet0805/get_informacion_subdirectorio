import os
import pdb

path = "Z:\\"
contenido = os.listdir(path)
# print(contenido)


def list_to_text(lista: list):
    texto = ''
    for elemento in lista:
        texto += elemento + '\n'
    return texto


def extension(key):
    i = key.rfind('.')
    return key[i:]


numero_de_iterarcion = 0
n_archivos = 0
with open('F:\\Usuario\\Desktop\\todos_los_archivos.txt', 'w', encoding='utf-8') as Archivo:
    for base, dirs, files in os.walk(path):
        files.sort(key = extension)
        # print(dirs)
        # print(base)

        # if numero_de_iterarcion == 0:
        #     base = list_to_text(base)

        Archivo.write(50*'#'+'\n')

        Archivo.write(base)

        Archivo.write('\n')

        dirs = list_to_text(dirs)
        Archivo.write(dirs)

        n_archivos += len(files)

        files = list_to_text(files)
        Archivo.write(files)

        Archivo.write('Resumen: Numero de archivos {0}'.format(len(files))+'\n')

        numero_de_iterarcion = numero_de_iterarcion + 1

    Archivo.write('\n')

    Archivo.write('Resumen General: Numero total de archivos {0}'.format(n_archivos)+'\n')

    print(n_archivos)
