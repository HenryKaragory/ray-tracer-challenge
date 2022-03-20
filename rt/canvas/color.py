import typing


class Color:
    def __init__(self, r: float, g: float, b: float):
        self._tuple = (r, g, b)

    @property
    def red(self) -> float:
        return self._tuple[0]

    @property
    def green(self) -> float:
        return self._tuple[1]

    @property
    def blue(self) -> float:
        return self._tuple[2]

    def __add__(self, other: 'Color') -> 'Color':
        return Color(
            self.red + other.red,
            self.green + other.green,
            self.blue + other.blue,
        )

    def __sub__(self, other: 'Color') -> 'Color':
        return Color(
            self.red - other.red,
            self.green - other.green,
            self.blue - other.blue,
        )

    def __mul__(self, other: typing.Any) -> 'Color':
        if isinstance(other, int) or isinstance(other, float):
            return Color(
                self.red * other,
                self.green * other,
                self.blue * other
            )
        elif isinstance(other, Color):
            return Color(
                self.red * other.red,
                self.green * other.green,
                self.blue * other.blue
            )
        else:
            raise NotImplementedError()
