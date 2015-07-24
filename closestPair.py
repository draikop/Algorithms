import math

def distance(m, n):
    return math.hypot(m[0] - n[0], m[1] - n[1])

def closestPair(points):
    points.sort(lambda x, y: cmp(x[0], y[0]))

    minimum_distance = None
    minimum_pair = None

    point_count = len(points)

    i = 0
    while i < point_count:
        left_point = points[i]

        j = i + 1
        while j < point_count:
            right_point = points[j]

            # if the x delta is greater than the current minimum distance,
            # then the rest of the list can be skipped, since it's sorted by x
            if minimum_distance is not None and right_point[0] - left_point[0] >= minimum_distance:
                break

            current_distance = distance(left_point, right_point)

            if minimum_distance is None or current_distance < minimum_distance:
                minimum_distance = current_distance
                minimum_pair = (left_point, right_point)
            j += 1
        i += 1

    return minimum_pair

def main():
    import random
    points = [(random.randint(-10000,10000), random.randint(-10000,10000)) for i in range(1000)]
    print closestPair(points)

if __name__ == '__main__':
    main()
1