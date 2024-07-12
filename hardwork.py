import math
import matplotlib.pyplot as plt
import numpy as np

# Task1
# Constants
dt = 0.01
alpha = 0.01
initial_conditions = [(1.0, 1.0), (1.0, 2.0)]

# Velocity components
def u(x, y):
    return y

def v(x, y):
    return -math.sin(x)

# Robert-Asselin filter
def robert_asselin_filter(previous, current, future, alpha):
    return current + alpha / 2.0 * (previous - 2.0 * current + future)

# Define the grid for the streamplot
x = np.linspace(-5, 30, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Calculate the velocity components on the grid
U = Y
V = -np.sin(X)

# Plot the streamplot
plt.streamplot(X, Y, U, V, density=[1.9, 1.9], minlength=1.002, arrowstyle='-')

# Trajectory calculation
for x0, y0 in initial_conditions:
    x_values = [x0]
    y_values = [y0]

    x_values.append(x_values[0] + dt * u(x_values[0], y_values[0]))
    y_values.append(y_values[0] + dt * v(x_values[0], y_values[0]))

    for t in range(2, int(20 / dt)):
        x_values.append(x_values[t - 2] + 2.0 * dt * u(x_values[t - 1], y_values[t - 1]))
        y_values.append(y_values[t - 2] + 2.0 * dt * v(x_values[t - 1], y_values[t - 1]))

        x_values[t - 1] = robert_asselin_filter(x_values[t - 2], x_values[t - 1], x_values[t], alpha)
        y_values[t - 1] = robert_asselin_filter(y_values[t - 2], y_values[t - 1], y_values[t], alpha)

    plt.plot(x_values, y_values, label=f'Initial position: ({x0}, {y0})')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Trajectory of an air parcel in the flow')
plt.legend()
plt.show()

# Task2
# Constants
epsilon = 0.1
k = 1.0
c = 3.0
initial_conditions = [(1.0, 1.70), (1.0, 1.71)]

# Velocity components
def u_new(x, y, t):
    return y

def v_new(x, y, t):
    return -math.sin(x) - epsilon * k * math.sin(k * (x - c * t))

U_new = -Y
V_new = np.sin(X) - epsilon * k * np.sin(k * (X - c))

plt.streamplot(X, Y, U_new, V_new, density=[1.9, 1.9], minlength=1.002, arrowstyle='-')

# Trajectory calculation
for x0, y0 in initial_conditions:
    x_values = [x0]
    y_values = [y0]

    x_values.append(x_values[0] + dt * u_new(x_values[0], y_values[0], 0))
    y_values.append(y_values[0] + dt * v_new(x_values[0], y_values[0], 0))

    for t in range(2, int(20 / dt)):
        x_values.append(x_values[t - 2] + 2.0 * dt * u_new(x_values[t - 1], y_values[t - 1], dt * t))
        y_values.append(y_values[t - 2] + 2.0 * dt * v_new(x_values[t - 1], y_values[t - 1], dt * t))

        x_values[t - 1] = robert_asselin_filter(x_values[t - 2], x_values[t - 1], x_values[t], alpha)
        y_values[t - 1] = robert_asselin_filter(y_values[t - 2], y_values[t - 1], y_values[t], alpha)

    plt.plot(x_values, y_values, label=f'Initial position: ({x0}, {y0})')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Trajectory of an air parcel in the flow with modified streamfunction')
plt.legend()
plt.show()

for x0, y0 in initial_conditions:
    print(f'For initial position ({x0}, {y0}), the coordinates at t=20 are ({x_values[-1]}, {y_values[-1]})')

# Task3
epsilon = 0.0

U_original = Y
V_original = -np.sin(X)

plt.streamplot(X, Y, U_original, V_original, density=[1.9, 1.9], minlength=1.002, arrowstyle='-')

# Trajectory calculation
for x0, y0 in initial_conditions:
    x_values = [x0]
    y_values = [y0]

    x_values.append(x_values[0] + dt * u(x_values[0], y_values[0]))
    y_values.append(y_values[0] + dt * v(x_values[0], y_values[0]))

    for t in range(2, int(20 / dt)):
        x_values.append(x_values[t - 2] + 2.0 * dt * u(x_values[t - 1], y_values[t - 1]))
        y_values.append(y_values[t - 2] + 2.0 * dt * v(x_values[t - 1], y_values[t - 1]))

        x_values[t - 1] = robert_asselin_filter(x_values[t - 2], x_values[t - 1], x_values[t], alpha)
        y_values[t - 1] = robert_asselin_filter(y_values[t - 2], y_values[t - 1], y_values[t], alpha)

    plt.plot(x_values, y_values, label=f'Initial position: ({x0}, {y0})')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Trajectory of an air parcel in the flow with original streamfunction')
plt.legend()
plt.show()

for x0, y0 in initial_conditions:
    print(f'For initial position ({x0}, {y0}), the coordinates at t=20 are ({x_values[-1]}, {y_values[-1]})')
