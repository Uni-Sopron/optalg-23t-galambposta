from Point import Point
from Connection import Connection
import random
from math import sqrt

point_to_generate = 10
grid_size = 9
chunks_to_make = 2

points = []
distances = []

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
end_dists = []

reached_points.append(distances[0].point1_id)
reached_points.append(distances[0].point2_id)
end_dists.append(distances[0])
distances.remove(distances[0])

while len(end_dists) < len(points) - 1:
    new_min = Connection(grid_size + 1, grid_size + 1, sqrt(3 * pow(grid_size, 2)) + 1)
    for point in reached_points:
        for dist in distances:
            if dist.point1_id == point or dist.point2_id == point and dist.dist < new_min.dist:
                new_min = dist

    end_dists.append(new_min)
    if reached_points.count(new_min.point1_id) > 0:
        reached_points.append(new_min.point2_id)
    else:
        reached_points.append(new_min.point1_id)

    to_remove = []
    for i in range(0,len(distances)):
        for d1 in range(0, len(end_dists) - 1):
            for d2 in range(d1 + 1, len(end_dists) - 1):
                if distances[i].point1_id == reached_points[d1] and distances[i].point2_id == reached_points[d2] or distances[i].point1_id == reached_points[d2] and distances[i].point2_id == reached_points[d1]:
                    
                    to_remove.append(i)

    print(to_remove)
    pass

for dist in distances:
    print(dist)
