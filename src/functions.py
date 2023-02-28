import sys
import argparse
# import os


class ArchivoError(Exception):
    pass


class ValError(Exception):
    pass


def argumentos():
    # parser = ArgumentParser(description='TP1')
    # creo la instancia del parser
    parser = argparse.ArgumentParser(description='Trabajo Final'
                                                 ' - Computacion 2')
    parser.add_argument('-p', '--port', default='5000',
                        help='puerto donde espera nuevas conexiones', type=int)
    parser.add_argument('-s', '--size', default=1026,
                        help='bloque de lectura', type=int)
    # parser.add_argument('-d', '--document_root', default='No ingreso nada',
    #                     help='directorio donde se encuentran los documentos', type=str)
    args = parser.parse_args()
    # hago un manejo de error en caso de que ingrese un document-root vacio
    # text = ""
    # try:
    #     if args.document_root == "No ingreso nada":
    #         raise ArchivoError()
    # except ArchivoError:
    #     text += "Error. Ingrese un archivo que se encuentre en el"
    #     text += " mismo directorio"
    #     print(text)
    #     sys.exit()
    try:
        if int(args.size) < 0:
            raise ValError()
    except ValError:
        print("Error. El tamaño del bloque no puede ser negativo")
        sys.exit()
    try:
        if int(args.port) < 0:
            raise ValError()
    except ValError:
        print("Error. El puerto a conectar debe ser un valor entero positivo")
        sys.exit()
    # try:
    #     path = args.document_root
    #     os.chdir(path)
    # except FileNotFoundError:
    #     print("Error. Ingrese un path que exista")
    #     sys.exit()
    return args

def get_file_type(data):
    for i in range(data.count(b"name")):
        inicio = data.find(b"name")
        fin = data.find(b"kml", inicio + 1)
        type_file = data[inicio:fin+3]
    type_file = ((type_file.decode('utf-8').split('"'))[1])
    return type_file

def get_name_file(data):
    for i in range(data.count(b"filename")):
        inicio = data.find(b"filename")
        fin = data.find(b".kml", inicio + 1)
        name = data[inicio:fin+4]
    file_name=(name.decode('utf-8').split('"'))[1]
    return file_name

def clean_comments(data):
    for i in range(data.count(b"------Web")):
        inicio = data.find(b"------Web")
        fin = data.find(b"+xml", inicio + 4)
        data = data.replace(data[inicio:fin], b"")
    for i in range(data.count(b"+xml")):
        inicio = data.find(b"+xml")
        data = data.replace(data[inicio:8], b"")
    return data