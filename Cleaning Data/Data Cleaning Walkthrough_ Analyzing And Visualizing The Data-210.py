## 2. Finding correlations ##

correlations = combined.corr()
correlations = correlations['sat_score']
correlations.head()

## 3. Plotting enrollment ##

import matplotlib.pyplot as plt
combined.plot.scatter(x='total_enrollment', y='sat_score')

## 4. Exploring schools with low SAT scores and enrollment ##

low_enrollment = combined[(combined['total_enrollment']<1000)&(combined['sat_score']<1000)]
low_enrollment['School Name']

## 5. Plotting language learning percentage ##

combined.plot.scatter(x='ell_percent',y='sat_score')

## 6. Mapping the schools ##

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
m = Basemap(
    projection='merc', 
    llcrnrlat=40.496044, 
    urcrnrlat=40.915256, 
    llcrnrlon=-74.255735, 
    urcrnrlon=-73.700272,
    resolution='i'
)

m.drawmapboundary(fill_color='#85A6D9')
m.drawcoastlines(color='#6D5F47', linewidth=.4)
m.drawrivers(color='#6D5F47', linewidth=.4)

longitudes = combined['lon'].tolist() 
latitudes = combined['lat'].tolist() 
x, y = m(longitudes, latitudes)
m.scatter(x, y, s=20, zorder=2, latlon=False, marker = 'o')
plt.show()

## 7. Plotting out statistics ##

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
m = Basemap(
    projection='merc', 
    llcrnrlat=40.496044, 
    urcrnrlat=40.915256, 
    llcrnrlon=-74.255735, 
    urcrnrlon=-73.700272,
    resolution='i'
)

m.drawmapboundary(fill_color='#85A6D9')
m.drawcoastlines(color='#6D5F47', linewidth=.4)
m.drawrivers(color='#6D5F47', linewidth=.4)

longitudes = combined['lon'].tolist() 
latitudes = combined['lat'].tolist() 
x, y = m(longitudes, latitudes)
m.scatter(x, y, s=20, zorder=2, latlon=False, c=combined["ell_percent"], cmap='summer')
plt.show()

## 8. Calculating district level statistics ##

import numpy

districts = combined.groupby('school_dist').agg(numpy.mean)
districts.reset_index(inplace=True)
districts.head()

## 9. Plotting ell_percent by district ##

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
m = Basemap(
    projection='merc', 
    llcrnrlat=40.496044, 
    urcrnrlat=40.915256, 
    llcrnrlon=-74.255735, 
    urcrnrlon=-73.700272,
    resolution='i'
)

m.drawmapboundary(fill_color='#85A6D9')
m.drawcoastlines(color='#6D5F47', linewidth=.4)
m.drawrivers(color='#6D5F47', linewidth=.4)

longitudes = districts['lon'].tolist() 
latitudes = districts['lat'].tolist() 
x, y = m(longitudes, latitudes)
m.scatter(x, y, s=50, zorder=2, latlon=False, c=districts["ell_percent"], cmap='summer')
plt.show()