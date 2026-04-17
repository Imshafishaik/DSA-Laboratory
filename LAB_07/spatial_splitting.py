import random

def split_region(x, y, width, height, min_size, regions):
    if width <= min_size or height <= min_size:
        regions.append((x, y, width, height))
        return

    half_w = width // 2
    half_h = height // 2

    split_region(x, y, half_w, half_h, min_size, regions)
    split_region(x + half_w, y, half_w, half_h, min_size, regions)
    split_region(x, y + half_h, half_w, half_h, min_size, regions)
    split_region(x + half_w, y + half_h, half_w, half_h, min_size, regions)

def count_points_in_region(points, region):
    x, y, w, h = region
    count = 0

    for px, py in points:
        if x <= px < x + w and y <= py < y + h:
            count += 1

    return count

def find_dense_regions(points, x, y, width, height, min_size, density_threshold, result):
    region = (x, y, width, height)
    count = count_points_in_region(points, region)

    area = width * height
    density = count / area if area > 0 else 0

    if width <= min_size or height <= min_size:
        if density > density_threshold:
            result.append(region)
        return

    if density > density_threshold:
        result.append(region)

    half_w = width // 2
    half_h = height // 2

    find_dense_regions(points, x, y, half_w, half_h, min_size, density_threshold, result)
    find_dense_regions(points, x + half_w, y, half_w, half_h, min_size, density_threshold, result)
    find_dense_regions(points, x, y + half_h, half_w, half_h, min_size, density_threshold, result)
    find_dense_regions(points, x + half_w, y + half_h, half_w, half_h, min_size, density_threshold, result)


if __name__ == "__main__":
    points = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(100)]

    regions = []
    split_region(0, 0, 100, 100, 10, regions)

    print("Total regions:", len(regions))

    dense_regions = []
    find_dense_regions(points, 0, 0, 100, 100, 10, 0.02, dense_regions)

    print("Dense regions:", dense_regions)