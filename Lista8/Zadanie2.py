import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

N = 200
updateInterval = 400

ON = 255
OFF = 0
vals = [ON, OFF]


def randomGrid(N):
    return np.random.choice(vals, N * N).reshape(N, N)


def update(frameNum, img, grid, N):
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            total = int((grid[i, (j - 1) % N] + grid[i, (j + 1) % N] + grid[(i - 1) % N, j] + grid[(i + 1) % N, j] +
                         grid[(i - 1) % N, (j - 1) % N] + grid[(i - 1) % N, (j + 1) % N] + grid[
                             (i + 1) % N, (j - 1) % N] + grid[(i + 1) % N, (j + 1) % N]) / 255)
            if grid[i, j] == ON:
                if not total == 3:
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,


grid = randomGrid(N)

fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='none')
ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N), frames=50, interval=updateInterval)
plt.show()
