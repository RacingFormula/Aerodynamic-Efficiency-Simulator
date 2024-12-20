import numpy as np
import matplotlib.pyplot as plt

class AerodynamicEfficiencySimulator:
    def __init__(self, config):
        self.drag_coefficient = config.get("drag_coefficient", 0.3)
        self.downforce_coefficient = config.get("downforce_coefficient", 2.0)
        self.frontal_area = config.get("frontal_area", 1.5)  # m^2
        self.air_density = config.get("air_density", 1.225)  # kg/m^3 (sea level)
        self.vehicle_mass = config.get("vehicle_mass", 800)  # kg
        self.speeds = config.get("speeds", np.linspace(10, 100, 50))  # m/s

    def calculate_aerodynamic_forces(self):
        drag_forces = []
        downforce = []
        lift_to_drag_ratios = []

        for speed in self.speeds:
            drag = 0.5 * self.air_density * self.frontal_area * self.drag_coefficient * speed**2
            down = 0.5 * self.air_density * self.frontal_area * self.downforce_coefficient * speed**2

            drag_forces.append(drag)
            downforce.append(down)
            lift_to_drag_ratios.append(down / drag if drag > 0 else 0)

        return {
            "speeds": self.speeds,
            "drag_forces": drag_forces,
            "downforce": downforce,
            "lift_to_drag_ratios": lift_to_drag_ratios
        }

    def plot_results(self, results):
        speeds = results["speeds"]
        drag_forces = results["drag_forces"]
        downforce = results["downforce"]
        lift_to_drag_ratios = results["lift_to_drag_ratios"]

        plt.figure(figsize=(14, 10))

        # Plot Drag Forces
        plt.subplot(3, 1, 1)
        plt.plot(speeds, drag_forces, label="Drag Force", color="blue")
        plt.title("Drag Force vs Speed")
        plt.xlabel("Speed (m/s)")
        plt.ylabel("Drag Force (N)")
        plt.legend()
        plt.grid(True)

        # Plot Downforce
        plt.subplot(3, 1, 2)
        plt.plot(speeds, downforce, label="Downforce", color="red")
        plt.title("Downforce vs Speed")
        plt.xlabel("Speed (m/s)")
        plt.ylabel("Downforce (N)")
        plt.legend()
        plt.grid(True)

        # Plot Lift-to-Drag Ratio
        plt.subplot(3, 1, 3)
        plt.plot(speeds, lift_to_drag_ratios, label="Lift-to-Drag Ratio", color="green")
        plt.title("Lift-to-Drag Ratio vs Speed")
        plt.xlabel("Speed (m/s)")
        plt.ylabel("Lift-to-Drag Ratio")
        plt.legend()
        plt.grid(True)

        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    config = {
        "drag_coefficient": 0.3,
        "downforce_coefficient": 2.0,
        "frontal_area": 1.5,
        "air_density": 1.225,
        "vehicle_mass": 800,
        "speeds": np.linspace(10, 100, 50)
    }

    simulator = AerodynamicEfficiencySimulator(config)
    results = simulator.calculate_aerodynamic_forces()
    simulator.plot_results(results)