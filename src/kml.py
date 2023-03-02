import geopandas as gpd
import fiona
from shapely.geometry import Point
import os
import time
import concurrent.futures
import threading

global result

result = {}

lc = threading.Lock()

def process_kml(path, lt, lg):
    start = time.time()

    # Creo una lista con los KML a recorrer
    kmls = os.listdir(path)
    
    # Recorro los kmls del directorio kml y verifico cobertura
    print(len(kmls))
    
    hilos = concurrent.futures.ThreadPoolExecutor(max_workers=len(kmls))
    
    r = [hilos.submit(verify_coverage, kml, lt, lg, path) for kml in kmls ]
    
    for i in range(len(r)):   
        r[i].result()
    end = time.time()
    print(end-start)
    return result
    
def verify_coverage(kml, lt, lg, path):
    
    pols = []
    
    file_name = (kml.split("."))[0]
            
    # fp es el archivo kml a leer
    fp = path + kml
    
    #Driver para leer los kml
    # fiona.drvsupport.supported_drivers['LIBKML'] = 'rw'
    fiona.drvsupport.supported_drivers['KML'] = 'rw'

    # Obtenemos las capas del KML
    index = fiona.listlayers(fp)

    # Recorrer con un for el listlayer, luego llamar con geopanda cada uno de los index
    for i in index:
        polys = gpd.read_file(fp, layer=i)
        pols.append([polys, i])

    # # Creamos el punto de coordenada del usuario a verificar
    # p1 = Point(-68.97434, -33.0801393, 0)
    p1 = Point(lg, lt, 0)
    print('\n')
    # Create diccionary to results
    global result
    
    for poly in pols:
        # convierto la informacion del kml a diccionario
        poligonos = poly[0].to_dict()
        for poligono in poligonos["geometry"]:
            validate = p1.within((poly[0]["geometry"][poligono]))
            if validate == True:
                lc.acquire()
                result[file_name] ="Layer: " + poly[1] + ", Zona: " + poly[0]["Name"][poligono]
                lc.release()
                print(result[file_name])
    return result