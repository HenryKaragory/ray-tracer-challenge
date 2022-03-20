FLOAT_EQ_TOLERANCE = 0.0001


def is_float_equal(a: float, b: float):
    return abs(a - b) < FLOAT_EQ_TOLERANCE
