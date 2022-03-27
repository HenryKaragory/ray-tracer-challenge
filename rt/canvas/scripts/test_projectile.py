from rt.tuple.rt_tuple import Tuple, make_point, make_vector
from rt.canvas.canvas import Canvas, Color


class Projectile:

    def __init__(self, position: Tuple, velocity: Tuple):
        self._position = position
        self._velocity = velocity

    @property
    def position(self):
        return self._position

    @property
    def velocity(self):
        return self._velocity


class Environment:

    def __init__(self, gravity: Tuple, wind: Tuple):
        self._gravity = gravity
        self._wind = wind

    @property
    def gravity(self):
        return self._gravity

    @property
    def wind(self):
        return self._wind


def tick(env: Environment, proj: Projectile) -> Projectile:
    new_position = proj.position + proj.velocity
    new_velocity = proj.velocity + env.gravity + env.wind
    return Projectile(new_position, new_velocity)


if __name__ == '__main__':
    projectile = Projectile(make_point(0, 1, 0),
                            make_vector(1, 1.8, 0).normalize() * 11.25)

    environment = Environment(make_vector(0, -0.1, 0),
                              make_vector(-0.01, 0, 0))

    canvas_height = 550
    canvas_width = 900
    canvas = Canvas(canvas_width, canvas_height)

    canvas_y = int(canvas_height - projectile.position.y)
    canvas_x = int(projectile.position.x)
    n = 0
    while canvas_x >= 0 and canvas_y >= 0 and canvas_y < canvas_height and canvas_x < canvas_width:
        n += 1
        canvas.write_pixel(canvas_y, canvas_x, Color(1, 0, 0))

        projectile = tick(environment, projectile)
        canvas_y = int(canvas_height - projectile.position.y)
        canvas_x = int(projectile.position.x)

    ppm_file_str = canvas.to_ppm()
    with open("test.ppm", "w") as f:
        f.write(ppm_file_str)

    print("All done running the simulation.")
    print(f"n = {str(n)}")
