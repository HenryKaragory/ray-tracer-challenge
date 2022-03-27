from rt.canvas.color import Color


class Canvas:
    PPM_FLAVOR = 'P3'
    MAX_COLOR_VALUE = 255
    PPM_MAX_LINE_CHARS = 70

    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        # Every pixel is black to begin
        self._canvas = [[Color(0, 0, 0) for _ in range(width)]
                        for _ in range(height)]

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def _throw_if_out_of_bounds(self, height_index: int,
                                width_index: int) -> None:
        if width_index < 0 or width_index >= self.width \
                or height_index < 0 or height_index >= self.height:
            ex_str = f"Attemped to write pixel to invalid spot (w, h) = \
                 ({str(width_index)}, {str(height_index)}). \
                    Actual (w,h) = ({str(self.width)}, {str(self.height)})"

            raise Exception(ex_str)

    def write_pixel(self, height_index: int, width_index: int,
                    color: Color) -> None:
        self._throw_if_out_of_bounds(height_index, width_index)
        self._canvas[height_index][width_index] = color

    def pixel_at(self, height_index: int, width_index: int) -> Color:
        self._throw_if_out_of_bounds(height_index, width_index)
        return self._canvas[height_index][width_index]

    @classmethod
    def _get_scaled_color_str(cls, color: Color) -> str:
        scaled_red = min(color.red * cls.MAX_COLOR_VALUE, cls.MAX_COLOR_VALUE)
        scaled_green = min(color.green * cls.MAX_COLOR_VALUE,
                           cls.MAX_COLOR_VALUE)
        scaled_blue = min(color.blue * cls.MAX_COLOR_VALUE,
                          cls.MAX_COLOR_VALUE)

        return f"{str(scaled_red)} {str(scaled_green)} {str(scaled_blue)}"

    def to_ppm(self) -> str:
        ppm_lines = [
            Canvas.PPM_FLAVOR, f"{str(self.width)} {str(self.height)}",
            str(Canvas.MAX_COLOR_VALUE)
        ]

        # No line should be longer than 70 charactesrs
        current_line = ''
        for row in self._canvas:
            for color_pixel in row:
                color_str = Canvas._get_scaled_color_str(color_pixel)

                if len(current_line) + len(
                        color_str) > Canvas.PPM_MAX_LINE_CHARS:
                    ppm_lines.append(current_line)
                    current_line = color_str
                elif len(current_line) == 0:
                    current_line = color_str
                else:
                    current_line = current_line + ' ' + color_str

        if len(current_line) > 0:
            ppm_lines.append(current_line)

        return '\n'.join(ppm_lines) + "\n"
