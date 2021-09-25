from pydantic import BaseModel

class Point(BaseModel):
    x: int = 0
    y: int = 0

    def __str__(self):
        return f"X: {self.x:.2f} | Y: {self.y:.2f}"