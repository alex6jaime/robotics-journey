import numpy as np
import matplotlib.pyplot as plt
from numpy_practice import rot2d

angles = np.linspace(0, 2 * np.pi, 200) # 200 angles from 0 to 2*pi

plt.figure()
plt.plot(angles, np.sin(angles), label='sin')
plt.plot(angles, np.cos(angles), label='cos')

plt.xlabel("Angle (radians)")
plt.ylabel("Value")
plt.title("Sine and cosine")
plt.legend()
plt.grid(True)
plt.savefig("sine_cosine.png", dpi=150, bbox_inches="tight")

#-----------------------------------------

square = np.array([
    [0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0]
], dtype=float)

plt.figure()

for degrees in [0, 45, 90]:
    theta = np.deg2rad(degrees)
    rotated = rot2d(theta) @ square

    plt.plot(
        rotated[0, :],
        rotated[1, :],
        marker='o',
        label=f"{degrees} degrees"
    )

plt.scatter(0, 0, color="black", zorder=5)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Unit square rotated about the origin")
plt.legend()
plt.grid(True)
plt.axis("equal")

plt.savefig("rotated_square.png", dpi=150, bbox_inches="tight")
plt.show()