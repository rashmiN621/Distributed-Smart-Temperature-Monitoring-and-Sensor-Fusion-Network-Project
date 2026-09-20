import numpy as np
import matplotlib.pyplot as plt

# 1. Distributed Sensor Nodes Data (Latitude, Longitude, Fused Temperature)
# Node 1 is our node (UoP EEE Dept)
nodes = {
    "Node 1 (Our Node)": {"lat": 7.2543, "lon": 80.5917, "temp": 28.3},
    "Node 2": {"lat": 7.2560, "lon": 80.5930, "temp": 30.1},
    "Node 3": {"lat": 7.2520, "lon": 80.5900, "temp": 26.8},
    "Node 4": {"lat": 7.2555, "lon": 80.5890, "temp": 29.0},
    "Node 5": {"lat": 7.2510, "lon": 80.5940, "temp": 27.5}
}

# Extract node arrays
node_lats = np.array([data["lat"] for data in nodes.values()])
node_lons = np.array([data["lon"] for data in nodes.values()])
node_temps = np.array([data["temp"] for data in nodes.values()])

# 2. Inverse Distance Weighting (IDW) Function
def idw_estimation(x_target, y_target, x_nodes, y_nodes, values, p=2):
    """
    T(x,y) = sum(T_i / d_i^p) / sum(1 / d_i^p)
    """
    distances = np.sqrt((x_nodes - x_target)**2 + (y_nodes - y_target)**2)
    
    # If the target point is exactly on a sensor node
    if np.any(distances == 0):
        return values[np.argmin(distances)]
    
    weights = 1.0 / (distances ** p)
    estimated_temp = np.sum(weights * values) / np.sum(weights)
    return round(estimated_temp, 2)

# 3. Estimate Temperature at an Unknown Coordinate
target_lat, target_lon = 7.2535, 80.5912
predicted_temp = idw_estimation(target_lat, target_lon, node_lats, node_lons, node_temps)

print("="*60)
print(f"DISTRIBUTED TEMPERATURE ESTIMATION (TASK 5)")
print("="*60)
print(f"Target Location Coordinates: ({target_lat}, {target_lon})")
print(f"Estimated Temperature (IDW Method): {predicted_temp} °C")
print("="*60)

# 4. Generate Spatial Heat Map
grid_lat = np.linspace(min(node_lats) - 0.002, max(node_lats) + 0.002, 100)
grid_lon = np.linspace(min(node_lons) - 0.002, max(node_lons) + 0.002, 100)
grid_lon_mesh, grid_lat_mesh = np.meshgrid(grid_lon, grid_lat)

grid_temp = np.zeros(grid_lat_mesh.shape)

for i in range(grid_lat_mesh.shape[0]):
    for j in range(grid_lat_mesh.shape[1]):
        grid_temp[i, j] = idw_estimation(
            grid_lat_mesh[i, j], grid_lon_mesh[i, j],
            node_lats, node_lons, node_temps
        )

# Plotting Heat Map
plt.figure(figsize=(9, 7))
contour = plt.contourf(grid_lon_mesh, grid_lat_mesh, grid_temp, levels=50, cmap='coolwarm')
plt.colorbar(contour, label='Estimated Temperature (°C)')

# Plot Sensor Nodes
plt.scatter(node_lons, node_lats, color='black', marker='o', s=100, label='Sensor Nodes')
for name, data in nodes.items():
    plt.annotate(f"{name}\n({data['temp']}°C)", (data['lon'], data['lat']),
                 textcoords="offset points", xytext=(0,8), ha='center', fontsize=8, weight='bold')

# Plot Target Unknown Coordinate
plt.scatter(target_lon, target_lat, color='green', marker='X', s=150, label=f'Target Point ({predicted_temp}°C)')

plt.title('EE2120: Distributed Temperature Heat Map (IDW Spatial Interpolation)', fontsize=11, fontweight='bold')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend(loc='lower left')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

# Save Map Image
plt.savefig('spatial_temperature_heatmap.png', dpi=300)
print("[SUCCESS] Spatial Heat Map saved as 'spatial_temperature_heatmap.png'")
plt.show()
