import chardet
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
 
def find_encoding(fname):
    r_file = open(fname, 'rb').read()
    result = chardet.detect(r_file)
    charenc = result['encoding']
    return charenc
 
my_encoding = find_encoding('stations.csv')
df = pd.read_csv('stations.csv',delimiter = ',', encoding = my_encoding)

print(df.head())

longitude_x = df.loc[:,'longitude']
latitude_y = df.loc[:,'latitude']

brand = df.loc[:,'brand'].unique()

#print(brand)
#print(longitude_x, latitude_y)

# setting up projection
# world map: map = Basemap(projection='cyl')
# Germany:
map = Basemap(projection='cyl',llcrnrlat=46,urcrnrlat=56,llcrnrlon=4,urcrnrlon=16,resolution='c')            

# setting up coastlines, countries, continents, rivers..
map.drawcoastlines()
map.drawcountries()
map.drawstates()

# setting up the background: available choices* bluemarble(), etopo(), shadedrelied() 
map.bluemarble() 

plt.scatter(longitude_x, latitude_y, alpha = 0.5)
plt.title('Tankerkönig scatter plot')
plt.show()
