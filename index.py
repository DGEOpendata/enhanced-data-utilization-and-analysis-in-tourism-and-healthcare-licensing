python
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load Healthcare Licensing Data
healthcare_data = pd.read_csv("Healthcare_Facility_Licenses.csv")

# Load Tourism Licensing Data
tourism_data = pd.read_excel("DL09-Tourism-Licenses-ADRA-OD-013-LTO.xlsx")

# Filter Active Licenses
active_healthcare = healthcare_data[healthcare_data['license_status'] == 'Active']
active_tourism = tourism_data[tourism_data['License Status'] == 'Active']

# Combine datasets for geographical mapping
combined_data = pd.concat([
    active_healthcare[['facility_name', 'facility_type', 'latitude', 'longitude']],
    active_tourism[['Trade Name', 'License Type', 'Latitude', 'Longitude']]
], axis=0, ignore_index=True)

# Convert to GeoDataFrame
geometry = gpd.points_from_xy(combined_data['longitude'], combined_data['latitude'])
geo_combined_data = gpd.GeoDataFrame(combined_data, geometry=geometry)

# Plot the facilities on a map
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
ax = world.plot(figsize=(15, 10), color='white', edgecolor='black')
geo_combined_data.plot(ax=ax, color='blue', markersize=10)
plt.title("Active Healthcare and Tourism Facilities in Abu Dhabi")
plt.show()
