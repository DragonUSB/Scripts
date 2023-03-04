import pandas as pd
import plotly.express as px
import geojson

with open('estados.geojson') as f:
    data = geojson.load(f)

COD_ESTADO = []
ESTADO = []

for feature in data['features']:
    COD_ESTADO.append(feature['properties']['COD_ESTADO'])
    ESTADO.append(feature['properties']['ESTADO'])

# Create a dataframe with the region names
df = pd.DataFrame({'COD_ESTADO': COD_ESTADO, 'ESTADO': ESTADO})
# For demonstration, create a column with the length of the region's name
df['name_length'] = df['ESTADO'].str.len()

# Choropleth representing the length of region names
fig = px.choropleth(data_frame=df, 
                    geojson=data, 
                    locations='COD_ESTADO', # name of dataframe column
                    featureidkey='properties.COD_ESTADO',  # path to field in GeoJSON feature object with which to match the values passed in to locations
                    color='name_length',
                    color_continuous_scale="rainbow"
                   )
fig.update_geos(showcountries=False, showcoastlines=False, showland=False, fitbounds="locations")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()