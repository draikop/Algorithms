def squaresum(m, n):
    return ((m[0] - n[0]) ** 2 + (m[1] - n[1]) ** 2)

def closestPair(points):
    points.sort(lambda x, y: cmp(x[0], y[0]))

    minimum_distance = None
    minimum_squaresum = None
    closest_pair = None

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

            # don't take the square root unless you need to
            current_squaresum = squaresum(left_point, right_point)

            if minimum_distance is None or current_squaresum < minimum_squaresum:
                minimum_squaresum = current_squaresum
                minimum_distance = minimum_squaresum ** 0.5
                closest_pair = (left_point, right_point)
            j += 1
        i += 1

    return closest_pair

def main():
    import random
    points = [(random.randint(-10000,10000), random.randint(-10000,10000)) for i in range(1000)]
    print closestPair(points)

if __name__ == '__main__':
    main()
