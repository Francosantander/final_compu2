import sys
import argparse


class ArchivoError(Exception):
    pass


class ValError(Exception):
    pass


def argumentos():
    # creo la instancia del parser
    parser = argparse.ArgumentParser(description='Trabajo Final'
                                                 ' - Computacion 2')
    parser.add_argument('-p', '--port', default='5000',
                        help='puerto donde espera nuevas conexiones', type=int)
    
    args = parser.parse_args()
    
    try:
        if int(args.port) < 0:
            raise ValError()
    except ValError:
        print("Error. El puerto a conectar debe ser un valor entero positivo")
        sys.exit()
    
    return args

def get_file_type(data):
    for i in range(data.count(b"Content-Type")):
        inicio = data.find(b"Content-Type")
        fin = data.find(b"\n", inicio)
        type_file = data[inicio:fin-1]
    type_file = ((type_file.decode('utf-8').split(': '))[1])
    return type_file

def get_name_file(data):
    for i in range(data.count(b"filename")):
        inicio = data.find(b"filename")
        fin = data.find(b".kml", inicio + 1)
        name = data[inicio:fin+4]
    file_name=(name.decode('utf-8').split('"'))[1]
    return file_name

def clean_comments(data):
    for i in range(data.count(b"------")):
        inicio = data.find(b"------")
        fin = data.find(b"+xml", inicio)
        data = data.replace(data[inicio:fin], b"")
    for i in range(data.count(b"+xml")):
        inicio = data.find(b"+xml")
        data = data.replace(data[inicio:8], b"")
    return data