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
    global result
    # Lo inicializo vacio ya que queda luego almacenado la respuesta de la request anterior
    result = {}
    start = time.time()
    # Creo una lista con los KML a recorrer
    kmls = os.listdir(path)
    
    # Recorro los kmls del directorio kml y verifico cobertura    
    hilos = concurrent.futures.ThreadPoolExecutor(max_workers=len(kmls))
    
    r = [hilos.submit(verify_coverage, kml, lt, lg, path) for kml in kmls ]
    
    for i in range(len(r)):   
        r[i].result()
    end = time.time()
    print(end-start)
    return result
    
def verify_coverage(kml, lt, lg, path):
        
    # Creamos el punto de coordenada del usuario a verificar
    # p1 = Point(-68.97434, -33.0801393, 0)
    p1 = Point(lg, lt, 0)
    
    # Create diccionary to results
    global result
    
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
        try:
            if result[file_name]:
                break
        except KeyError:
            polys = gpd.read_file(fp, layer=i)        
            # convierto la informacion del kml a diccionario
            poligonos = polys.to_dict()
            for poligono in poligonos["geometry"]:
                validate = p1.within((polys["geometry"][poligono]))
                if validate == True:
                    lc.acquire()
                    result[file_name] ="Layer: " + i + ", Zona: " + polys["Name"][poligono]
                    lc.release()
                    break
    return result