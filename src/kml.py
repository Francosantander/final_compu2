import geopandas as gpd
import fiona
from shapely.geometry import Point
import os
import time


def read_kml(path):
    #Creamos un diccionario para los datos leidos
    d = {}

    # fp es el archivo kml a leer
    fp = path
    fiona.drvsupport.supported_drivers['KML'] = 'rw'

    # Obtenemos las capas del KML
    index = fiona.listlayers(fp)

    pols = []

    # Recorrer con un for el listlayer, luego llamar con geopanda cada uno de los index
    for i in index:
        polys = gpd.read_file(fp, layer=i)
        pols.append([polys, i])
            
    d["kml"] = {"polys": pols}
    return d

    
def verify_coverage(d, lt, lg):
    # # Creamos el punto de coordenada del usuario a verificar
    p1 = Point(lg, lt, 0)
    print('\n')
    print(p1)

    # Create diccionary to results
    results = {}
    
    for key in d.keys():
        for poly in d[key]["polys"]:
            # convierto la informacion del kml a diccionario
            poligonos = poly[0].to_dict()
            for poligono in poligonos["geometry"]:
                validate = p1.within((poly[0]["geometry"][poligono]))
                if validate == True:
                    results[key] ="Layer: " + poly[1] + ", Zona: " + poly[0]["Name"][poligono]
    return results
