from rt.canvas.color import Color


class Canvas:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        self._canvas = [[0 for _ in width] for _ in height]

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def write_pixel(self, width_index: int, height_index: int, color: Color) -> None:
        if width_index < 0 or width_index >= self.width \
                or height_index < 0 or height_index >= self.height:
            ex_str = f"Attemped to write pixel to invalid spot (w, h) = \
                 ({str(width_index)}, {str(height_index)}). \
                    Actual (w,h) = ({str(self.width)}, {str(self.height)})"
            raise Exception(ex_str)

        self._canvas[height_index][width_index] = color
