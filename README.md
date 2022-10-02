# Moonquake Map
A Moonquake Map for Planetary Scientists

## About
This project was created for NASA's Space Apps Challenge 2022.

For more information please refer to our team site:  
https://2022.spaceappschallenge.org/challenges/2022-challenges/moonquake-map/teams/brute-force-5/project

Try out a demo of the map:
https://constantinosar.github.io/Moonquake-Map/

##  Detailed Project Description
### Moon Map
This project produces a map of the moon with Apollo PSE network stations and their plotted seismometer observations, as
well as shallow moonquake locations with ripple effects according to their magnitude. The Apollo landing locations are
also displayed for reference [3].

The map was built using the Globe.GL javascript library which is based on Three.js, an open source WebGL 3D renderer for
the web [3]. The entry point of the webpage is index.html which holds the logic for rendering the processed data.

The tool provides easy-to-use functions to displays items on the map.

### Timeline and Nakamura Tabs
The map has two main tabs to select options to display data, the "Timeline" tab to view data from stations in the Apollo
Passive Seismic Experiments (PSE) Network and the "Nakamura" tab to visualize shallow moonquake locations and magnitude.

Using the "Timeline" tab, the user is able to select a date by selecting the year, month, and day of the date.
Then, by clicking "Show Data", if during that day any of the 5 stations in the Apollo PSE network (S11, S12, S14, S15,
S16) transmitted data from its seismometers back to Earth, its location will be highlighted on the map. By clicking on
a station, a plot of processed time-series data from the SEED Collection [2] will appear. Each plot includes a graph for
each of the mid-period seismometers (MH1, MH2, MHZ). Additionally, the max deviations from average daily values recorded
on the plots are included with on each graph's title, which are useful to note disturbances in the graphs, indicating a
possible moonquake.

![PSE stations](/resources/demo_stations.png)

Using the "Nakamura" tab, the user is able to click on dates from a list of dates where shallow moonquakes were detected
in Nakamura et al. 1979 [1]. Clicking on a date highlights the corresponding moonquake with a ripple effect relative to
the magnitude of the moonquake. Multiple moonquakes can be selected and displayed on the map. Clicking on "Clear Data"
removes any mapped moonquakes from the map.

![Nakamura moonquakes](/resources/demo_moonquakes.png)

The Apollo PSE data used was scraped from NASA's PDS with pse_fetch.py and plotted with pse_plot.py using Python. ObsPy
was used for data processing and plotting. Station info and locations (longitude, latitude) were retrieved from the
FDSN [4]. The Nakamura 1979 data was fetched and converted for usage with nakamura_convert.py using Python.


## Space Agency Data
Apollo PSE station info and locations from the FDSN [4] was used to map the stations. The data from these stations [3]
was scraped from NASA's PDS and processed to display mid-period seismometer data graphs. In order to detect
disturbances, max deviations are also plotted.

Nakamura 1979 data [1] was used to display the locations of shallow moonquakes and display a ripple effect according to
their magnitude in the data.

Apollo landing locations from Globe.GL [3] were used to plot the landings to have a reference of their locations when
viewing stations.

## References
[1] Apollo Passive Seismic Experiment Expanded Event Catalog Online from NASA's Planetary Data System (PDS):  
    https://pds-geosciences.wustl.edu/missions/apollo/seismic_event_catalog.htm

[2] Apollo Passive Seismic Experiment SEED Collection from NASA's Planetary Data System (PDS):  
    https://pds-geosciences.wustl.edu/lunar/urn-nasa-pds-apollo_pse/

[3] Globe.Gl for Moon Map and Apollo landing locations:  
    https://github.com/vasturiano/globe.gl

[4] Apollo Passive Seismic Experiments Station Info and Locations from the FDSN:  
    https://www.fdsn.org/networks/detail/XA_1969/
