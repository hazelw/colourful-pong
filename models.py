class Shape:
    def update_colour(self, colour):
        # Check that we actually have a valid RGB value
        assert len(colour) == 3, 'Colour must be an RGB value'
        for val in colour:
            assert type(val) == int
            assert val <= 255
            assert val >= 0

        self.colour = colour


class Ball(Shape):
    def __init__(self, radius, width, colour=(0, 0, 0)):
        self.radius = radius
        self.width = width
        self.update_colour(colour)

    def update_radius(self, radius):
        self.radius = radius

    def update_width(self, width):
        self.width = width


class Paddle(Shape):
    def __init__(self, height, width, colour=(0, 0, 0)):
        self.height = height
        self.width = width
        self.update_colour(colour)
