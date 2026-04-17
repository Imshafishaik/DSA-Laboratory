import turtle
import numpy as np

def draw_triangle(t, x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for _ in range(3):
        t.forward(size)
        t.left(120)

def draw_sierpinski(t, x, y, size, depth):
    if depth == 0:
        draw_triangle(t, x, y, size)
        return

    half = size / 2
    # Recursively draw three smaller triangles
    draw_sierpinski(t, x, y, half, depth - 1)
    draw_sierpinski(t, x + half, y, half, depth - 1)
    draw_sierpinski(t, x + half / 2, y + (half * (3**0.5)/2), half, depth - 1)

def draw_tree(t, length, depth):
    if depth == 0:
        return

    t.forward(length)
    t.left(30)
    draw_tree(t, length * 0.7, depth - 1)

    t.right(60)
    draw_tree(t, length * 0.7, depth - 1)

    t.left(30)
    t.backward(length)

def fractal_dimension(fractal_image, box_sizes):
    counts = []
    for size in box_sizes:
        count = 0
        for i in range(0, len(fractal_image), size):
            for j in range(0, len(fractal_image[0]), size):
                box = fractal_image[i:i+size, j:j+size]
                if np.any(box):
                    count += 1
        counts.append(count)

    log_sizes = np.log(1 / np.array(box_sizes))
    log_counts = np.log(counts)
    slope, _ = np.polyfit(log_sizes, log_counts, 1)
    return slope

if __name__ == "__main__":
    # Setup Screen
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0) # Fastest setting
    
    # Draw Sierpinski
    draw_sierpinski(t, -200, -100, 200, 4)
    
    # Move to a new spot for the tree
    t.penup()
    t.goto(150, -100)
    t.setheading(90) # Face upwards
    t.pendown()
    
    # Draw Tree
    draw_tree(t, 70, 7)
    
    turtle.done()