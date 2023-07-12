from Point import Point
from Connection import Connection
import random
from math import sqrt

point_to_generate = 10
grid_size = 9
chunks_to_make = 2

points = []
distances = []
chunks = []

def find_dist(point1: Point, point2: Point) -> int:
    return sqrt(pow(point1.z - point2.z, 2) + (pow(point1.x - point2.x, 2) + pow(point1.y - point2.y, 2)))

for i in range(0, point_to_generate):
    new_point = Point(i, random.randint(0, grid_size), random.randint(0, grid_size), random.randint(0, grid_size))
    #print(new_point)
    for point in points:
        if new_point.x == point.x and new_point.y == point.y and new_point.z == point.z:
            i -= 1
            break
    points.append(new_point)

for point in points:
    for i in range(int(point.id) + 1, len(points)):
        dist = find_dist(point, points[i])
        distances.append(Connection(point.id, points[i].id, dist))

distances.sort()
reached_points = []

for dist in distances:
    pass

for dist in distances:
    print(dist)