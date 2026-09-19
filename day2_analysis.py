import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Load Data
df = pd.read_csv(
    r'C:\EE2120_PROJECT\calibration_data.csv',
    skiprows=2
)

# 2. Calculate Errors
df['LM35_Error'] = np.abs(df['LM35_Temp'] - df['Ref_Temp'])
df['DS18B20_Error'] = np.abs(df['DS18B20_Temp'] - df['Ref_Temp'])

print("--- Summary & Error Table ---")
print(df[['Ref_Temp', 'LM35_Temp', 'LM35_Error', 'DS18B20_Temp', 'DS18B20_Error']])
print("\nLM35 MAE:", df['LM35_Error'].mean())
print("DS18B20 MAE:", df['DS18B20_Error'].mean())

# 3. Plot Graphs
plt.figure(figsize=(10, 4))

# Graph 1: Reference vs Sensor Readings
plt.subplot(1, 2, 1)
plt.plot(df['Ref_Temp'], df['Ref_Temp'], 'k--', label='Reference (Ideal)')
plt.plot(df['Ref_Temp'], df['LM35_Temp'], 'ro-', label='LM35')
plt.plot(df['Ref_Temp'], df['DS18B20_Temp'], 'bs-', label='DS18B20')
plt.title('Reference vs Sensor Readings')
plt.xlabel('Reference Temp (°C)')
plt.ylabel('Measured Temp (°C)')
plt.legend()
plt.grid(True)

# Graph 2: Absolute Errors
plt.subplot(1, 2, 2)
plt.plot(df['Ref_Temp'], df['LM35_Error'], 'r^--', label='LM35 Error')
plt.plot(df['Ref_Temp'], df['DS18B20_Error'], 'b^--', label='DS18B20 Error')
plt.title('Absolute Errors')
plt.xlabel('Reference Temp (°C)')
plt.ylabel('Error (°C)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig('sensor_comparison_graphs.png')
plt.show()
