import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Calibration Data Load කිරීම
df = pd.read_csv('calibration_data.csv')

# 2. Absolute Errors ගණනය කිරීම
df['LM35_Error'] = np.abs(df['LM35_Temp'] - df['Ref_Temp'])
df['DS18B20_Error'] = np.abs(df['DS18B20_Temp'] - df['Ref_Temp'])

# 3. Terminal එකේ Summary & Error Table එක Print කිරීම
print("==================================================")
print("         EE2120 - DAY 2 SENSOR ERROR TABLE         ")
print("==================================================")
print(df[['Ref_Temp', 'LM35_Temp', 'LM35_Error', 'DS18B20_Temp', 'DS18B20_Error']])
print("\n--- Mean Absolute Errors (MAE) ---")
print(f"LM35 MAE    : {df['LM35_Error'].mean():.2f} °C")
print(f"DS18B20 MAE : {df['DS18B20_Error'].mean():.2f} °C")
print("==================================================")

# 4. Graphs ඇඳීම
plt.figure(figsize=(12, 5))

# Plot 1: Reference vs Measured Readings
plt.subplot(1, 2, 1)
plt.plot(df['Ref_Temp'], df['Ref_Temp'], 'k--', label='Ideal (Reference)')
plt.plot(df['Ref_Temp'], df['LM35_Temp'], 'ro-', label='LM35')
plt.plot(df['Ref_Temp'], df['DS18B20_Temp'], 'bs-', label='DS18B20')
plt.title('Sensor Readings vs Reference Temp')
plt.xlabel('Reference Temp (°C)')
plt.ylabel('Measured Temp (°C)')
plt.legend()
plt.grid(True)

# Plot 2: Absolute Errors
plt.subplot(1, 2, 2)
plt.plot(df['Ref_Temp'], df['LM35_Error'], 'r^--', label='LM35 Absolute Error')
plt.plot(df['Ref_Temp'], df['DS18B20_Error'], 'b^--', label='DS18B20 Absolute Error')
plt.title('Absolute Errors Across Temperature Range')
plt.xlabel('Reference Temp (°C)')
plt.ylabel('Absolute Error (°C)')
plt.legend()
plt.grid(True)

plt.tight_layout()
# Graph image එක auto-save කරගැනීම
plt.savefig('sensor_comparison_graphs.png')
print("\nGraph successfully saved as 'sensor_comparison_graphs.png'!")
plt.show()
