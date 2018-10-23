
import geopandas as gpd
import numpy as np
import pandas as pd

from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize
from shapely.geometry import Point, LineString

path = r'C:\Users\Chris\Desktop\Machine Learning Raw Data\air-quality-madrid\stations.csv'
stations = pd.read_csv(path)
stations.head()

geometry = [Point(xy) for xy in zip(stations['lon'], stations['lat'])]
crs = {'init': 'epsg:4326'}
geoDF_stations = gpd.GeoDataFrame(stations, crs=crs, geometry=geometry)
geoDF_stations_new = geoDF_stations.to_crs({'init': 'epsg:25830'}) 

streetsystem = gpd.read_file('C:/Users/Chris/Desktop/Machine Learning Raw Data/900BTQKCJT/call2016.shp')
calleselected = streetsystem.loc[streetsystem['VIA_TVIA'] == "Calle"]
avdselected = streetsystem.loc[streetsystem['VIA_TVIA'] == "Avda"]
ctraselected = streetsystem.loc[streetsystem['VIA_TVIA'] == "Ctra"]
calleandavd = calleselected.append(avdselected)
streetselected = calleandavd.append(ctraselected)

#xlim=(420000,460000)
#ylim=(4460000,4490000)
base = streetselected.plot(figsize=(32,20), color='blue', edgecolor='blue',markersize=0.01); 
mapMadrid = geoDF_stations_new.plot(figsize=(32,20),ax=base, marker='o',color='red',markersize=100.0);
