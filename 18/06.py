def find_farthest_orbit(list_of_orbits):
    return list(filter(lambda a: a[0] * a[1] * 3.14 == max(
        list(map(lambda a: 3.14 * a[0] * a[1], [(i, j) for i, j in list_of_orbits if i != j]))),
                       [(i, j) for i, j in list_of_orbits if i != j]))[0][0], list(
        filter(lambda a: a[0] * a[1] * 3.14 == max(
            list(map(lambda a: 3.14 * a[0] * a[1], [(i, j) for i, j in list_of_orbits if i != j]))),
               [(i, j) for i, j in list_of_orbits if i != j]))[0][1]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))