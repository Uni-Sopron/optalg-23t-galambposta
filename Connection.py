class Connection:

    def __init__(self, point1_id, point2_id, dist) -> None:
        self.point1_id = point1_id
        self.point2_id = point2_id
        self.dist = dist

    def __str__(self) -> str:
        return f"{self.point1_id} - {self.point2_id}: {self.dist}"
    
    def __lt__(self, obj):
        return ((self.dist) < (obj.dist))
