import pandas as pd
import geopandas as gpd
from geodatasets import get_path
import matplotlib.pyplot as plt

path_geodata = "C:/Users/alencar/Documents/DataScience/caesb_proj/malha/"
gdf = gpd.read_file(path_geodata)

gdf.plot(legend=True)
#plt.show()


gdf.explore(legend=False)

