

class Polygon:
    def __init__(self, vertices: int) -> None:
        if vertices < 3:
            raise ValueError
        self.vertices = vertices
    
