#Primero descargamos del INE el zip con los ficheros de las secciones censales. El fichero que nos interesa es el que tiene extension .shp  "SECC_CPV_E_20111101_01_R_INE.shp"
# https://www.ine.es/censos2011_datos/cartografia_censo2011_nacional.zip
#la funcion devuelve el código de seccion censal

import geopandas as gpd
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
  
def sec_censal (x,y,ruta_fichero):
  
  shapefile = gpd.read_file(ruta_fichero + "\\SECC_CPV_E_20111101_01_R_INE.shp")
  point = Point(x,y) 
  # shapefile[shapefile.geometry.contains(punto)].NMUN devuelve el nombre del municipio al que pertenece

  salida=shapefile[shapefile.geometry.contains(point)].CUSEC 
  return(salida)
  
#ejemplo : 
sec_censal(676576.70765588,4612618.97474742,'C:\\shp_sec_censal\\')
  
