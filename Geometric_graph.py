import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt

# 1. Create a figure and set up an axes with a map projection
fig = plt.figure(figsize=(10, 6))
ax = plt.axes(projection=ccrs.PlateCarree())  # Equirectangular projection

# 2. Add geographic features to the map
ax.add_feature(cfeature.LAND, facecolor="lightgray")
ax.add_feature(cfeature.OCEAN, facecolor="lightblue")
ax.add_feature(cfeature.COASTLINE, edgecolor="black", linewidth=0.5)
ax.add_feature(cfeature.BORDERS, edgecolor="gray", linestyle=":")

# 3. Define sample data points (Longitude, Latitude)
# Cities: San Francisco, Paris, Tokyo, Sydney
lons = [-122.4194, 2.3522, 139.6917, 151.2093]
lats = [37.7749, 48.8566, 35.6762, -33.8688]

# 4. Plot data points onto the map
# CRITICAL: Always pass 'transform=ccrs.PlateCarree()' when plotting raw lat/lon coordinates
ax.scatter(
    lons, lats, color="red", marker="o", s=50, transform=ccrs.PlateCarree()
)

# 5. Add map visual aids
ax.gridlines(draw_labels=True, linestyle="--", alpha=0.5)
plt.title("World Map Example with Cartopy & Matplotlib", fontsize=14)

# save the plot 
plt.savefig("World_map.png")
# 6. Display the plot
plt.show()
