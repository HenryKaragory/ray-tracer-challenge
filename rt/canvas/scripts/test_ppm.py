from rt.canvas.color import Color
from rt.canvas.canvas import Canvas

if __name__ == '__main__':
    my_canvas = Canvas(100, 100)
    for r in range(25):
        for c in range(25):
            my_canvas.write_pixel(r, c, Color(0.25, .5, .6))

    ppm = my_canvas.to_ppm()
    with open("test.ppm", "w") as f:
        f.write(ppm)
