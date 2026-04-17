import numpy as np
import random

def midpoint_displacement(x1, y1, x2, y2, roughness, depth, points):
    if depth == 0:
        return

    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2

    offset = roughness * random.uniform(-1, 1)
    mid_y += offset

    points.append((mid_x, mid_y))

    midpoint_displacement(x1, y1, mid_x, mid_y, roughness, depth - 1, points)
    midpoint_displacement(mid_x, mid_y, x2, y2, roughness, depth - 1, points)

def generate_terrain(size, roughness):
    grid = np.zeros((size, size))

    step = size - 1

    while step > 1:
        half = step // 2

        # Diamond step
        for x in range(half, size, step):
            for y in range(half, size, step):
                avg = (
                    grid[x-half][y-half] +
                    grid[x-half][y+half] +
                    grid[x+half][y-half] +
                    grid[x+half][y+half]
                ) / 4
                grid[x][y] = avg + random.uniform(-roughness, roughness)

        for x in range(0, size, half):
            for y in range((x + half) % step, size, step):
                avg = []
                if x - half >= 0:
                    avg.append(grid[x-half][y])
                if x + half < size:
                    avg.append(grid[x+half][y])
                if y - half >= 0:
                    avg.append(grid[x][y-half])
                if y + half < size:
                    avg.append(grid[x][y+half])

                grid[x][y] = sum(avg) / len(avg) + random.uniform(-roughness, roughness)

        step //= 2
        roughness *= 0.5

    return grid

def detect_artifacts(grid, threshold):
    rows = len(grid)
    cols = len(grid[0])
    artifacts = []

    for i in range(rows - 1):
        for j in range(cols - 1):
            if abs(grid[i][j] - grid[i+1][j]) > threshold or \
               abs(grid[i][j] - grid[i][j+1]) > threshold:
                artifacts.append((i, j))

    return artifacts


if __name__ == "__main__":
    points = [(0, 0), (100, 0)]

    midpoint_displacement(0, 0, 100, 0, 10, 5, points)

    print("Generated points:")
    for p in points:
        print(p)

    terrain = generate_terrain(9, 5)  

    print(terrain)

    artifacts = detect_artifacts(terrain, threshold=2)

    print("Artifacts:", artifacts)

