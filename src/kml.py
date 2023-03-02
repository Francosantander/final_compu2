import geopandas as gpd
import fiona
from shapely.geometry import Point
import os
import time
# from concurrent import futures
#import threading

global result

result = {}

#lc = threading.Lock()

def process_kml(path, lt, lg):
    #Creamos un diccionario para los datos
    d = {}

    # obtengo el path donde estan los kml
    dir = path

    pols = []
    # Creo una lista con los KML a recorrer
    kmls = os.listdir(dir)
    
    # Recorro los kmls del directorio kml y verifico cobertura
    
    #hilos = futures.ThreadPoolExecutor(max_workers=len(kmls))
    
    #threads = []

    for kml in kmls:
        # Crear hilos, pasarle la funcion que verifica la cobertura y el mapa leido
        file_name = (kml.split("."))[0]
        
        # fp es el archivo kml a leer
        fp = dir + kml
        
        #Driver para leer los kml
        # fiona.drvsupport.supported_drivers['LIBKML'] = 'rw'
        fiona.drvsupport.supported_drivers['KML'] = 'rw'

        # Obtenemos las capas del KML
        index = fiona.listlayers(fp)

        # Recorrer con un for el listlayer, luego llamar con geopanda cada uno de los index
        for i in index:
            polys = gpd.read_file(fp, layer=i)
            pols.append([polys, i])

        # Almaceno los poligonos del mapa para luego verificar la cobertura    
    d[file_name] = {"polys": pols}
    result = verify_coverage(d, lt, lg)
        # mendoza.kml: {polys: pols}
        # threads.append(hilos.submit(verify_coverage, d, lt, lg))
    return result
    
def verify_coverage(d, lt, lg):
    # # Creamos el punto de coordenada del usuario a verificar
    # p1 = Point(-68.97434, -33.0801393, 0)
    p1 = Point(lg, lt, 0)
    print('\n')
    
    # Create diccionary to results
    global result
    
    print(d.keys())
    
    for key in d.keys():
        for poly in d[key]["polys"]:
            # convierto la informacion del kml a diccionario
            poligonos = poly[0].to_dict()
            for poligono in poligonos["geometry"]:
                validate = p1.within((poly[0]["geometry"][poligono]))
                if validate == True:
                    # lc.acquire()
                    result[key] ="Layer: " + poly[1] + ", Zona: " + poly[0]["Name"][poligono]
                    # lc.release()
    return result