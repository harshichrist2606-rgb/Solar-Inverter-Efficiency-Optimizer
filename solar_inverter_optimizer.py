import numpy as np
import matplotlib.pyplot as plt

print("=" * 65)
print("          SOLAR INVERTER EFFICIENCY OPTIMIZER")
print("=" * 65)

# Inverter parameters
rated_power = float(input("Enter inverter rated power (kW): "))
dc_voltage = float(input("Enter DC input voltage (V): "))
dc_current = float(input("Enter DC input current (A): "))

# Basic DC input power
dc_power = (dc_voltage * dc_current) / 1000

print(f"\nActual DC Input Power: {dc_power:.2f} kW")

# Generate operating power range
power_values = np.linspace(0.1, rated_power, 100)

# Inverter loss model
# Constant losses + variable losses
constant_loss = 0.02 * rated_power
variable_loss_factor = 0.04

losses = (
    constant_loss
    + variable_loss_factor * (power_values ** 2 / rated_power)
)

# AC output power
ac_power = power_values - losses

# Efficiency
efficiency = (ac_power / power_values) * 100

# Remove invalid values
efficiency = np.maximum(efficiency, 0)

# Find optimum point
max_index = np.argmax(efficiency)

optimal_power = power_values[max_index]
optimal_efficiency = efficiency[max_index]
optimal_loss = losses[max_index]
optimal_output = ac_power[max_index]

# Efficiency at actual operating point
actual_loss = (
    constant_loss
    + variable_loss_factor * (dc_power ** 2 / rated_power)
)

actual_output = dc_power - actual_loss

if dc_power > 0:
    actual_efficiency = (actual_output / dc_power) * 100
else:
    actual_efficiency = 0

# Results
print("\n" + "=" * 65)
print("                  OPTIMIZATION RESULTS")
print("=" * 65)

print(f"Rated Inverter Power       : {rated_power:.2f} kW")
print(f"Actual DC Input Power      : {dc_power:.2f} kW")
print(f"Actual AC Output Power     : {actual_output:.2f} kW")
print(f"Actual Power Loss          : {actual_loss:.3f} kW")
print(f"Actual Efficiency          : {actual_efficiency:.2f} %")

print("\n--- OPTIMUM OPERATING POINT ---")

print(f"Optimal DC Power           : {optimal_power:.2f} kW")
print(f"Optimal AC Output          : {optimal_output:.2f} kW")
print(f"Minimum Power Loss         : {optimal_loss:.3f} kW")
print(f"Maximum Efficiency         : {optimal_efficiency:.2f} %")

print("=" * 65)

# Operating condition analysis
if actual_efficiency >= 95:
    print("Inverter Status             : HIGHLY EFFICIENT")
elif actual_efficiency >= 90:
    print("Inverter Status             : EFFICIENT")
elif actual_efficiency >= 80:
    print("Inverter Status             : MODERATELY EFFICIENT")
else:
    print("Inverter Status             : LOW EFFICIENCY")

# Optimization recommendation
if dc_power < optimal_power:
    print("Recommendation              : Increase inverter loading.")
elif dc_power > optimal_power:
    print("Recommendation              : Reduce inverter loading.")
else:
    print("Recommendation              : Operating near optimum point.")

print("=" * 65)

# Plot efficiency curve
plt.figure(figsize=(10, 6))

plt.plot(
    power_values,
    efficiency,
    label="Inverter Efficiency"
)

plt.scatter(
    optimal_power,
    optimal_efficiency,
    s=80,
    label="Optimum Point"
)

plt.xlabel("DC Input Power (kW)")
plt.ylabel("Efficiency (%)")
plt.title("Solar Inverter Efficiency Optimization")
plt.grid(True)
plt.legend()

plt.show()
