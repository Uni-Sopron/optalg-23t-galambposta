class Point:

    def __init__(self, id, x, y, z) -> None:
        self.id = id
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f"Id:{self.id}: [{self.x};{self.y};{self.z}] Dists: {self.dists}"