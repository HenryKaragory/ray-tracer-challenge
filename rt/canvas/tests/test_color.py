import unittest
from rt.canvas.canvas import Canvas


class TestCanvas(unittest.TestCase):

    def test_ppm_header(self):
        canvas = Canvas(10, 20)
        ppm_str_lines = canvas.to_ppm().split('\n')

        self.assertEqual(ppm_str_lines[0], "P3")
        self.assertEqual(ppm_str_lines[1],  "10 20")
        self.assertEqual(ppm_str_lines[2], "255")
