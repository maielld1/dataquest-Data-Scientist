## 1. Geographic Data ##

import pandas as pd

airlines = pd.read_csv('airlines.csv')
airports = pd.read_csv('airports.csv')
routes  = pd.read_csv('routes.csv')

print(airlines.iloc[0])
print(airports.iloc[0])
print(routes.iloc[0])

## 4. Workflow With Basemap ##

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)

## 5. Converting From Spherical to Cartesian Coordinates ##

m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
longitudes = airports["longitude"].tolist()
latitudes = airports["latitude"].tolist()
x, y = m(longitudes, latitudes)

## 6. Generating A Scatter Plot ##

m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
x, y = m(longitudes, latitudes)
m.scatter(x, y, s=1)
plt.show()

## 7. Customizing The Plot Using Basemap ##

m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
longitudes = airports["longitude"].tolist()
latitudes = airports["latitude"].tolist()
x, y = m(longitudes, latitudes)
m.scatter(x, y, s=1)

m.drawcoastlines()
plt.show()

## 8. Customizing The Plot Using Matplotlib ##

# Add code here, before creating the Basemap instance.
fig = plt.figure(figsize=(15, 20))
ax = fig.add_subplot(1, 1, 1)
ax.set_title('Scaled Up Earth With Coastlines')
m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
longitudes = airports["longitude"].tolist()
latitudes = airports["latitude"].tolist()
x, y = m(longitudes, latitudes)
m.scatter(x, y, s=1)
m.drawcoastlines()
plt.show()

## 9. Introduction to Great Circles ##

geo_routes = pd.read_csv("geo_routes.csv")
geo_routes.info()
geo_routes.head()

## 10. Displaying Great Circles ##

fig, ax = plt.subplots(figsize=(15,20))
m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
m.drawcoastlines()

def create_great_circles(df):
    # Add your code here.
    for index, row in df.iterrows():
        start_lon = row['start_lon']
        start_lat = row['start_lat']
        end_lon = row['end_lon']
        end_lat = row['end_lat']
        if abs(end_lat - start_lat) < 180 and abs(end_lon - start_lon) < 180:
          m.drawgreatcircle(start_lon, start_lat, end_lon, end_lat, linewidth=1)
    
dfw = geo_routes[geo_routes['source'] == "DFW"]
create_great_circles(dfw)
plt.show()