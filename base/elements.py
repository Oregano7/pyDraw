from abc import ABC, abstractmethod

from pydantic import Field
from pydantic.dataclasses import dataclass
from structures import Point


class Element(ABC):
    """
    Base class for all elements
    """

    @abstractmethod
    def generate(self):
        """
        Returns a iterator to generate the points for given element
        """
        pass

    @abstractmethod
    def animate(self):
        """
        Sets attributes to control the animation
        These attributes affect generation
        """
        pass

    @abstractmethod
    def draw(self):
        """
        Draw the element onto a canvas
        """
        pass


@dataclass
class Line(Element):
    """
    Creates a Line object based on DDA Line Generation Algorithm
    """

    point1: Point = Field(default_factory=Point)
    point2: Point = Field(default_factory=Point)

    speed: float = 1

    def generate(self) -> Point:
        """
        Returns an iterable for all points of a line from point1 to point2
        """

        diff_x = self.point2.x - self.point1.x
        diff_y = self.point2.y - self.point1.y

        steps = max(abs(diff_x), abs(diff_y))
        steps //= self.speed

        x_inc = float(diff_x) / steps
        y_inc = float(diff_y) / steps

        point = Point.parse_obj(self.point1)
        for step in range(steps + 1):  # +1 to return the end point as well
            yield point
            point.x += x_inc
            point.y += y_inc

    def animate(self, speed: float = 1) -> None:
        """
        Sets the speed of the line
        <1 means slower
        >1 means faster
        """
        self.speed = speed

    def draw(self):
        pass


@dataclass
class Curve(Element):
    """
    Creates a Curve object based on Bresenham circle algorithm
    """

    center: Point = Field(default_factory=Point)
    radius: float = 0.0

    def generate(self) -> Point:
        """
        Returns an iterable for all points of a curve of set radius about set center
        """
        p = 3 - 2 * self.radius
        x_offset, y_offset = 0, self.radius
        while x_offset <= y_offset:
            yield Point(x=self.center.x + x_offset, y=self.center.y + y_offset)
            if p <= 0:
                p += (4 * x_offset) + 6
            else:
                p += (4 * (x_offset - y_offset)) + 10
                y_offset -= 1
            x_offset += 1

    def animate(self):
        pass

    def draw(self):
        pass



def line_generator():
    """
    Useful for animation
    """


if __name__ == "__main__":

    print("=== LINE TEST ===")
    line = Line(point1=Point(x=2, y=3), point2=Point(x=8, y=12))
    line.animate(speed=2)
    line_gen = line.generate()
    for point in line_gen:
        print(point)
    print("=== LINE TEST COMPLETE ===")


    print("=== CURVE TEST ===")
    curve = Curve(center=Point(x=1,y=5), radius=7.8)
    curve_gen = curve.generate()
    for point in curve_gen:
        print(point)
    print("=== CURVE TEST COMPLETE ===")
