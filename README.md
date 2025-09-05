# Pendulum_simulator
This project demonstrates applied physics and Python programming through a visual, interactive pendulum simulation. It computes and animates position, velocity, acceleration, forces, and energy of a simple pendulum from first principles using a custom `Draw` library.

## Features
- Computes real-time position, velocity, and acceleration
- Visualizes vectors: velocity, tangential/radial acceleration
- Displays forces: tension and weight
- Graphs kinetic, potential, and total mechanical energy
- Modular parameters: pendulum length, mass, amplitude, and timestep
- Interactive animations: plain, velocity, acceleration, forces, and energy modes

## Physics
- Assumes small-angle approximation
- No damping or air resistance

## How to Run
1. Install Python 3.x
2. Ensure `Draw.py` is in the same folder as the main script
3. Run the main script:
   ```bash
   python pendulum.py
