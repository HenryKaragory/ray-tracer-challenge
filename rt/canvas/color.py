import typing


class Color:
    def __init__(self, r: float, g: float, b: float):
        self._tuple = (r, g, b)

    @property
    def r(self) -> float:
        return self._tuple[0]

    @property
    def g(self) -> float:
        return self._tuple[1]

    @property
    def b(self) -> float:
        return self._tuple[2]

    def __add__(self, other: 'Color') -> 'Color':
        return Color(
            self.r + other.r,
            self.g + other.g,
            self.b + other.b,
        )

    def __sub__(self, other: 'Color') -> 'Color':
        return Color(
            self.r - other.r,
            self.g - other.g,
            self.b - other.b,
        )

    def __mul__(self, other: typing.Any) -> 'Color':
        if isinstance(other, int) or isinstance(other, float):
            return Color(
                self.r * other,
                self.g * other,
                self.b * other
            )
        elif isinstance(other, Color):
            return Color(
                self.r * other.r,
                self.g * other.g,
                self.b * other.b
            )
        else:
            raise NotImplementedError()
